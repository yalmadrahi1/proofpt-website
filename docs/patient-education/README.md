# Proof patient-education handouts (DRAFT — pending clinician review)

Created 2026-11-28. These are Proof-branded patient-education **print handouts** modeled on SMC's system
(see `docs/clinical-content-system-playbook.md`), re-centered for a pure PT practice: active care + same-scale
measurement, not injections/procedures.

**Status (2026-11-28): direction approved; these exact finals NOT yet reviewed.** Zubair Fayyaz, PT, DPT and
Justin Jwad, DC approved the patient-education *direction/approach* on Fri 2026-11-27 (relayed by Yousef). They have
**not** yet reviewed these specific handout PDFs — which were generated 2026-11-28 — so no dated "Reviewed by" byline
is applied yet. Each reviewer of record must sign off on the exact wording, dosages, and red flags of their handout(s)
before the byline goes on and before any patient use. A review date is never back-dated to before the file existed.

Each handout is clinical content and must be reviewed and dated-signed by its reviewer of record before any patient
use — exactly like the website's reviewed-by workflow. They are intentionally **not** published as web pages (that would duplicate existing condition/guide
pages). Intended use after sign-off: (1) print in-clinic handouts, and (2) a "Download the home-exercise sheet /
recovery card" link on the matching condition/guide page (a download link is non-clinical once the asset is reviewed).

## Generate
`python3 gen.py` → writes print-ready HTML to `./out/` (override dir with `PROOF_EDU_OUT`). Open in a browser and
print to a letter PDF. Brand + layout match the Proof site (Bricolage Grotesque + Hanken Grotesk; navy/blue palette).

## Drafts in this batch (for review)
Reviewer of record assigned by Yousef 2026-11-28: Justin on the three cards, Zubair on the home-exercise pamphlet.

| Code | Topic | Type | Reviewer of record | Final reviewed? | Key sources |
|---|---|---|---|---|---|
| P01 | Low back pain — gentle movement helps | Education card | Justin Jwad, DC | ☐ pending | ACP 2017; JOSPT LBP CPG 2021; NICE NG59 |
| P02 | Neck/back pain after a crash (whiplash) | Education card | Justin Jwad, DC | ☐ pending | Spine 2007;32:618; JOSPT neck CPG 2017; Mayo (pro) |
| P04 | Pain down the leg (sciatica) | Education card | Justin Jwad, DC | ☐ pending | Am Fam Physician 2008;78:835; JOSPT LBP+leg 2021; ACP 2017 |
| H01 | Low back pain — try at home (HEP) | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ☐ pending | ACP 2017; JOSPT LBP CPG 2021 |

## Reviewer checklist (per handout)
- Clinical accuracy of the "plan," red flags, and dosage against current PT practice.
- Scope: no overclaiming; "educational only / your therapist's plan comes first" retained.
- Red flags complete and correctly escalated (same-day call vs ER/911).
- Sources current and correctly attributed.
- On sign-off: record reviewer + date here, then the download link can be wired to the matching page via the PR gate.

## Approvals
- **2026-11-27 (Fri):** Direction/approach approved by Zubair Fayyaz, PT, DPT and Justin Jwad, DC (relayed by Yousef).
  This is approval of the concept, not of these specific finals.
- **Per-handout final sign-off:** _(none yet)_ — awaiting each reviewer of record's review of the exact PDF. On
  sign-off, record here as "P0X — Reviewed by <name> — <date>" using the real review date, then stamp the byline and
  wire the download link via the PR gate.

## Backlog (next batch, on format approval)
Warning-signs/red-flags card · sleep & pain · after a work injury (return-to-work) · knee OA (card + HEP) · neck/whiplash HEP ·
"How we measure your recovery" (this one may suit a web page rather than a handout).
