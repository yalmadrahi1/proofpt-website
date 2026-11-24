# Core Update Compliance Audit — Google November 2026 Core Update

**Date:** 2026-11-23 · **Site:** proofphysicaltherapy.com (pre-opening, YMYL medical) · **Commit:** 9d958bd

## 1. What the update is
- **November 2026 core update**, announced **Nov 10, 2026**; Google says it "may take up to **2 weeks** to complete" (completing ~Nov 24).
- Google's exact wording: *"a regular update designed to better surface relevant, satisfying content for searchers from all types of sites."*
- **No new rule, no named targets, no content type singled out.** Not a penalty. No structured-data deprecation, no page-experience/HTTPS change, no AI-search reporting change tied to it.
- **Therefore "compliance" = Google's standing guidance:** people-first content, **E-E-A-T (weighted heavily for YMYL — this is a medical site)**, spam policies, valid structured data, page experience.
- Sources: Search Engine Roundtable (Nov 10, 2026); Google Search Central / LinkedIn announcement.

## 2. Audit results (163 pages, built site)
| Check | Result |
|---|---|
| Invalid JSON-LD | **0** |
| Retired / misused schema types | none |
| Self-serving `aggregateRating` / `Review` on own business | **none** (correctly refused when Semrush suggested adding them) |
| Dangling schema `@id` refs (reviewedBy/author/accountablePerson) | **0** |
| Duplicate `<title>` | **0** |
| Duplicate / empty meta descriptions | **0** |
| Missing canonical | **0** |
| `noindex` leaks | only `/404.html` (intended) |
| Doorway similarity — conditions / services / locations | avg 0.24 / 0.12 / 0.09 (low) |
| **E-E-A-T: clinical pages naming no responsible clinician** | **41 pages (fixed — see §3)** |
| Doorway similarity — areas-served | avg 0.54; **1 pair > 0.70** (deferred — see §4) |
| Borderline-thin condition pages (416–449 words) | 8 (deferred — see §4) |

## 3. Fixed now (defect fix, commit 9d958bd)
All 41 `/conditions/*` and `/services/*` clinical pages named no responsible clinician in text or schema. Added the **accurate** responsible-professional signal (not a manufactured per-page review):
- Schema: `accountablePerson` = Zubair Fayyaz, PT, DPT (the clinic's named clinical lead) on each page's `MedicalWebPage` node. **`accountablePerson`, not `reviewedBy`** — accountability is true now; individual page review is published when complete.
- Visible: *"Clinical oversight: Zubair Fayyaz, PT, DPT. Every clinical page on this site is reviewed by our licensed clinical team before the clinic opens; the individual reviewer and date are published here when that review is complete. General information, not medical advice."*
- Re-validated: 0 invalid JSON-LD; 90/90 tests pass.

## 4. Deferred to post-rollout (no page rewrites mid-rollout)
Google advises waiting ~1 week after the rollout completes before comparing Search Console data; index-removing changes are the owner's call with data.

**Risk table**
| Item | Detail | Recommendation |
|---|---|---|
| `eastpointe` ↔ `roseville` city pages | content similarity 0.73 (only pair site-wide over 0.70) | keep-and-watch; differentiate with genuinely local content if it underperforms |
| 8 condition pages at 416–449 words | knee-pain, dizziness-vertigo, post-surgical-rehab, shoulder-pain, sports-injury, chronic-pain, hip-pain, herniated-disc | keep-and-watch; enrich with accurate clinical content if they underperform |

**Decision rule (set now, apply ~Dec 1 after rollout completes):** pull Search Console (domain property), compare the 14 days before the update (Oct 27–Nov 9) with the latest 14 days. For a flagged page/group, if its impressions fall **25+ points more than the rest of the site's change** over the same window, act (differentiate the city pair; enrich the thin page). Judge **relative to the rest of the site** — holidays (Black Friday / Thanksgiving) move everything. Otherwise keep as-is. Removing any page from the index is the owner's decision.

## 5. Owner / access-gated
- Search Console checks (manual actions, security, indexing, the before/after pull) need the owner GSC account — not accessible this session.
- No disavow change: toxic-link spam is ignored by Google absent a manual action (none present).

## 6. Spam-policy (SpamBrain) audit — 2026-11-24
SpamBrain is Google's ML spam-detection system; it enforces the published spam policies rather than a separate rulebook, so the site was audited against each policy.

| Spam policy | Result |
|---|---|
| Hidden text / links | **clean** (0 — body markup scanned with CSS/JS excluded; no hidden or off-screen keyword text, no stuffed `sr-only`) |
| Cloaking / crawler sniffing | **clean** (0 — no user-agent/Googlebot detection) |
| Sneaky redirects (meta-refresh / JS) | **clean** (0) |
| Keyword stuffing | **clean** — flagged terms are topical ("dry needling" on the dry-needling guide), navigational, or date chips; city pages name their city across title/meta/schema/body as expected, not stuffed |
| Doorway / scaled-content abuse | low similarity (conditions 0.24, services 0.12); one near-duplicate city pair `eastpointe`/`roseville` (0.73) — already in the §4 deferred queue with the decision rule |
| Misleading functionality | **clean** — "open now" refers accurately to referrals/requests being accepted pre-opening, not the clinic being open |
| AI-answer manipulation (2026 policy) | **clean** — llms.txt and pages contain no injected/hidden instructions; AEO is accurate, honest content |
| Link spam | the `rankvance.com` PBN was disavowed (Nov 21); no new unnatural links; SpamBrain neutralizes residual spam algorithmically |
| Expired-domain / site-reputation / parasite / thin-affiliate / UGC spam | **not applicable** (fresh single domain; no third-party, affiliate, or user-generated content) |

**Verdict: no spam-policy violations — no fixes required.** The only spam-adjacent item (the one near-duplicate city pair) is handled by the existing deferred decision rule and the Dec 1 re-check.
