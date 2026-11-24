# "Proof of Outcomes" Reporting Framework

**Date:** 2026-11-24 · **Owner:** Yousef (ops) + Zubair Fayyaz, PT, DPT (clinical) · **Status:** framework ready; publishes real data **after** the clinic opens (Feb 2027) and has a first discharged cohort.

## Why this is the #1 AEO asset
Across every section of the Nov 24 AI Brand Performance report, the single most-repeated recommendation is to **replace the "promising but new" narrative with a documented outcomes record**. AI engines (and referrers) default to established systems because their track record is *visible and citable*. Proof already wins on sentiment (92%) and is cited for its *model*; a transparent, structured outcomes page is what converts that into being **recommended** as a concrete option — especially on Gemini, where Proof is weakest. It is also the honest answer to the exact unanswered questions ("data-driven and transparent about success rates," "tracks outcomes like return-to-work rates and functional improvements").

## Hard guardrails (non-negotiable — this is what makes it credible, not spam)
1. **No numbers before data exists.** Nothing is published until a real cohort has been evaluated *and* discharged. Pre-opening, the page states the methodology only.
2. **Always show sample size (N) and the reporting period** on every figure. "Return-to-work within X weeks (n=42, Jan–Jun 2027)."
3. **No cherry-picking.** Report the full discharged cohort for a period, not selected wins. State who is excluded and why.
4. **State limitations plainly** — single site, self-selected patients, short history, measure definitions.
5. **De-identify to HIPAA standard.** Case journeys carry no identifying detail; aggregate stats only below safe cell sizes.
6. **Clinician-governed.** Zubair signs off on every published figure and every case journey. Protocols for how metrics are defined/collected are published alongside.

## What to measure (all sourced from DrChrono + the computerized testing)
| Metric | Definition | Source |
|---|---|---|
| Functional-test gains | Δ range-of-motion and Δ strength, baseline → discharge (the clinic's differentiator) | Computerized ROM/strength testing in DrChrono |
| Return-to-work rate & timing | % of work-injury patients returned to work (full or modified) and median time | DrChrono + work-status reports |
| Return-to-sport / activity rate | % back to their stated goal activity | DrChrono + goal tracking |
| Visits to discharge | Median visits per episode, by condition group | DrChrono billing/visit data |
| Time to meaningful improvement | Median days to a defined functional milestone | Testing cadence |
| Patient-reported outcomes (PROMs) | Validated scores (e.g. pain/function indices) at intake vs discharge | DrChrono forms |
| Home-program adherence | % completing the prescribed home program | DrChrono / follow-up |
| Satisfaction | Simple post-discharge measure, with N | Post-discharge survey |

## How it's published (so AI can cite it)
- A dedicated **`/proof-of-outcomes.html`** reference page (not a sales page): each metric with its N, period, definition, and a short "how we measure" note.
- **Schema:** `MedicalWebPage` + a `Dataset` node (name, description, temporalCoverage, measurementTechnique) with a `citation`/methodology link — the same citable-primary-source pattern that earned the data guides their AI citations.
- **De-identified case journeys** for the priority case types (active adult with persistent spine/joint pain; physically demanding worker returning after injury; adult rebuilding strength after lower-limb injury/surgery) — baseline → plan → re-test → result, in plain language.
- **Visible clinical governance:** a short note on how protocols are chosen and updated, signed by Zubair.
- Link it from the homepage, work-injury, FCE, and the three named programs; add to `llms.txt` "best pages to cite."

## Dated task plan
| When | Task | Owner |
|---|---|---|
| **Now (pre-opening)** | Lock the metric definitions + collection fields in DrChrono so data is captured cleanly from patient #1 (don't retrofit later) | Yousef + Zubair |
| Now | Build the `/proof-of-outcomes.html` page in **methodology-only** mode (what we measure + how), with the Dataset schema stubbed, no numbers | Claude, on your go |
| Now | Draft the post-discharge PROM + satisfaction instrument in DrChrono forms | Zubair |
| **~Feb 2027 (open)** | Begin capturing baseline tests on every patient | Clinic |
| **~Q3 2027 (first discharges)** | First aggregate pull (N + period), Zubair sign-off, publish the first real figures + 1–2 case journeys | Yousef + Zubair + Claude |
| Quarterly thereafter | Refresh figures; add case journeys; re-measure AI Brand Performance to track the lift | Recurring |

## The honest expectation
This is a **6–12-month compounding asset**, not a quick lever — the first credible numbers can't exist until mid-2027. But locking the measurement now (so patient #1's data is usable) is the cheap, high-leverage move, and it is the one thing the report says will most move Proof from "promising" to "proven" in AI answers.
