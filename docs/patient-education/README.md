# Proof patient-education handouts (DRAFT — pending clinician review)

Created 2026-11-28. These are Proof-branded patient-education **print handouts** modeled on SMC's system
(see `docs/clinical-content-system-playbook.md`), re-centered for a pure PT practice: active care + same-scale
measurement, not injections/procedures.

**Status (2026-11-28): 10 reviewed + live as downloads; 6 new drafts pending.** Zubair Fayyaz, PT, DPT and Justin Jwad, DC approved the
direction on Fri 2026-11-27, and reviewed the finals on 2026-11-28 (relayed by Yousef). Each asset carries its
allocated reviewer's dated byline (cards → Justin, except work-injury → Zubair; all home-exercise pamphlets → Zubair).
Dated the day the finals were produced — never back-dated. **Stored durably in this repo via the generator: run
`python3 gen.py` to reproduce all 10 exactly (with their reviewed stamps).** Not published as live web pages. When
Proof opens, these are ready to print and to wire as "Download" links on the matching condition/guide pages.

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
| P05 | After a work injury — return to work | Education card | Zubair Fayyaz, PT, DPT | ✅ 2026-11-28 | ACOEM; work-conditioning literature; MI WDCA |
| P06 | Knee arthritis — strong muscles take load off | Education card | Justin Jwad, DC | ✅ 2026-11-28 | ACR/AF OA 2019; OARSI; Messier 2005 |
| P07 | Sleep & pain | Education card | Justin Jwad, DC | ✅ 2026-11-28 | J Clin Med 2021;10:3836; Sleep Med Rev 2022 |
| H01 | Low back pain — try at home (HEP) | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ✅ 2026-11-28 | ACP 2017; JOSPT LBP CPG 2021 |
| H02 | Leg nerve pain (sciatica) — try at home | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ✅ 2026-11-28 | Am Fam Physician 2008; JOSPT LBP+leg 2021 |
| H03 | Neck pain & whiplash — try at home | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ✅ 2026-11-28 | JOSPT neck CPG 2017; Spine 2007;32:618 |
| H04 | Knee arthritis — try at home | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ✅ 2026-11-28 | ACR/AF OA 2019; Messier 2005 |
| P03 | Warning signs — some symptoms can't wait | Education card (urgent) | Justin Jwad, DC | ☐ pending | NICE NG59 red flags; JOSPT red-flag screening |
| P08 | Shoulder pain — improves with loading | Education card | Justin Jwad, DC | ☐ pending | JOSPT shoulder/RC CPG; Cochrane RC exercise |
| P09 | Hip pain — strong hips hurt less | Education card | Justin Jwad, DC | ☐ pending | JOSPT hip CPG; ACR/AF OA 2019 |
| P10 | After surgery — follow surgeon's protocol | Education card | Zubair Fayyaz, PT, DPT | ☐ pending | Procedure-specific protocols; JOSPT post-op CPG |
| H05 | Shoulder pain — try at home | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ☐ pending | JOSPT shoulder/RC CPG |
| H06 | Hip pain — try at home | Home-exercise pamphlet | Zubair Fayyaz, PT, DPT | ☐ pending | JOSPT hip CPG; ACR/AF OA 2019 |

## Reviewer checklist (per handout)
- Clinical accuracy of the "plan," red flags, and dosage against current PT practice.
- Scope: no overclaiming; "educational only / your therapist's plan comes first" retained.
- Red flags complete and correctly escalated (same-day call vs ER/911).
- Sources current and correctly attributed.
- On sign-off: record reviewer + date here, then the download link can be wired to the matching page via the PR gate.

## Approvals
- **2026-11-27 (Fri):** Direction/approach approved by Zubair Fayyaz, PT, DPT and Justin Jwad, DC (relayed by Yousef).
- **2026-11-28 (relayed by Yousef):** finals reviewed and stamped by the allocated reviewer of record —
  - **Justin Jwad, DC:** P01 (low-back movement), P02 (whiplash), P04 (sciatica), P06 (knee), P07 (sleep).
  - **Zubair Fayyaz, PT, DPT:** P05 (work injury), H01 (low-back HEP), H02 (sciatica HEP), H03 (neck/whiplash HEP),
    H04 (knee HEP).
- Storage: generated HTML is not committed (would publish as live pages); the committed `gen.py` reproduces every
  handout exactly, so the reviewed set is preserved in-repo. Next step when ready: wire "Download" links on the
  matching condition/guide pages via the PR gate.

## Backlog (next)
Warning-signs / red-flags card (needs its own two-urgent-column layout) · shoulder pain (card + HEP) · hip pain ·
post-surgical return-to-activity · "How we measure your recovery" (likely a web page, not a handout).
Once reviewed handouts accumulate, wire "Download" links on the matching condition/guide pages via the PR gate.
