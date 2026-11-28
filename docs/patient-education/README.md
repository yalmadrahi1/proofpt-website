# Proof patient-education handouts (DRAFT — pending clinician review)

Created 2026-11-28. These are Proof-branded patient-education **print handouts** modeled on SMC's system
(see `docs/clinical-content-system-playbook.md`), re-centered for a pure PT practice: active care + same-scale
measurement, not injections/procedures.

**Status: DRAFT. Not live on the website.** Each handout is clinical content and must be reviewed and dated-signed
by Zubair Fayyaz, PT, DPT and/or Justin Jwad, DC before any patient use — exactly like the website's reviewed-by
workflow. They are intentionally **not** published as web pages (that would duplicate existing condition/guide
pages). Intended use after sign-off: (1) print in-clinic handouts, and (2) a "Download the home-exercise sheet /
recovery card" link on the matching condition/guide page (a download link is non-clinical once the asset is reviewed).

## Generate
`python3 gen.py` → writes print-ready HTML to `./out/` (override dir with `PROOF_EDU_OUT`). Open in a browser and
print to a letter PDF. Brand + layout match the Proof site (Bricolage Grotesque + Hanken Grotesk; navy/blue palette).

## Drafts in this batch (for review)
| Code | Topic | Type | Suggested reviewer | Key sources |
|---|---|---|---|---|
| P01 | Low back pain — gentle movement helps | Education card | Justin / Zubair | ACP 2017; JOSPT LBP CPG 2021; NICE NG59 |
| P02 | Neck/back pain after a crash (whiplash) | Education card | Justin | Spine 2007;32:618; JOSPT neck CPG 2017; Mayo (pro) |
| P04 | Pain down the leg (sciatica) | Education card | Justin / Zubair | Am Fam Physician 2008;78:835; JOSPT LBP+leg 2021; ACP 2017 |
| H01 | Low back pain — try at home (HEP) | Home-exercise pamphlet | Justin / Zubair | ACP 2017; JOSPT LBP CPG 2021 |

## Reviewer checklist (per handout)
- Clinical accuracy of the "plan," red flags, and dosage against current PT practice.
- Scope: no overclaiming; "educational only / your therapist's plan comes first" retained.
- Red flags complete and correctly escalated (same-day call vs ER/911).
- Sources current and correctly attributed.
- On sign-off: record reviewer + date here, then the download link can be wired to the matching page via the PR gate.

## Approved (reviewer · date)
_(none yet — awaiting Zubair / Justin)_

## Backlog (next batch, on format approval)
Warning-signs/red-flags card · sleep & pain · after a work injury (return-to-work) · knee OA (card + HEP) · neck/whiplash HEP ·
"How we measure your recovery" (this one may suit a web page rather than a handout).
