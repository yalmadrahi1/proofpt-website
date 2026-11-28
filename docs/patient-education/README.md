# Proof patient-education handouts (DRAFT — pending clinician review)

Created 2026-11-28. These are Proof-branded patient-education **print handouts** modeled on SMC's system
(see `docs/clinical-content-system-playbook.md`), re-centered for a pure PT practice: active care + same-scale
measurement, not injections/procedures.

**Status (2026-11-28): direction approved; 3 cards reviewed, 7 drafts pending.** Zubair Fayyaz, PT, DPT and
Justin Jwad, DC approved the patient-education *direction* on Fri 2026-11-27. Justin then reviewed his three cards
(P01, P02, P04) on 2026-11-28 — those carry his dated byline. The remaining seven (P05–P07, H01–H04) are DRAFT pending
each reviewer of record's sign-off on the exact wording, dosages, and red flags before any patient use. A review date
is never back-dated to before the file existed.

Each handout is clinical content and must be reviewed and dated-signed by its reviewer of record before any patient
use — exactly like the website's reviewed-by workflow. They are intentionally **not** published as web pages (that would duplicate existing condition/guide
pages). Intended use after sign-off: (1) print in-clinic handouts, and (2) a "Download the home-exercise sheet /
recovery card" link on the matching condition/guide page (a download link is non-clinical once the asset is reviewed).

## Generate
`python3 gen.py` → writes print-ready HTML to `./out/` (override dir with `PROOF_EDU_OUT`). Open in a browser and
print to a letter PDF. Brand + layout match the Proof site (Bricolage Grotesque + Hanken Grotesk; navy/blue palette).

## Drafts in this batch (for review)
Reviewer of record: cards → Justin Jwad, DC (except work-injury → Zubair, per the website scope mapping); home-exercise
pamphlets → Zubair Fayyaz, PT, DPT. A reviewed card shows a green "Reviewed by … · date" stamp; drafts show the DRAFT stamp.

| Code | Topic | Type | Reviewer of record | Final reviewed? | Key sources |
|---|---|---|---|---|---|
| P01 | Low back pain — gentle movement helps | Education card | Justin Jwad, DC | ✅ 2026-11-28 | ACP 2017; JOSPT LBP CPG 2021; NICE NG59 |
| P02 | Neck/back pain after a crash (whiplash) | Education card | Justin Jwad, DC | ✅ 2026-11-28 | Spine 2007;32:618; JOSPT neck CPG 2017; Mayo (pro) |
| P04 | Pain down the leg (sciatica) | Education card | Justin Jwad, DC | ✅ 2026-11-28 | Am Fam Physician 2008;78:835; JOSPT LBP+leg 2021; ACP 2017 |
| P05 | After a work injury — return to work | Education card | Zubair Fayyaz, PT, DPT | ☐ pending | ACOEM; work-conditioning literature; MI WDCA |
| P06 | Knee arthritis — strong muscles take load off | Education card | Justin Jwad, DC | ☐ pending | ACR/AF OA 2019; OARSI; Messier 2005 |
| P07 | Sleep & pain | Education card | Justin Jwad, DC | ☐ pending | J Clin Med 2021;10:3836; Sleep Med Rev 2022 |
| H01 | Low back pain — try at home (HEP) | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ☐ pending | ACP 2017; JOSPT LBP CPG 2021 |
| H02 | Leg nerve pain (sciatica) — try at home | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ☐ pending | Am Fam Physician 2008; JOSPT LBP+leg 2021 |
| H03 | Neck pain & whiplash — try at home | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ☐ pending | JOSPT neck CPG 2017; Spine 2007;32:618 |
| H04 | Knee arthritis — try at home | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ☐ pending | ACR/AF OA 2019; Messier 2005 |

## Reviewer checklist (per handout)
- Clinical accuracy of the "plan," red flags, and dosage against current PT practice.
- Scope: no overclaiming; "educational only / your therapist's plan comes first" retained.
- Red flags complete and correctly escalated (same-day call vs ER/911).
- Sources current and correctly attributed.
- On sign-off: record reviewer + date here, then the download link can be wired to the matching page via the PR gate.

## Approvals
- **2026-11-27 (Fri):** Direction/approach approved by Zubair Fayyaz, PT, DPT and Justin Jwad, DC (relayed by Yousef).
  Concept approval, not of specific finals.
- **2026-11-28:** **P01, P02, P04 — Reviewed by Justin Jwad, DC** (relayed by Yousef; Justin reviewed these exact
  finals the day they were produced). Byline stamped on those three cards.
- **Pending final sign-off:** Zubair — H01–H04 and P05 (work injury); Justin — P06 (knee), P07 (sleep). On each
  reviewer's OK of the exact PDF, record it here with the real date, regenerate (stamps the byline), then wire the
  download link to the matching page via the PR gate.

## Backlog (next)
Warning-signs / red-flags card (needs its own two-urgent-column layout) · shoulder pain (card + HEP) · hip pain ·
post-surgical return-to-activity · "How we measure your recovery" (likely a web page, not a handout).
Once reviewed handouts accumulate, wire "Download" links on the matching condition/guide pages via the PR gate.
