# Proof clinical-content & guidelines playbook (learned from the SMC model)

Created 2026-11-28. Source: Yousef shared Specialty Medical Center's (SMC) full clinical-content system — patient
education cards, try-at-home PT pamphlets, a "Care Journey" patient handout + tracker + provider view, and a deep
clinical-evidence/guideline reference layer (FSU, disc pathologies, integrated-spine validation, interventional
spine/ortho master references), all built around SMC's DrChrono data via its "AI Operations Platform."

Purpose of this doc: capture the **method** so that (a) when Proof gets its own EHR, we can build Proof's clinical
guidelines and care-journey system the same disciplined way, and (b) we can utilize the patient-facing pieces on the
Proof website now. This is an internal methodology doc — not patient-facing, not a clinical statement itself.

---

## 1. What SMC built (the reference model)
Four layers, from patient-facing to clinician-facing:

1. **Patient education cards** (E01–E10) — one page each: topic eyebrow, big serif headline, short plain-language
   intro, a two-column "do / don't" (Eat more/less, Helps/Slows recovery, It can/It can't…), one highlighted stat or
   action callout with a big number, real source citations, and a standing footer: *"Educational only, not medical
   advice. Your provider's instructions come first."* Each marked **DRAFT · for clinical & compliance review.**
2. **Try-at-home pamphlets** (H01–H04…) — two pages each: a "How hard?" soreness rule (≤3/10, settling in 24h; *"if
   your therapist gave you a program, follow theirs"*), numbered exercises with dosage (hold/reps/frequency) split into
   "Start now (wk 1–2)" and "Add when these feel easy (wk 3+)", an Every-day / Avoid-for-now pair, a red-flag "Stop and
   call us" box, and a "What to expect" line. **These are already physical-therapy home-exercise programs.**
3. **Care Journey** — the measured-care artifact in three views: a **patient handout** (where you are in the plan ·
   your goals · progress shown as same-scale outcome scores (NRS, ODI, NDI, QuickDASH) · what we've done together ·
   next 90 days · your part · what we're watching · if the plan changes), a **tracker**, and a **provider journey
   view** (pain/function trend charts on the same scales, a "needs you" worklist, active problems vs baseline, a care
   timeline, a **treatment-response ledger** (every intervention · target · measure before→after · decision), a
   guideline check, and coverage/claims).
4. **Clinical-evidence / guideline references** — rigorously sourced modules for clinicians. SMC's are
   interventional-spine/ortho IP (FSU biomechanics, disc pathology, regenerative pathways).

## 2. The method worth copying (this is the real lesson)
SMC's content is good because of *how* it's disciplined, not the topics:
- **The four-claims ladder.** Plausible mechanism → clinical benefit → structural repair → added value of the whole
  program. Evidence for one claim never silently becomes evidence for the next. Unproven things are labelled unproven
  ("promising signal", "not established"). Copy this exactly — it's also Proof's brand ("Recovery, proven", no
  overclaiming).
- **Same scale, every reassessment.** Pain and function measured on fixed instruments at eval, re-check and discharge,
  and shown back to the patient. This *is* Proof's differentiator; make it the spine of every asset.
- **Honesty rails on every patient asset:** "Educational only, not medical advice; your therapist's plan comes first,"
  plus real citations and a visible DRAFT→clinician-review stamp before any patient use.
- **Separation of measures:** pain relief, functional recovery, imaging change, and prevention are different outcomes
  needing different measures — never collapse them into one "it works."
- **One consistent brand system** across every asset.

## 3. The PT translation for Proof (what changes)
SMC is an interventional pain/spine/ortho practice where PT is one supporting lane. **Proof is a pure PT practice**, so:
- **Re-center every asset on active care + measurement.** Where SMC's plan column lists epidural injections, RFA or a
  spine surgeon, Proof's lists graded exercise, nerve-friendly movement, hands-on therapy, a home program, and
  same-scale re-testing. (See the worked example: the "Pain down the leg" card rebuilt for Proof.)
- **Own the patient-facing layers natively** — HEPs, education cards, and the measured-care journey are Proof's core
  competency, not an add-on. Proof can do these better and deeper than a procedural practice.
- **The clinician-facing guideline layer flips** from injection/FSU/regenerative pathways to **PT clinical practice
  guidelines**: movement-system diagnosis, loading/dosage progression, objective outcome-measure standards, and
  return-to-function / discharge criteria — anchored to APTA/JOSPT clinical practice guidelines.
- **Keep the Michigan no-fault / workers'-comp documentation layer** — for Proof's payer mix, the guideline layer must
  also define medical-necessity and progress-note standards that hold up to PIP/WC utilization review. This is where
  Proof's clinical governance and its reimbursement defensibility are the same document.

## 4. When Proof has an EHR (the future-guidelines build)
SMC built its care-journey and provider views from DrChrono fields. When Proof selects an EHR, replicate the pattern:
- **Standardize the outcome-measure set first** (e.g. NPRS for pain; region-specific function: ODI (low back), NDI
  (neck), LEFS (lower limb), QuickDASH (upper limb); plus a global rating). Captured at eval → each reassessment →
  discharge, on the same scale.
- **Build the clinical guidelines as structured EHR content** — eval templates, treatment-progression protocols by
  movement-system diagnosis, re-test cadence, and discharge criteria — the PT analog of Dr. Otero's guideline set.
- **Generate the two journey views from EHR data**: the patient "Care Journey" handout and the clinician "provider
  journey view" (trend charts, treatment-response ledger, guideline check, red-flag screen, work-status timeline).
- **Documentation-defensibility check** baked in: every note ties an intervention to a target and a measured
  before→after, so no-fault/WC review sees objective justification.
- Named reviewer + date on every clinical guideline, same as the website's reviewed-by workflow.

## 5. Website utilization now (what to do before the EHR)
The patient-facing assets double as **E-E-A-T / AEO authority content** — first-party, sourced, clinician-reviewed —
which directly feeds the AI-visibility goal (see `docs/ai-visibility-playbook.md`). Plan:
- Publish Proof-branded **education cards** and **try-at-home HEP pages** as web pages (and printable handouts),
  mirroring Proof's existing ~50 reviewed guides but in the tighter card/pamphlet format.
- Build a public **"How we measure your recovery"** page — the patient-facing explainer of the same-scale
  measurement method (this is the asset SMC's set implies and Proof's brand is built on; it has no injection analog, so
  it's purely Proof's).
- **Every clinical asset routes through the review queue** (`docs/clinical-review-queue.md`): build as DRAFT, open a PR
  marked ready-for-review, add the page to the queue, and apply the dated "Reviewed by" byline + `reviewedBy` schema
  only after Zubair/Justin sign off — exactly the workflow already in place. Nothing clinical auto-merges.

## 6. Build inventory & priority (proposed)
| # | Asset | Type | Clinical review? | Value |
|---|---|---|---|---|
| 1 | "How we measure your recovery" page | Web (patient) | Light (method, few claims) | Brand + AEO; Proof-unique |
| 2 | Education cards (8–10, Proof-recentered) | Web + print | Yes (per card) | Patient trust + AEO |
| 3 | Try-at-home HEP pages (match SMC's H-series topics) | Web + print | Yes (per program) | Patient value + AEO |
| 4 | PT clinical practice guideline set | Internal (clinician) | Authored with clinicians | Care quality + no-fault/WC defensibility |
| 5 | Measured Care Journey handout (manual pre-EHR, automated post-EHR) | Patient handout | Yes | Embodiment of "Recovery, proven" |

Worked example delivered 2026-11-28: `proof-card-sciatica.html` (Proof PT rebuild of SMC card E04).

**Do NOT** copy SMC's text verbatim onto Proof's site (it's SMC's content and partly interventional). Rebuild from PT
sources, in Proof's voice, reviewed by Proof's clinicians.
