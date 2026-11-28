#!/usr/bin/env python3
# Proof patient-education asset generator — consistent brand system, scalable.
# Produces print-ready HTML (cards + try-at-home HEP pamphlets). All DRAFT, for clinician review.
import os, html
OUT = os.environ.get("PROOF_EDU_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"))
os.makedirs(OUT, exist_ok=True)

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@700;800&family=Hanken+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{{--navy:#0C2457;--blue:#1948E3;--blue-deep:#1238B5;--ice:#F4F7FE;--sky:#E6EDFD;--line:#DDE5F3;--mut:#4E5F82;--ink:#1A2340;--amber:#E79A2B;--red:#C0392B;--paper:#FBFAF6;--green:#1E8E6A}}
*{{box-sizing:border-box}}html,body{{margin:0;background:#E7EAF1;color:var(--ink);font-family:"Hanken Grotesk",system-ui,sans-serif}}
.sheet{{width:8.5in;margin:22px auto;background:var(--paper);padding:0.66in 0.66in 0.52in;position:relative;box-shadow:0 10px 40px -18px rgba(12,36,87,.4)}}
.draft{{position:absolute;top:0.4in;right:0.66in;font-size:10px;letter-spacing:.03em;color:#9A7B37;background:#FBEFD6;border-radius:999px;padding:4px 11px;font-weight:700}}
.eyebrow{{display:flex;align-items:center;gap:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);font-size:12.5px;margin:0 0 9px}}
.eyebrow::before{{content:"";width:26px;height:3px;border-radius:2px;background:var(--blue)}}
h1{{font-family:"Bricolage Grotesque",serif;font-weight:800;color:var(--navy);font-size:42px;line-height:1.03;margin:0 0 12px;letter-spacing:-.01em}}
.lead{{font-size:17.5px;line-height:1.48;color:#2B3758;max-width:54ch;margin:0 0 22px}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:18px}}
.col{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px}}
.col h2{{display:flex;align-items:center;gap:10px;font-size:19px;color:var(--navy);margin:0 0 12px;font-family:"Bricolage Grotesque",serif;font-weight:700}}
.badge{{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:0 0 auto}}
.badge svg{{width:16px;height:16px}}.b-ok{{background:var(--blue)}}.b-warn{{background:#F3E2C4}}
ul{{margin:0;padding:0;list-style:none}}
li{{position:relative;padding-left:19px;margin-bottom:10px;font-size:15px;line-height:1.4;color:var(--ink)}}
li::before{{content:"";position:absolute;left:0;top:8px;width:7px;height:7px;border-radius:50%;background:var(--blue)}}
.col.warn li::before{{background:var(--amber)}}
.redline{{margin-top:12px;font-size:13px;color:var(--red);line-height:1.4}}
.note{{border-left:4px solid var(--amber);background:#fff;border-radius:0 12px 12px 0;padding:12px 15px;font-size:14px;line-height:1.45;color:#2B3758;margin-bottom:18px}}.note b{{color:var(--navy)}}
.callout{{background:var(--navy);border-radius:18px;padding:20px 24px;display:flex;align-items:center;gap:20px;color:#fff}}
.callout .big{{font-family:"Bricolage Grotesque",serif;font-weight:800;color:var(--amber);font-size:34px;line-height:1;flex:0 0 auto;white-space:nowrap}}
.callout p{{margin:0;font-size:15.5px;line-height:1.45}}
.foot{{margin-top:22px;padding-top:13px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:flex-end;gap:20px}}
.brand{{font-family:"Bricolage Grotesque",serif;font-weight:800;color:var(--navy);font-size:17px}}
.brand small{{display:block;font-family:"Hanken Grotesk";font-weight:600;color:var(--blue);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;margin-top:3px}}
.disc{{text-align:right;font-size:11.5px;color:var(--mut);line-height:1.4;max-width:34ch}}
.src{{margin-top:11px;font-size:10px;color:#8792AC;line-height:1.4}}
/* HEP */
.hep .how{{background:var(--sky);border-radius:12px;padding:13px 16px;font-size:14px;line-height:1.45;color:#2B3758;margin:0 0 18px}}.hep .how b{{color:var(--navy)}}
.seclabel{{font-family:"Bricolage Grotesque",serif;font-weight:700;color:var(--navy);font-size:19px;margin:4px 0 11px;display:flex;align-items:baseline;gap:10px}}
.seclabel span{{font-family:"Hanken Grotesk";font-weight:700;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--blue)}}
.exg{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}}
.ex{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px}}
.ex h3{{display:flex;align-items:center;gap:9px;font-size:15.5px;color:var(--navy);margin:0 0 7px}}
.ex .n{{width:22px;height:22px;border-radius:50%;background:var(--navy);color:var(--amber);font-weight:800;font-size:12px;display:flex;align-items:center;justify-content:center;flex:0 0 auto;font-family:"Bricolage Grotesque",serif}}
.ex ol{{margin:0 0 9px;padding-left:18px;font-size:13.5px;line-height:1.4;color:var(--ink)}}
.ex ol li{{padding-left:4px;margin-bottom:5px}}.ex ol li::before{{display:none}}
.ex .dose{{background:#FBEFD6;border-radius:7px;padding:5px 9px;font-size:12px;color:#7A5A16;font-weight:600;display:inline-block}}
.twobox{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}}
.box{{border-radius:12px;padding:13px 16px;font-size:13.5px;line-height:1.5}}
.box.ev{{background:var(--ice)}}.box.av{{background:#F1F0F4}}
.box h4{{margin:0 0 7px;font-size:13.5px;color:var(--navy)}}.box ul li{{font-size:13.5px;margin-bottom:5px;padding-left:15px}}.box ul li::before{{top:7px;width:5px;height:5px}}
.stop{{background:#FBEAE7;border-left:4px solid var(--red);border-radius:0 12px 12px 0;padding:13px 16px;margin-bottom:16px}}
.stop h4{{margin:0 0 7px;color:var(--red);font-size:14px}}.stop ul li{{font-size:13.5px;margin-bottom:4px;color:#7A2820}}.stop ul li::before{{background:var(--red);top:7px;width:5px;height:5px}}
.expect{{background:var(--navy);color:#fff;border-radius:12px;padding:14px 18px;font-size:14.5px;line-height:1.45;margin-bottom:6px}}.expect b{{color:var(--amber)}}
@media(max-width:720px){{.sheet{{width:auto;padding:26px 18px}}.cols,.exg,.twobox{{grid-template-columns:1fr}}h1{{font-size:31px}}.draft{{position:static;display:inline-block;margin-bottom:8px}}}}
@media print{{html,body{{background:#fff}}.sheet{{box-shadow:none;margin:0;width:auto}}}}
</style></head><body>"""

FOOT = """</body></html>"""
CHECK='<svg viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
BANG='<svg viewBox="0 0 24 24" fill="none"><path d="M12 8v5" stroke="#9A6A12" stroke-width="2.6" stroke-linecap="round"/><circle cx="12" cy="16.5" r="1.4" fill="#9A6A12"/></svg>'

def li(items): return "".join(f"<li>{x}</li>" for x in items)

def card(c):
    note = f'<div class="note">{c["note"]}</div>' if c.get("note") else ""
    red = f'<div class="redline"><b>{c["redflag_lead"]}</b> {c["redflag"]}</div>' if c.get("redflag") else ""
    htmlout = HEAD.format(title="Proof Education Card") + f"""
<div class="sheet"><div class="draft">DRAFT · {c['code']} · for clinical review (Z.F. / J.J.)</div>
<p class="eyebrow">{c['eyebrow']}</p><h1>{c['h1']}</h1><p class="lead">{c['lead']}</p>
<div class="cols">
 <div class="col"><h2><span class="badge b-ok">{CHECK}</span>{c['plan_title']}</h2><ul>{li(c['plan'])}</ul></div>
 <div class="col warn"><h2><span class="badge b-warn">{BANG}</span>{c['warn_title']}</h2><ul>{li(c['warn'])}</ul>{red}</div>
</div>{note}
<div class="callout"><div class="big">{c['big']}</div><p>{c['callout']}</p></div>
<div class="foot"><div class="brand">Proof Physical Therapy<small>Recovery, proven.</small></div>
<div class="disc">Educational only, not medical advice. Your therapist's plan comes first.<br>Sterling Heights, MI · (586) 800-8488</div></div>
<div class="src">Sources: {c['sources']} · Draft for clinician review before any patient use.</div></div>""" + FOOT
    p = os.path.join(OUT, f"card-{c['code'].lower()}-{c['slug']}.html")
    open(p,"w").write(htmlout); return p

def hep(h):
    def exs(lst):
        out=""
        for i,e in enumerate(lst, h.get("_start",1)):
            steps="".join(f"<li>{s}</li>" for s in e["steps"])
            out+=f'<div class="ex"><h3><span class="n">{i}</span>{e["name"]}</h3><ol>{steps}</ol><span class="dose">{e["dose"]}</span></div>'
        return out
    h["_start"]=1; start=exs(h["start"])
    h["_start"]=len(h["start"])+1; add=exs(h["add"])
    htmlout = HEAD.format(title="Proof Home Exercise Program") + f"""
<div class="sheet hep"><div class="draft">DRAFT · {h['code']} · for PT review (Z.F. / J.J.)</div>
<p class="eyebrow">Try at home</p><h1>{h['h1']}</h1><p class="lead">{h['lead']}</p>
<div class="how"><b>How hard?</b> Mild soreness is OK — up to 3 out of 10 during exercise, settling within 24 hours. If pain is higher or lasts into the next day, do fewer reps next time. If your therapist gave you a program, follow theirs instead.</div>
<div class="seclabel">Start now <span>weeks 1–2</span></div><div class="exg">{start}</div>
<div class="seclabel">Add when these feel easy <span>usually week 3+</span></div><div class="exg">{add}</div>
<div class="twobox">
 <div class="box ev"><h4>Every day</h4><ul>{li(h['every'])}</ul></div>
 <div class="box av"><h4>Avoid for now</h4><ul>{li(h['avoid'])}</ul></div>
</div>
<div class="stop"><h4>Stop and call us</h4><ul>{li(h['stop'])}</ul></div>
<div class="expect"><b>What to expect.</b> {h['expect']}</div>
<div class="foot"><div class="brand">Proof Physical Therapy<small>Recovery, proven.</small></div>
<div class="disc">Educational only, not medical advice. Your therapist's plan comes first.<br>Sterling Heights, MI · (586) 800-8488</div></div>
<div class="src">Sources: {h['sources']} · Draft for clinician review before any patient use.</div></div>""" + FOOT
    p=os.path.join(OUT, f"hep-{h['code'].lower()}-{h['slug']}.html")
    open(p,"w").write(htmlout); return p

SAME_SCORE_PLAN = "We re-test your pain and function on the <b>same scale every visit</b>"

CARDS=[
 {"code":"P01","slug":"back-movement","eyebrow":"Back pain","h1":"Gentle movement helps your back recover.",
  "lead":"For most low back pain, staying active within comfort works better than bed rest. Some soreness with movement does not always mean harm, and most new back pain eases over weeks.",
  "plan_title":"Your plan at Proof","plan":["Short walks a few times a day","A home program that builds strength","Hands-on therapy and graded, progressive movement","Heat or ice for 15–20 minutes for comfort",SAME_SCORE_PLAN],
  "warn_title":"Call us the same day if","warn":["New or spreading numbness, tingling or weakness in a leg","Pain that wakes you every night","Back pain with fever or chills"],
  "redflag_lead":"Go to the ER or call 911","redflag":"for loss of bladder or bowel control, or new numbness in the groin.",
  "note":"<b>Most new back pain improves over weeks to months.</b> If you are not improving after 2–4 weeks, tell us — we change the plan rather than repeat it.",
  "big":"Weeks","callout":"Most new back pain improves over weeks to months. Your plan builds strength so it is easier to stay well.",
  "sources":"ACP low back pain guideline, Ann Intern Med 2017 · JOSPT low back pain clinical practice guideline (2021 revision) · NICE NG59 low back pain and sciatica"},
 {"code":"P02","slug":"after-a-crash","eyebrow":"After a car accident","h1":"Neck and back pain after a crash usually improves.",
  "lead":"Whiplash is a soft-tissue injury and often does not show on an X-ray. Most people recover over weeks to months, and gentle, regular movement helps more than resting or wearing a collar.",
  "plan_title":"Your plan at Proof","plan":["Gentle neck and back movement every day","Returning to normal activities step by step","Your therapy plan and home exercises","Heat for stiffness",SAME_SCORE_PLAN],
  "warn_title":"Call us the same day if","warn":["New weakness, or clumsy hands","Numbness or tingling spreading down an arm or leg","Dizziness that does not settle"],
  "redflag_lead":"Go to the ER","redflag":"for a bad headache, confusion or vomiting after a crash, or any loss of bladder or bowel control.",
  "note":"<b>Michigan no-fault (auto injury):</b> bring your claim number, adjuster's name and the crash date — we handle the paperwork with your insurer so you can focus on recovering.",
  "big":"3 months","callout":"Most whiplash recovers within about 3 months. If you are not improving, we change the plan rather than repeat it.",
  "sources":"Whiplash: activity vs collar, Spine 2007;32:618 · JOSPT neck pain clinical practice guideline (2017 revision) · Whiplash-associated disorders, Mayo Clinic (for professionals)"},
 {"code":"P04","slug":"pain-down-the-leg","eyebrow":"Pain down the leg","h1":"Nerve pain usually calms with the right movement.",
  "lead":"Pain, numbness or tingling down the leg from an irritated nerve in the lower back usually improves. Many people feel better within 6 weeks and most within 3 months — and for most, active movement, not rest, is what moves it along.",
  "plan_title":"Your plan at Proof","plan":["A home program you can do between visits","Nerve-friendly movement and regular walking","Hands-on therapy and graded, progressive exercise","Positions that take pressure off the leg",SAME_SCORE_PLAN],
  "warn_title":"Call us the same day if","warn":["Your leg or foot gets weaker","You start tripping or your foot drags","Numbness spreads or gets worse"],
  "redflag_lead":"Go to the ER or call 911","redflag":"for loss of bladder or bowel control, or new numbness in the groin.",
  "note":None,
  "big":"Same&nbsp;score","callout":"We re-check your pain and function on the same scale at every visit, so you and your therapist can see whether the plan is working — and change it if it isn't.",
  "sources":"Lumbar disk herniation, Am Fam Physician 2008;78:835 · JOSPT low back pain with leg pain clinical practice guideline (2021 revision) · ACP low back pain guideline, Ann Intern Med 2017"},
]

HEPS=[
 {"code":"H01","slug":"low-back","h1":"Low back pain: try at home","lead":"Most low back pain eases with movement and time. These gentle exercises keep your back moving while it settles.",
  "start":[
   {"name":"Pelvic tilt","steps":["Lie on your back, knees bent, feet flat.","Tighten your stomach and flatten your low back into the floor.","Hold, then relax."],"dose":"Hold 5 seconds · 10 times · 2× a day"},
   {"name":"Knee to chest","steps":["Lie on your back, knees bent.","Hug one knee toward your chest until you feel a gentle stretch.","Switch sides."],"dose":"Hold 20 seconds · 3 each side · 2× a day"},
   {"name":"Cat and camel","steps":["On hands and knees, slowly round your back up.","Then let it sag gently, lifting your head.","Move only as far as is comfortable."],"dose":"10 slow repeats · 2× a day"},
   {"name":"Walking","steps":["Walk at an easy pace on flat ground.","Add 2 to 5 minutes every few days."],"dose":"5–10 minutes · 2–3× a day to start"},
  ],
  "add":[{"name":"Bridge","steps":["Lie on your back, knees bent.","Squeeze your buttocks and lift your hips until your body is straight.","Lower slowly."],"dose":"Hold 5 seconds · 10 times · once a day"}],
  "every":["Change position every 30 to 45 minutes","Heat for 15 to 20 minutes for stiffness","Sleep on your side with a pillow between your knees, or on your back with a pillow under your knees"],
  "avoid":["Bed rest for more than a day","Lifting heavy objects with a rounded back","Long car rides without breaks"],
  "stop":["Sharp or rapidly increasing pain","Numbness, tingling or weakness spreading down a leg","New weakness, or your knee or foot giving way","Back pain with fever, or after a fall","Loss of bladder or bowel control, or numbness in the groin: go to the ER or call 911"],
  "expect":"Many people feel better within a few weeks. If you are not improving after 2 to 4 weeks, tell us so we can adjust the plan.",
  "sources":"ACP low back pain guideline, Ann Intern Med 2017 · JOSPT low back pain clinical practice guideline (2021 revision)"},
]

made=[]
for c in CARDS: made.append(card(c))
for h in HEPS: made.append(hep(h))
print("generated:", len(made))
for m in made: print(" ", m)
