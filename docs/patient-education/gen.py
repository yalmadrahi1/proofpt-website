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
.rev{{position:absolute;top:0.4in;right:0.66in;font-size:10px;letter-spacing:.02em;color:#13624A;background:#DEF2EA;border-radius:999px;padding:4px 11px;font-weight:700}}
.eyebrow{{display:flex;align-items:center;gap:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);font-size:12.5px;margin:0 0 9px}}
.eyebrow::before{{content:"";width:26px;height:3px;border-radius:2px;background:var(--blue)}}
h1{{font-family:"Bricolage Grotesque",serif;font-weight:800;color:var(--navy);font-size:42px;line-height:1.03;margin:0 0 12px;letter-spacing:-.01em}}
.lead{{font-size:17.5px;line-height:1.48;color:#2B3758;max-width:54ch;margin:0 0 22px}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:18px}}
.col{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px}}
.col h2{{display:flex;align-items:center;gap:10px;font-size:19px;color:var(--navy);margin:0 0 12px;font-family:"Bricolage Grotesque",serif;font-weight:700}}
.badge{{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:0 0 auto}}
.badge svg{{width:16px;height:16px}}.b-ok{{background:var(--blue)}}.b-warn{{background:#F3E2C4}}.b-er{{background:var(--red)}}
.col.er li::before{{background:var(--red)}}
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
BANGW='<svg viewBox="0 0 24 24" fill="none"><path d="M12 8v5" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><circle cx="12" cy="16.5" r="1.4" fill="#fff"/></svg>'

def li(items): return "".join(f"<li>{x}</li>" for x in items)

def stamp_and_src(c):
    if c.get("reviewed_by"):
        stamp = f'<div class="rev">✓ Reviewed by {c["reviewed_by"]} · {c["reviewed_date"]}</div>'
        srcsuf = f'Reviewed by {c["reviewed_by"]} — {c["reviewed_date"]}.'
    else:
        stamp = f'<div class="draft">DRAFT · {c["code"]} · for clinical review (Z.F. / J.J.)</div>'
        srcsuf = 'Draft for clinician review before any patient use.'
    return stamp, srcsuf

def card(c):
    note = f'<div class="note">{c["note"]}</div>' if c.get("note") else ""
    red = f'<div class="redline"><b>{c["redflag_lead"]}</b> {c["redflag"]}</div>' if c.get("redflag") else ""
    stamp, srcsuf = stamp_and_src(c)
    if c.get("urgent"):
        colsblock = (f'<div class="cols">'
          f'<div class="col er"><h2><span class="badge b-er">{BANGW}</span>{c["er_title"]}</h2><ul>{li(c["er"])}</ul></div>'
          f'<div class="col warn"><h2><span class="badge b-warn">{BANG}</span>{c["sameday_title"]}</h2><ul>{li(c["sameday"])}</ul></div>'
          f'</div>{note}')
    else:
        colsblock = (f'<div class="cols">'
          f'<div class="col"><h2><span class="badge b-ok">{CHECK}</span>{c["plan_title"]}</h2><ul>{li(c["plan"])}</ul></div>'
          f'<div class="col warn"><h2><span class="badge b-warn">{BANG}</span>{c["warn_title"]}</h2><ul>{li(c["warn"])}</ul>{red}</div>'
          f'</div>{note}')
    htmlout = HEAD.format(title="Proof Education Card") + f"""
<div class="sheet">{stamp}
<p class="eyebrow">{c['eyebrow']}</p><h1>{c['h1']}</h1><p class="lead">{c['lead']}</p>
{colsblock}
<div class="callout"><div class="big">{c['big']}</div><p>{c['callout']}</p></div>
<div class="foot"><div class="brand">Proof Physical Therapy<small>Recovery, proven.</small></div>
<div class="disc">Educational only, not medical advice. Your therapist's plan comes first.<br>Sterling Heights, MI · (586) 800-8488</div></div>
<div class="src">Sources: {c['sources']} · {srcsuf}</div></div>""" + FOOT
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
    stamp, srcsuf = stamp_and_src(h)
    htmlout = HEAD.format(title="Proof Home Exercise Program") + f"""
<div class="sheet hep">{stamp}
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
<div class="src">Sources: {h['sources']} · {srcsuf}</div></div>""" + FOOT
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
 {"code":"P05","slug":"work-injury","eyebrow":"After a work injury","h1":"Getting back to work is part of your recovery.",
  "lead":"For most work injuries, a safe, gradual return to activity — including modified duty where appropriate — rebuilds function better than waiting until you are pain-free. Your plan is built around what your job actually requires.",
  "plan_title":"Your plan at Proof","plan":["Graded exercise that rebuilds the strength your job needs","Modified or transitional duty where appropriate","Objective testing of range, strength and function","Clear, measured updates to you, your employer and your doctor",SAME_SCORE_PLAN],
  "warn_title":"Tell us or your doctor if","warn":["New or spreading numbness, tingling or weakness","Pain that is not improving after a few weeks","A task at work keeps setting you back"],
  "redflag_lead":"Go to the ER or call 911","redflag":"for chest pain, severe shortness of breath, or loss of bladder or bowel control.",
  "note":"<b>Michigan workers' compensation:</b> bring your claim details — we coordinate objective findings and work status with your employer and treating doctor.",
  "big":"Function","callout":"We measure what your job requires and re-test it, so return-to-work decisions are based on numbers, not guesswork.",
  "sources":"ACOEM occupational musculoskeletal practice guidelines · Work conditioning / functional restoration literature · Michigan Workers' Disability Compensation Agency (provider-choice rules)"},
 {"code":"P06","slug":"knee-arthritis","eyebrow":"Knee arthritis","h1":"Strong muscles take load off an arthritic knee.",
  "lead":"Exercise is one of the most effective treatments for knee osteoarthritis. Strong thigh and hip muscles take load off the joint, and staying active usually helps more than resting it.",
  "plan_title":"Your plan at Proof","plan":["Strengthening for the thigh and hip muscles","Low-impact activity — walking, cycling or swimming","Hands-on therapy and movement to ease stiffness","Guidance on load, footwear and pacing",SAME_SCORE_PLAN],
  "warn_title":"Call us the same day if","warn":["A hot, red, swollen knee, or fever","The knee locks or gives way","Sudden severe pain, or you cannot bear weight"],
  "redflag_lead":None,"redflag":None,
  "note":"<b>Losing even a little weight takes load off the knee with every step.</b> Supportive, cushioned shoes help too.",
  "big":"6–8 wks","callout":"Most people notice less pain and easier walking after 6 to 8 weeks of regular exercise. We track it so you can see the change.",
  "sources":"ACR/Arthritis Foundation osteoarthritis guideline, 2019 · OARSI guidelines · Messier et al., Arthritis Rheum 2005;52:2026"},
 {"code":"P07","slug":"sleep-and-pain","eyebrow":"Sleep & pain","h1":"Poor sleep turns up the volume on pain.",
  "lead":"Pain and sleep feed each other. People with back and neck pain who sleep poorly tend to hurt more, and better sleep goes along with better recovery.",
  "plan_title":"Try tonight","plan":["Same bedtime and wake-up time every day","A dark, cool, quiet room","Screens off an hour before bed","A pillow that keeps your neck level","A walk or gentle movement earlier in the day"],
  "warn_title":"Avoid","warn":["Caffeine after noon","Alcohol to fall asleep","Naps longer than 30 minutes","Lying awake in bed — get up for 20 minutes, then try again"],
  "redflag_lead":None,"redflag":None,
  "note":"<b>Loud snoring, stopping breathing at night, or poor sleep most nights can be treated.</b> Mention it at your next visit.",
  "big":"Tell us","callout":"Better sleep supports recovery. Tell us how you are sleeping — it shapes your plan.",
  "sources":"Sleep and chronic spinal pain, J Clin Med 2021;10:3836 (systematic review) · Sleep deprivation and pain, Sleep Med Rev 2022;66:101695"},
 {"code":"P03","slug":"warning-signs","eyebrow":"Warning signs","h1":"Some symptoms can’t wait.",
  "lead":"These are uncommon, but they need care right away. Keep this card where you can see it.","urgent":True,
  "er_title":"Go to the ER or call 911","er":["Losing control of your bladder or bowels, or you can’t pee","Numbness in the groin or inner thighs","Sudden or fast-worsening leg or arm weakness","Chest pain, or trouble breathing","Severe pain right after a fall or crash"],
  "sameday_title":"Call us the same day","sameday":["New numbness or tingling that is spreading","Pain that wakes you every night","A hot, swollen joint, or a fever with pain","Clumsy hands or trouble with balance"],
  "note":None,"big":"911","callout":"If you are not sure, get care now. Tell the ER you are a Proof patient, and call us afterward.",
  "sources":"Low back pain red flags, NICE NG59 · JOSPT clinical practice guidelines, red-flag screening"},
 {"code":"P08","slug":"shoulder-pain","eyebrow":"Shoulder pain","h1":"Most shoulder pain improves with the right loading.",
  "lead":"Most shoulder pain — from the rotator cuff, tendons, or stiffness — improves with graded exercise and movement. Rest alone usually makes a stiff shoulder worse.",
  "plan_title":"Your plan at Proof","plan":["Graded rotator-cuff and shoulder-blade strengthening","Movement to keep the shoulder from stiffening","Hands-on therapy for mobility and pain","Activity changes while it settles",SAME_SCORE_PLAN],
  "warn_title":"Call us the same day if","warn":["You can’t lift or use the arm after an injury","Sudden weakness, numbness or tingling down the arm","A hot, swollen or deformed shoulder, or fever"],
  "redflag_lead":None,"redflag":None,
  "note":"Most shoulder pain improves over weeks to a few months with a steady, progressive program.",
  "big":"Load it","callout":"Shoulders respond to the right amount of load, re-tested over time — not to rest. We measure your range and strength so progress is visible.",
  "sources":"JOSPT shoulder pain / rotator cuff clinical practice guidelines · Cochrane review, exercise for rotator cuff disease"},
 {"code":"P09","slug":"hip-pain","eyebrow":"Hip pain","h1":"Strong hips move better and hurt less.",
  "lead":"Most hip pain — from the joint, tendons, or surrounding muscles — improves with strengthening and movement. Staying active within comfort usually helps more than resting.",
  "plan_title":"Your plan at Proof","plan":["Strengthening for the hip and core muscles","Low-impact activity — walking, cycling or swimming","Hands-on therapy and movement to ease stiffness","Guidance on load, stairs and pacing",SAME_SCORE_PLAN],
  "warn_title":"Call us the same day if","warn":["You can’t bear weight after a fall or injury","A hot, swollen hip, or fever","Sudden numbness, tingling or weakness in the leg"],
  "redflag_lead":None,"redflag":None,
  "note":"Most hip pain improves over weeks with a steady, progressive program.",
  "big":"Weeks","callout":"Most hip pain eases over weeks with strengthening. We re-test so you and your therapist can see it working.",
  "sources":"JOSPT hip pain clinical practice guidelines · ACR/Arthritis Foundation osteoarthritis guideline, 2019"},
 {"code":"P10","slug":"after-surgery","eyebrow":"After surgery","h1":"Recovery after surgery follows your surgeon’s plan.",
  "lead":"After orthopedic surgery, the safest recovery follows the protocol your surgeon sets — the right movements at the right time. We work within that protocol to rebuild your strength and function.",
  "plan_title":"Your plan at Proof","plan":["A plan matched to your surgeon’s protocol and timeline","Protecting the repair while you regain motion","Graded strengthening as you are cleared for it","Getting back to daily activities step by step",SAME_SCORE_PLAN],
  "warn_title":"Call us or your surgeon the same day if","warn":["Increasing redness, warmth, swelling or drainage at the incision","Fever, or a calf that is red, swollen or painful","A sudden increase in pain, or a ‘pop’ with new weakness"],
  "redflag_lead":"Go to the ER or call 911","redflag":"for chest pain, trouble breathing, or a sudden swollen, painful calf.",
  "note":"<b>Your surgeon’s protocol comes first.</b> We never push past the limits your surgeon has set.",
  "big":"On time","callout":"The right exercise at the right stage protects the repair and speeds recovery. We measure your progress against your plan.",
  "sources":"Procedure-specific post-operative rehabilitation protocols · JOSPT post-operative clinical practice guidelines (by procedure)"},
]
# Clinician sign-offs (relayed by Yousef). Dated the day the finals were produced/reviewed; never back-dated.

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
 {"code":"H02","slug":"sciatica","h1":"Leg nerve pain (sciatica): try at home","lead":"An irritated nerve in the lower back can cause pain down the leg. The goal is movement that calms the nerve, not stretching it hard.",
  "start":[
   {"name":"Positions of relief","steps":["Lie on your back with your calves resting on a chair seat.","Or lie on your stomach with a pillow under your hips if that eases the leg pain."],"dose":"5 to 10 minutes, as needed"},
   {"name":"Press-up (only if it eases the leg)","steps":["Lie on your stomach, hands under your shoulders.","Slowly push your upper body up, keeping your hips down.","Stop if leg pain moves further down the leg."],"dose":"10 times · every 2–3 hours if it helps"},
   {"name":"Nerve glide (slider)","steps":["Sit upright on a chair.","Straighten the sore leg while tipping your head back.","Bend the knee while bringing your chin down. Keep it smooth and gentle."],"dose":"10 slow repeats · 2–3× a day"},
   {"name":"Walking","steps":["Short, frequent walks on flat ground.","Stop and rest before the leg pain builds."],"dose":"5 minutes, several times a day"},
  ],
  "add":[{"name":"Bridge","steps":["Lie on your back, knees bent.","Lift your hips, keeping your back straight.","Lower slowly."],"dose":"Hold 5 seconds · 10 times · once a day"}],
  "every":["Move a little every hour","Sit with your back supported and hips slightly higher than your knees","Ice or heat, whichever feels better, for 15 to 20 minutes"],
  "avoid":["Long periods of sitting","Toe-touching stretches","Heavy lifting or twisting"],
  "stop":["Sharp or rapidly increasing pain","Leg or foot weakness, or your foot dragging","Numbness that spreads","Any change in bladder or bowel control: go to the ER or call 911"],
  "expect":"Many people feel better within 6 weeks and most within 3 months. We check your pain and function on the same score at each visit.",
  "sources":"Lumbar disk herniation, Am Fam Physician 2008 · JOSPT low back pain with leg pain clinical practice guideline (2021 revision)"},
 {"code":"H03","slug":"neck-whiplash","h1":"Neck pain and whiplash: try at home","lead":"Gentle, regular neck movement helps recovery more than resting it or wearing a collar.",
  "start":[
   {"name":"Chin tuck","steps":["Sit or stand tall.","Slide your chin straight back, making a double chin.","Hold, then relax."],"dose":"Hold 5 seconds · 10 times · 3× a day"},
   {"name":"Turning side to side","steps":["Sit tall.","Slowly turn your head to look over one shoulder, then the other.","Go only as far as is comfortable."],"dose":"10 each way · 3× a day"},
   {"name":"Shoulder blade squeeze","steps":["Sit tall, arms relaxed.","Squeeze your shoulder blades back and down.","Hold, then relax."],"dose":"Hold 5 seconds · 10 times · 3× a day"},
   {"name":"Upper shoulder stretch","steps":["Sit tall and hold the chair seat with one hand.","Tilt your ear toward the other shoulder until you feel a gentle stretch."],"dose":"Hold 20 seconds · 3 each side · 2× a day"},
  ],
  "add":[{"name":"Arms-up wall slide","steps":["Stand with your back to a wall, arms bent like a goalpost.","Slide your arms up the wall and back down slowly."],"dose":"10 times · once a day"}],
  "every":["Take a posture break every 30 minutes at screens or driving","Keep your phone at eye level","Use a pillow that keeps your neck level with your body","Heat for 15 to 20 minutes for stiffness"],
  "avoid":["A soft collar unless your provider told you to wear one","Long periods looking down","Sleeping on your stomach"],
  "stop":["Sharp or rapidly increasing pain","Numbness, tingling or weakness down an arm","New weakness, or clumsy hands","Bad headache, confusion or vomiting after a crash: go to the ER"],
  "expect":"Most neck pain and whiplash improves over weeks, and most people recover within about 3 months.",
  "sources":"JOSPT neck pain clinical practice guideline (2017 revision) · Whiplash: activity vs collar, Spine 2007;32:618"},
 {"code":"H04","slug":"knee-arthritis","h1":"Knee arthritis: try at home","lead":"Strong thigh and hip muscles take load off the knee. Exercise is one of the most effective treatments for knee arthritis.",
  "start":[
   {"name":"Thigh tightening (quad set)","steps":["Sit with your leg straight and a rolled towel under the knee.","Press the back of your knee down into the towel.","Hold, then relax."],"dose":"Hold 5 seconds · 10 times · 2× a day"},
   {"name":"Straight leg raise","steps":["Lie on your back, other knee bent.","Tighten your thigh and lift the straight leg to the height of the other knee.","Lower slowly."],"dose":"10 times · 2 sets · once a day"},
   {"name":"Heel slide","steps":["Lie on your back.","Slide your heel toward your buttock, bending the knee.","Slide back."],"dose":"10 times · 2× a day"},
   {"name":"Sit to stand","steps":["Sit on a firm chair.","Stand up without using your hands if you can.","Sit back down slowly."],"dose":"10 times · once a day"},
  ],
  "add":[{"name":"Step-up","steps":["Hold a rail.","Step up onto a low step with the sore leg, then step down slowly."],"dose":"10 times · once a day"}],
  "every":["Walk, cycle or swim most days","Wear supportive, cushioned shoes","Losing even a little weight takes load off your knees with every step"],
  "avoid":["Deep squats and kneeling for long periods","Running on hard surfaces while it is flaring","Complete rest"],
  "stop":["Sharp or rapidly increasing pain","A hot, red, swollen knee, or fever","The knee locking or giving way","Sudden inability to bear weight"],
  "expect":"Most people notice less pain and easier walking after 6 to 8 weeks of regular exercise.",
  "sources":"ACR/Arthritis Foundation osteoarthritis guideline, 2019 · Messier et al., Arthritis Rheum 2005"},
 {"code":"H05","slug":"shoulder","h1":"Shoulder pain: try at home","lead":"Gentle movement and light strengthening help most shoulder pain. Keep within a comfortable range.",
  "start":[
   {"name":"Pendulum","steps":["Lean forward with your good hand resting on a table.","Let the sore arm hang and gently swing it in small circles."],"dose":"1 minute each direction · 2–3× a day"},
   {"name":"Shoulder blade squeeze","steps":["Sit tall, arms relaxed.","Squeeze your shoulder blades back and down.","Hold, then relax."],"dose":"Hold 5 seconds · 10 times · 3× a day"},
   {"name":"Wall walk","steps":["Face a wall, fingers resting on it.","Walk your fingers up the wall as far as is comfortable, then back down."],"dose":"5 times · 2× a day"},
   {"name":"External rotation (with a towel)","steps":["Hold a rolled towel under your elbow against your side.","Keeping the elbow in, rotate your forearm outward.","Return slowly."],"dose":"10 times · 2 sets · once a day"},
  ],
  "add":[{"name":"Band row","steps":["Anchor a light band at waist height.","Pull your elbow back, squeezing the shoulder blade.","Return slowly."],"dose":"10 times · 2 sets · once a day"}],
  "every":["Move the shoulder a little often","Keep good posture at screens and driving","Heat for 10–15 minutes before exercises for stiffness"],
  "avoid":["Overhead lifting while it is painful","Sleeping directly on the sore shoulder","Complete rest for more than a day or two"],
  "stop":["Sharp or rapidly increasing pain","Numbness, tingling or weakness down the arm","A hot, swollen shoulder or fever","Inability to lift or use the arm after an injury"],
  "expect":"Most shoulder pain eases over weeks to a few months. We re-test your range and strength on the same scale at each visit.",
  "sources":"JOSPT shoulder pain / rotator cuff clinical practice guidelines"},
 {"code":"H06","slug":"hip","h1":"Hip pain: try at home","lead":"Strengthening the hip and core muscles takes load off the joint. Keep within a comfortable range.",
  "start":[
   {"name":"Glute bridge","steps":["Lie on your back, knees bent.","Squeeze your buttocks and lift your hips until your body is straight.","Lower slowly."],"dose":"10 times · 2 sets · once a day"},
   {"name":"Clamshell","steps":["Lie on your side, knees bent and stacked.","Keeping your feet together, lift the top knee.","Lower slowly."],"dose":"10 each side · 2 sets · once a day"},
   {"name":"Standing hip abduction","steps":["Hold a counter for balance.","Lift one leg out to the side, keeping it straight.","Lower slowly."],"dose":"10 each side · 2× a day"},
   {"name":"Sit to stand","steps":["Sit on a firm chair.","Stand up without using your hands if you can.","Sit back down slowly."],"dose":"10 times · once a day"},
  ],
  "add":[{"name":"Step-up","steps":["Hold a rail.","Step up onto a low step, then step down slowly."],"dose":"10 each leg · once a day"}],
  "every":["Walk, cycle or swim most days","Change position often; avoid long sitting","Wear supportive, cushioned shoes"],
  "avoid":["Deep squats while it is flaring","Crossing your legs for long periods","Complete rest"],
  "stop":["Sharp or rapidly increasing pain","A hot, swollen hip or fever","Numbness, tingling or weakness in the leg","Inability to bear weight after a fall"],
  "expect":"Most hip pain eases over weeks with a steady program. We re-test on the same scale at each visit.",
  "sources":"JOSPT hip pain clinical practice guidelines · ACR/Arthritis Foundation osteoarthritis guideline, 2019"},
]

# Reviewer of record per asset, all reviewed 2026-11-28 (relayed by Yousef). Dated the day the finals were produced.
REVIEWED={
 "P01":"Justin Jwad, DC","P02":"Justin Jwad, DC","P04":"Justin Jwad, DC",
 "P06":"Justin Jwad, DC","P07":"Justin Jwad, DC",
 "P05":"Zubair Fayyaz, PT, DPT",
 "H01":"Zubair Fayyaz, PT, DPT","H02":"Zubair Fayyaz, PT, DPT",
 "H03":"Zubair Fayyaz, PT, DPT","H04":"Zubair Fayyaz, PT, DPT",
}
for _a in CARDS+HEPS:
    if _a["code"] in REVIEWED:
        _a["reviewed_by"]=REVIEWED[_a["code"]]; _a["reviewed_date"]="November 28, 2026"

made=[]
for c in CARDS: made.append(card(c))
for h in HEPS: made.append(hep(h))
print("generated:", len(made))
for m in made: print(" ", m)
