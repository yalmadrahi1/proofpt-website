/* Referral intake regression tests — run: `npm test` (invoked alongside intake.test.mjs).
   Extracts and executes the PUBLISHED submit handler straight out of refer.html, so it tests
   the real shipped logic. The headline assertion is the PHI boundary: patient details go to the
   primary (Web3Forms -> BAA'd inbox) but NEVER to the non-BAA CRM mirror, which carries the
   REFERRER contact only (source "referral"). Also covers: full-field validation, success + event,
   primary-before-mirror ordering, request_id correlation, explicit reject, and ambiguous states. */
import {JSDOM} from 'jsdom';
import fs from 'fs';
import path from 'path';
import {fileURLToPath} from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const FILE = 'refer.html';

function extract(){
  const src = fs.readFileSync(path.join(ROOT, FILE),'utf8');
  const form = src.match(/<form id="refer"[\s\S]*?<\/form>/)[0];
  const script = [...src.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1])
    .find(s=>s.includes("addEventListener('submit'"));
  if(!form || !script) throw new Error('could not extract form/script from '+FILE);
  return {form, script};
}

function harness(){
  const {form, script} = extract();
  const dom = new JSDOM('<!doctype html><html><body><section>'+form+'</section></body></html>', {runScripts:'outside-only'});
  const w = dom.window;
  const calls = {order:[], fetch:[], beacon:[], accepted:[]};
  w.navigator.sendBeacon = (url, body)=>{ calls.beacon.push({url, body:String(body)}); calls.order.push('beacon'); return true; };
  w.document.addEventListener('proof:accepted', e=> calls.accepted.push(e.detail));
  w.__mode = 'success';
  w.fetch = (url, opts)=>{
    calls.fetch.push({url, opts}); calls.order.push('fetch:'+(/web3forms/.test(url)?'primary':'other'));
    if(/web3forms/.test(url)){
      const m = w.__mode;
      if(m==='success')    return Promise.resolve({ok:true, json:()=>Promise.resolve({success:true})});
      if(m==='reject')     return Promise.resolve({ok:true, json:()=>Promise.resolve({success:false})});
      if(m==='neterr')     return Promise.reject(new Error('network down'));
      if(m==='unreadable') return Promise.resolve({ok:true, json:()=>Promise.reject(new Error('bad json'))});
      if(m==='timeout')    return new Promise((_,rej)=>{ opts.signal && opts.signal.addEventListener('abort', ()=>rej(new w.DOMException('aborted','AbortError'))); });
    }
    return Promise.resolve({ok:true, json:()=>Promise.resolve({success:true})});
  };
  const realST = w.setTimeout; w.setTimeout = (fn,ms)=> ms===15000 ? realST(fn,5) : realST(fn,ms);
  w.eval(script);
  const set = (id,val)=>{ const el=w.document.getElementById(id); if(el) el.value = val; };
  const fill = (o={})=>{
    set('rname', 'rname' in o ? o.rname : 'Dr Jane Smith');
    set('rorg',  'rorg'  in o ? o.rorg  : 'Smith Orthopedics');
    set('rcontact','rcontact' in o ? o.rcontact : 'referrals@smithortho.com');
    set('pname', 'pname' in o ? o.pname : 'John Patient');
    set('pcontact','pcontact' in o ? o.pcontact : '586-555-0199');
    set('rrole', o.rrole || 'Physician');
    set('preason', o.preason || '');
    set('pcoverage', o.pcoverage || '');
    set('pnote', 'pnote' in o ? o.pnote : 'Post-op ACL, 6 weeks, avoid open-chain');
  };
  const submit = ()=> w.document.getElementById('refer').dispatchEvent(new w.Event('submit',{cancelable:true,bubbles:true}));
  const msg = ()=> w.document.getElementById('rmsg').textContent;
  return {w, calls, fill, submit, msg};
}

const sleep = ms=> new Promise(r=>setTimeout(r,ms));
let PASS=true, N=0;
const ok = (cond, m)=>{ N++; if(!cond){PASS=false; console.log('  FAIL:', m);} else console.log('  ok  :', m); };

console.log('\n[refer]');

/* happy path + PHI boundary */
{ const h=harness(); h.fill(); h.submit(); await sleep(30);
  ok(h.calls.fetch.length===1, 'valid referral -> exactly one primary fetch');
  ok(h.calls.accepted.length===1, 'valid referral -> one accepted event');
  ok(h.calls.beacon.length===1, 'valid referral -> CRM mirror fired');
  const body = JSON.parse(h.calls.fetch[0].opts.body);
  ok(body.patient_name==='John Patient' && body.patient_contact==='586-555-0199' && /ACL/.test(body.clinical_note),
     'primary (Web3Forms->BAA inbox) CARRIES patient name, contact, clinical note');
  ok(body.referrer_name==='Dr Jane Smith' && body.referrer_org==='Smith Orthopedics', 'primary carries referrer identity + org');
  const b = h.calls.beacon[0].body;
  ok(!/John|Patient|0199|ACL|avoid|open-chain/.test(b), 'CRM mirror contains NO patient PHI (name/contact/note)');
  ok(/source=referral/.test(b), 'CRM mirror tagged source=referral');
  ok(/first_name=Dr/.test(b) && /last_name=Jane\+Smith/.test(b), 'CRM mirror carries referrer name only');
  ok(/email=referrals%40smithortho\.com/.test(b), 'CRM mirror carries referrer contact (email)');
  const rid=body.request_id;
  ok(!!rid && b.includes('request_id='+rid), 'request_id present + identical in both payloads');
  const fi=h.calls.order.indexOf('fetch:primary'), bi=h.calls.order.indexOf('beacon');
  ok(fi>-1 && bi>-1 && fi<bi, 'ordering: primary fetch BEFORE CRM mirror'); }

/* referrer contact routed as phone when it's a phone */
{ const h=harness(); h.fill({rcontact:'586-555-0100'}); h.submit(); await sleep(30);
  const b=h.calls.beacon[0].body;
  ok(/phone=586-555-0100/.test(b) && !/email=/.test(b), 'phone referrer contact -> mirror sends phone, not email'); }

/* validation: every required field blocks the network when missing/invalid */
const bad = [
  ['rname',    {rname:''},                      'missing referrer name'],
  ['rorg',     {rorg:''},                       'missing organization'],
  ['rcontact', {rcontact:'nope'},               'invalid referrer contact'],
  ['rcontact2',{rcontact:'abc5868008488'},      'alphabetic referrer phone'],
  ['pname',    {pname:''},                      'missing patient name'],
  ['pcontact', {pcontact:''},                   'missing patient contact'],
  ['pcontact2',{pcontact:'123'},                'too-short patient phone'],
];
for(const [label,over,desc] of bad){
  const h=harness(); h.fill(over); h.submit(); await sleep(20);
  ok(h.calls.fetch.length===0 && h.calls.beacon.length===0 && h.calls.accepted.length===0,
     'invalid ('+desc+') -> no network, no event, no mirror');
}

/* fast/autofill submit is not time-gated */
{ const h=harness(); h.fill(); h.submit(); await sleep(20);
  ok(h.calls.fetch.length===1, 'fast/autofill submit is NOT blocked by a time gate'); }

/* explicit reject */
{ const h=harness(); h.w.__mode='reject'; h.fill(); h.submit(); await sleep(30);
  ok(h.calls.accepted.length===0 && h.calls.beacon.length===0, 'explicit reject -> no event, no mirror');
  ok(/wasn.t accepted/i.test(h.msg()), 'explicit reject -> definite "wasnt accepted" copy');
  ok(h.w.document.querySelector('#refer button').disabled===false, 'explicit reject -> button re-enabled'); }

/* ambiguous states */
for(const [mode,desc] of [['neterr','network error'],['unreadable','unreadable response'],['timeout','timeout']]){
  const h=harness(); h.w.__mode=mode; h.fill(); h.submit(); await sleep(60);
  ok(h.calls.accepted.length===0, desc+' -> no accepted event');
  ok(h.calls.beacon.length===0, desc+' -> no CRM mirror on unconfirmed delivery');
  ok(/couldn.t confirm/i.test(h.msg()), desc+' -> "couldnt confirm" (ambiguous, not definite rejection)');
}

/* double-submit guard + retry keeps same request_id */
{ const h=harness(); h.w.__mode='timeout'; h.fill(); h.submit(); await sleep(40);
  const rid1=JSON.parse(h.calls.fetch[0].opts.body).request_id;
  h.w.__mode='success'; h.submit(); await sleep(30);
  const rid2=JSON.parse(h.calls.fetch[1].opts.body).request_id;
  ok(rid1===rid2, 'retry after ambiguous -> SAME request_id (same session)');
  ok(h.calls.accepted.length===1, 'retry success -> accepted event');
  h.submit(); await sleep(20);
  ok(h.calls.fetch.length===2, 'after confirmed success, resubmit is blocked (no 3rd fetch)'); }

console.log('\n'+(PASS ? 'ALL '+N+' REFERRAL TESTS PASS' : 'REFERRAL TEST FAILURES ABOVE'));
process.exit(PASS?0:1);
