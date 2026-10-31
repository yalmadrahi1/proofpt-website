/* Intake regression tests — run: `npm install && npm test`
   Extracts and executes the PUBLISHED submit handler straight out of the deployed HTML
   (request-appointment.html / contact.html), so it tests the real shipped logic, not a
   re-created validator. Covers: valid/invalid contacts, alphabetic-phone rejection, fast
   autofill (no time gate), success + accepted event, primary-before-mirror ordering,
   request_id correlation, explicit rejection, ambiguous network/unreadable/timeout, and
   retry reusing the same session request_id. */
import {JSDOM} from 'jsdom';
import fs from 'fs';
import path from 'path';
import {fileURLToPath} from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

function extract(file, formId){
  const src = fs.readFileSync(path.join(ROOT, file),'utf8');
  const form = src.match(new RegExp('<form id="'+formId+'"[\\s\\S]*?</form>'))[0];
  const script = [...src.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1])
    .find(s=>s.includes("addEventListener('submit'"));
  if(!form || !script) throw new Error('could not extract form/script for #'+formId+' in '+file);
  return {form, script};
}

function harness(file, formId, ids){
  const {form, script} = extract(file, formId);
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
  const submit = (name, contact)=>{
    w.document.getElementById(ids.name).value = name;
    w.document.getElementById(ids.contact).value = contact;
    w.document.getElementById(formId).dispatchEvent(new w.Event('submit', {cancelable:true, bubbles:true}));
  };
  const msg = ()=> w.document.getElementById(ids.msg).textContent;
  return {w, calls, submit, msg};
}

const sleep = ms=> new Promise(r=>setTimeout(r,ms));
let PASS=true, N=0;
const ok = (cond, m)=>{ N++; if(!cond){PASS=false; console.log('  FAIL:', m);} else console.log('  ok  :', m); };

async function runFor(label, file, formId, ids){
  console.log('\n['+label+']');
  for(const good of ['you@email.com','(586) 800-8488','586-800-8488','+1 586 800 8488','5868008488']){
    const h=harness(file,formId,ids); h.submit('Jane Doe', good); await sleep(20);
    ok(h.calls.fetch.length===1, 'valid contact "'+good+'" -> primary fetch fired');
  }
  for(const bad of ['', 'abc', 'abc@', 'abc5868008488', '123']){
    const h=harness(file,formId,ids); h.submit('Jane', bad); await sleep(20);
    ok(h.calls.fetch.length===0 && h.calls.beacon.length===0 && h.calls.accepted.length===0, 'invalid contact "'+bad+'" -> no network, no event');
  }
  { const h=harness(file,formId,ids); h.submit('Jane','abc5868008488'); await sleep(10);
    ok(h.calls.fetch.length===0, 'alphabetic phone "abc5868008488" rejected (not stripped-and-accepted)'); }
  { const h=harness(file,formId,ids); h.submit('Jane Doe','jane@example.com'); await sleep(20);
    ok(h.calls.fetch.length===1 && h.calls.accepted.length===1, 'fast/autofill submit is NOT blocked by a time gate'); }
  { const h=harness(file,formId,ids); h.submit('Jane Doe','jane@example.com'); await sleep(30);
    ok(h.calls.accepted.length===1, 'success -> exactly one accepted event');
    ok(h.calls.beacon.length===1, 'success -> CRM mirror fired');
    const rid=JSON.parse(h.calls.fetch[0].opts.body).request_id;
    ok(!!rid && h.calls.beacon[0].body.includes('request_id='+rid), 'request_id present + identical in both payloads');
    const fi=h.calls.order.indexOf('fetch:primary'), bi=h.calls.order.indexOf('beacon');
    ok(fi>-1 && bi>-1 && fi<bi, 'ordering: primary fetch BEFORE CRM mirror'); }
  { const h=harness(file,formId,ids); h.w.__mode='reject'; h.submit('Jane Doe','jane@example.com'); await sleep(30);
    ok(h.calls.accepted.length===0 && h.calls.beacon.length===0, 'explicit reject -> no event, no CRM mirror');
    ok(/wasn.t accepted/i.test(h.msg()), 'explicit reject -> definite "wasnt accepted" copy');
    ok(h.w.document.querySelector('#'+formId+' button').disabled===false, 'explicit reject -> button re-enabled'); }
  { const h=harness(file,formId,ids); h.w.__mode='neterr'; h.submit('Jane Doe','jane@example.com'); await sleep(30);
    ok(h.calls.accepted.length===0, 'network error -> no accepted event');
    ok(/couldn.t confirm/i.test(h.msg()), 'network error -> "couldnt confirm" (ambiguous, not definite rejection)'); }
  { const h=harness(file,formId,ids); h.w.__mode='unreadable'; h.submit('Jane Doe','jane@example.com'); await sleep(30);
    ok(/couldn.t confirm/i.test(h.msg()), 'unreadable response -> "couldnt confirm"'); }
  { const h=harness(file,formId,ids); h.w.__mode='timeout'; h.submit('Jane Doe','jane@example.com'); await sleep(60);
    ok(/couldn.t confirm/i.test(h.msg()), 'timeout -> "couldnt confirm"');
    const rid1=JSON.parse(h.calls.fetch[0].opts.body).request_id;
    h.w.__mode='success'; h.submit('Jane Doe','jane@example.com'); await sleep(30);
    const rid2=JSON.parse(h.calls.fetch[1].opts.body).request_id;
    ok(rid1===rid2, 'retry after ambiguous -> SAME request_id (same logical request, same session)');
    ok(h.calls.accepted.length===1, 'retry success -> accepted event'); }
}

await runFor('request-appointment', 'request-appointment.html', 'appt',    {name:'aname', contact:'acontact', msg:'amsg'});
await runFor('contact',             'contact.html',             'contact', {name:'wname', contact:'wphone',   msg:'wmsg'});

console.log('\n'+(PASS ? 'ALL '+N+' INTAKE TESTS PASS' : 'INTAKE TEST FAILURES ABOVE'));
process.exit(PASS?0:1);
