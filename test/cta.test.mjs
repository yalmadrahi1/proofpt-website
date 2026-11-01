/* CTA + availability-status regression guard — run: `npm test`
   Scans the built HTML (the shared layer that produced the defect) and fails if
   contradictory "bookable now" status or an appointment CTA mis-routed to
   contact.html reappears. This is the check for the shared generation logic that
   caused the Nov-1 routing defect. Pure string scan, no deps. */
import fs from 'fs';
import path from 'path';
import {fileURLToPath} from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
let pass = 0, fail = 0;
function ok(c, m){ if(c){pass++; console.log('  ok  : '+m);} else {fail++; console.log('  FAIL: '+m);} }

function walk(dir){
  const out = [];
  for(const e of fs.readdirSync(dir, {withFileTypes:true})){
    if(e.name === 'node_modules' || e.name === 'test' || e.name.startsWith('.')) continue;
    const p = path.join(dir, e.name);
    if(e.isDirectory()) out.push(...walk(p));
    else if(e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

const files = walk(ROOT);
const read = f => fs.readFileSync(f,'utf8');
const rel = f => path.relative(ROOT, f);

// 1) No "bookable now" status anywhere — before scheduling actually opens, nothing is bookable.
const bookable = files.filter(f => /bookable now/i.test(read(f))).map(rel);
ok(bookable.length === 0, 'no page claims "bookable now"' + (bookable.length?' — offenders: '+bookable.join(', '):''));

// 2) No appointment CTA routed to contact.html (patient appt actions go to request-appointment.html).
const misrouted = files.filter(f => /contact\.html(\?[^"]*)?">\s*Request an appointment/i.test(read(f))).map(rel);
ok(misrouted.length === 0, 'no "Request an appointment" CTA points at contact.html' + (misrouted.length?' — offenders: '+misrouted.join(', '):''));

// 3) Every condition page carries a request-appointment.html CTA (routing present, not dropped).
const conditions = files.filter(f => rel(f).startsWith('conditions/') && path.basename(f) !== 'index.html');
const missing = conditions.filter(f => !/request-appointment\.html/.test(read(f))).map(rel);
ok(conditions.length > 0 && missing.length === 0,
   conditions.length+' condition pages route appointments to request-appointment.html' + (missing.length?' — missing: '+missing.join(', '):''));

// 4) June services stay future-facing (honest, not bookable).
for(const svc of ['services/occupational-therapy.html','services/spinal-decompression.html']){
  const h = read(path.join(ROOT, svc));
  ok(/(not bookable yet|nothing is bookable)/i.test(h) && /Ask about June 2027 availability/i.test(h),
     svc+' stays future-facing (not bookable) + an availability-inquiry route');
}

console.log('\n'+(fail===0?'ALL '+pass+' CTA/STATUS TESTS PASS':fail+' CTA/STATUS TEST(S) FAILED'));
process.exit(fail===0?0:1);
