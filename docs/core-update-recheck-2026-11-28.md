# Post-Rollout Re-Check — Google November 2026 Core Update

**Date:** 2026-11-28 · **Site:** proofphysicaltherapy.com (pre-opening, YMYL medical) · **Repo HEAD:** 7809b12 · **Audit commit under review:** 9d958bd
**Scope:** scheduled re-check of the 2026-11-23 audit (`core-update-compliance-2026-11.md`). Report-and-recommend only — no index/redirect/content changes made, nothing committed.

## 1. Rollout status (confirmed via web)
- **November 2026 core update: COMPLETE.** Google updated the Search Status Dashboard to mark the rollout complete on **Nov 24, 2026 ~9:03am ET** (14-day rollout, Nov 10 → Nov 24). Reported by Search Engine Roundtable, attributed to Google's dashboard.
- **December 2026 core update: PRE-ANNOUNCED, not yet live.** Google preannounced it Nov 24 (new practice, tied partly to UK CMA advance-notice rules). Google confirmed it is **not active**, with no start date and "not imminent." The status dashboard shows a December incident entry dated Nov 24, but it has not started rolling out.
- **Implication:** once December goes live it will re-shuffle rankings again, so the clean before/after window for *November* is narrow — the sooner the Dec-1 pull happens the better.

## 2. Timing of the data comparison
- Google advises waiting ~1 week after completion before trusting Search Console comparisons → **~Dec 1** (matches the audit's pre-set checkpoint).
- Today (Nov 28) is only **4 days** post-completion, and **Thanksgiving (Nov 26) + Black Friday (Nov 27)** fall inside the latest-14-day window — any comparison today would be seasonally distorted.
- **Recommendation: run the formal before/after pull on or after Dec 1.**

## 3. Structural re-audit (re-run today)
| Check | Result |
|---|---|
| Invalid JSON-LD (164 pages, `test/ci_static.py verify`) | **0** (exit 0, "pages checked: 164; problems: 0") |
| Duplicate `<title>` | **0** |
| Duplicate / empty / missing meta descriptions | **0** (the apparent Michigan-guides pair was a scan artifact; the two descriptions are distinct) |
| Test suite (`npm test`) | **90/90 pass** (50 intake + 35 referral + 5 CTA) |
| **E-E-A-T `accountablePerson` (commit 9d958bd)** | **Still live on all 41 condition/service pages** |
| E-E-A-T — enhanced since audit (commit cc3975f) | `reviewedBy` = Justin Jwad, DC + `lastReviewed` 2026-11-25 added to schema; visible dated byline "Reviewed by Justin Jwad, DC on November 25, 2026" now present. All 41 pages carry **both** the schema signal and a visible clinician byline. |
| Areas-served city pages | **Byte-identical to the audit commit** (only `areas-served/index.html` gained 1 line) → doorway similarity **unchanged** from Nov 23 (eastpointe/roseville remains the top near-duplicate pair). No new duplication. |
| 8 deferred thin condition pages | **Still thin** (~399–474 main-content words; audit said 416–449). Not enriched — the only diffs since the audit are the reviewed-by byline/schema. |

Note on similarity metric: absolute doorway-similarity values are highly metric-dependent (flat word overlap ≈0.9, TF-IDF cosine ≈0.03 for the same city pair). Because the city-page files are unchanged since the audit, the relationship is definitionally unchanged — no need to re-pin the 0.73 figure.

## 4. Decision rule (audit §4) — CANNOT be applied this run
The rule requires Google Search Console impressions (domain property `sc-domain:proofphysicaltherapy.com`), comparing Oct 27–Nov 9 vs the latest 14 days, flagging a page only if its impressions fell **25+ points more than the rest of the site**.

**GSC is not reachable this session.** The Windsor.ai connector (the available route to Search Console) is `connect_incomplete`; there is no direct GSC connector. Per instructions, **no numbers were guessed or substituted** (Semrush estimates are not GSC and would not satisfy a rule defined on GSC impressions).

→ **Neither deferred item is flagged for action** — not because they passed the rule, but because the triggering data is unavailable and it is pre-checkpoint.

## 5. Recommendations
1. **eastpointe ↔ roseville city pair** — keep-and-watch (unchanged). Differentiate with genuinely local content **only if** the Dec-1 GSC pull shows its impressions fell 25+ pts more than the rest of the site.
2. **8 thin condition pages** (knee-pain, dizziness-vertigo, post-surgical-rehab, shoulder-pain, sports-injury, chronic-pain, hip-pain, herniated-disc) — keep-and-watch (unchanged). Enrich with accurate clinical content only if they breach the same rule at Dec 1.
3. **Enable the data pull:** complete the Windsor.ai connection (or connect Google Search Console) for `sc-domain:proofphysicaltherapy.com`, then re-run on/after Dec 1 — ideally before the December core update goes live.
4. **No destructive action taken.** Index removal, redirects, consolidation, and content rewrites remain the owner's decision with data. Nothing was committed.

**Caveat:** rollout-completion and the December preannouncement are third-party reporting (Search Engine Roundtable) attributed to Google's Search Status Dashboard.
