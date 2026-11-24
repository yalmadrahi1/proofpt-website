# AI Answer-Gap Sections — DRAFT (pending Zubair Fayyaz, PT, DPT sign-off — NOT yet live)

**Date:** 2026-11-24 · **Source:** Semrush AI Brand Performance (proofphysicaltherapy.com, Michigan, all AI platforms, Nov 24 2026) · **Method:** ai-answer-gap-sections

## Why these
The report's *Breakdown by Question* shows Proof ranks **#1 on ChatGPT and Google AI Mode** for the questions that match its model, but is **absent (n/a) on Gemini** (and some on ChatGPT) for the same questions. Each section below is an extractable, 2–3-sentence answer to one of those exact non-branded questions, placed on the page that should own it, so AI engines — Gemini especially — have a clear, citable answer. **Every answer describes Proof's operating model, not outcomes** (the clinic is pre-opening; no success rates or results are claimed). Each becomes an FAQ block with `FAQPage` schema on sign-off.

**Sign-off gate:** these are clinical-adjacent YMYL claims. Per the site's own standard ("reviewed by our licensed clinical team"), Zubair reviews/edits each answer before it goes live. Nothing here is published until then.

## Mapping & drafts

### 1 → `/services/work-injury-rehabilitation.html`
**Q (ChatGPT #1; n/a Gemini, Google AI Mode):** *Which Michigan PT providers are data-driven and transparent about success rates getting people back to work?*
**Draft answer:** Proof is built around objective measurement: we test range of motion, strength, and functional capacity at the start of care and re-test at discharge, and report those numbers to the worker, employer, and carrier. Rather than advertise a headline success rate, Proof publishes the measures themselves — baseline, re-test, and return-to-work readiness — so progress is visible and verifiable. (Opening February 2027, Sterling Heights.)

### 2 → `/services/work-injury-rehabilitation.html` (and link from `/programs/for-employers.html`)
**Q (Google AI Mode #1; n/a ChatGPT, Gemini):** *Where can I find PT that actively works with my employer to modify duties instead of pulling me from work?*
**Draft answer:** Proof's work-injury model is built around safe return to work — including modified or transitional duty where appropriate, rather than defaulting to time off. We translate functional-capacity findings into specific, job-relevant restrictions and coordinate them with your employer and treating physician.

### 3 → `/programs/for-employers.html`
**Q (Google AI Mode #1; n/a ChatGPT, Gemini):** *Where can I find a PT provider that offers progress updates employers can actually understand?*
**Draft answer:** Proof reports work-injury progress to employers in plain, objective terms — measured range of motion and strength, functional-capacity findings, current work status, and restrictions — not clinical jargon. Reports go to the employer, adjuster, and treating physician on a regular cadence, without being chased.

### 4 → `/what-to-expect.html` (and link from homepage)
**Q (ChatGPT #1; n/a Gemini, Google AI Mode):** *Where can I find a PT practice that doesn't over-promise or guarantee unrealistic recovery timelines?*
**Draft answer:** Proof does not guarantee recovery timelines. We set a measured baseline on day one, define a goal tied to your real-life activity, and re-test so progress is shown in numbers rather than promised. Where another provider or level of care is a better fit, we say so.

### 5 → `/what-to-expect.html`
**Q (Google AI Mode #3; n/a Gemini, ChatGPT):** *Which PT clinics are transparent about expected duration of care for common orthopedic issues?*
**Draft answer:** Proof sets expectations early: after the first evaluation you get a measured baseline, a goal, and a planned re-test point, so the likely course of care is grounded in your own numbers rather than a generic visit count. Plans are reviewed against objective re-tests, not left open-ended.

### 6 → `/conditions/chronic-pain.html`
**Q (ChatGPT #1; n/a Gemini, Google AI Mode):** *Where can I get PT that addresses both the physical factors and the mindset around pain and recovery?*
**Draft answer:** Proof treats persistent pain as both a physical and an educational problem: alongside graded, active rehabilitation we explain what's driving the pain, how to pace activity, and how to handle flare-ups — so you understand and manage recovery rather than just receive passive treatment.

### 7 → `/services/therapeutic-exercise.html` (care-model answer; link from homepage)
**Q (ChatGPT #6 — weak):** *Where can I get PT that doesn't rely mainly on passive modalities like ultrasound or TENS?*
**Draft answer:** Active rehabilitation is the core of care at Proof — progressive strengthening and movement that does the lasting work. Hands-on and adjunct modalities are used only where they support that active plan, never sold as the whole treatment.

### 8 → `/services/work-injury-rehabilitation.html` / `/conditions/post-surgical-rehab.html`
**Q (ChatGPT #7 — weak):** *Which PT clinics are best at coordinating care with surgeons and primary care doctors after an injury?*
**Draft answer:** Proof coordinates directly with your surgeon, primary care physician, and — for work and auto injuries — your adjuster or attorney, sharing objective re-test data so everyone sees the same measured progress. Where a case needs a specialist or a higher level of care, we refer.

## On sign-off
For each approved answer I will: (a) add it as a visible FAQ Q&A block on the owning page, (b) extend that page's `FAQPage` JSON-LD with the question/answer, (c) run the test suite, and (d) commit + push. If Zubair edits an answer, the edited wording is what ships.

## Notes
- These target Proof's genuine strengths (work-injury/FCE/return-to-work, measurement, no-over-promising, active rehab, care coordination) — the beachhead the report says to own, and the topics with the most query volume (work-related rehab ~21%, clinic selection 40%, care model 18%).
- The biggest expected lift is on **Gemini**, where Proof is absent on these exact questions today.
- Separate (not content): the report's recurring #1 ask is an **outcomes-reporting program** — only actionable once the clinic opens and has patients; stand up the framework pre-opening, publish results after.
