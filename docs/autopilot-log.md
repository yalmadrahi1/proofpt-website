# Proof website autopilot log

Newest run first. Keep the last 20 runs.

## Waiting for the clinical reviewer

(none)

## Approved

- **2026-11-25 — 42 clinical pages, dated reviewed-by (PR #9).** Zubair Fayyaz, PT, DPT and Justin Jwad, DC reviewed and approved all 42 queued pages on 2026-11-25 (relayed by Yousef; mapping confirmed). Reviewer of record: Justin Jwad, DC on the 34 musculoskeletal pages; Zubair Fayyaz, PT, DPT on the 8 PT-scope pages. 41 stamped with "Reviewed by <name> on November 25, 2026" + `reviewedBy`/`lastReviewed` schema. Full record: docs/clinical-review-queue.md.
- **Held:** /services/functional-capacity-evaluation.html — approved by Zubair 2026-11-25 but frozen for the rank experiment; stamp its reviewed-by byline (Zubair, 2026-11-25) when the freeze lifts.

## Runs

### 2026-11-26 — scheduled autopilot (Thanksgiving)

**Google guidance checked (2026-11-26):** Search Status Dashboard — November 2026 core update started Nov 10, listed duration 13 days 20 h (≈ complete Nov 24); no spam or other ranking incidents in November. Dashboard also shows a "December 2026 core update" entry dated Nov 24 marked "Information" (announcement only — re-check its status next run). Impact: per the core-update protocol, no impact analysis until ≥1 full week after completion (earliest Dec 1); the Dec 1 re-check in docs/core-update-compliance-2026-11.md has **not** recorded a decision yet, so eastpointe/roseville + the 8 short condition pages stay frozen. Search Console / GA4 / GBP / generative-AI setting: not accessible to this session (owner-gated) — unchanged gap.

**Data used:** Semrush connector — Position Tracking 31708634_5685808 (desktop, Sterling Heights), dates Oct 28 → Nov 25; visibility (estimate) **0.17% (Nov 18) → 1.46% (Nov 25)**. Per-keyword pull done this run (weekly-rank doc not reachable from this session): only 2 of 19 keywords rank — "functional capacity evaluation near me" **#59 → #7** and "workers compensation physical therapy near me" **#82 → #12**, both now ranking via **/areas-served/macomb-township-mi/** (frozen) rather than the FCE / work-injury service pages; 10 keywords were added to the campaign Nov 26 and have no reads yet (incl. "physical therapy sterling heights", ~110/mo est.). Site Audit snapshot 6b080d40 (crawl finished Nov 26, 10:45 UTC): 195 errors — 164 "broken internal links" + 1 5xx + 1 sitemap item all = one transient **503 on /services/neuromuscular-reeducation.html** (file present, unchanged; GitHub Pages blip); **29 structured-data errors**. Units used ≈ 2,700 (left 33,100). Weekly-rank / baseline / semrush-monthly project docs: not reachable from this session (no Projects tool) — used live connector data instead.

**PR:** see PR for this branch (autopilot/2026-11-26-run).

Changes (each pre-approved: structured data / internal links):
1. **Schema fix — reviewedBy/lastReviewed moved off `Article` onto a `WebPage` node** (20 guides). Semrush: "NOT_RECOGNIZED reviewedBy, lastReviewed" on ARTICLE (they are WebPage properties). Article now has `@id #article` + `mainEntityOfPage`; new WebPage node carries the same reviewer/date already shown on-page (no reviewer or date changed). Acceptance: 0 Article-level reviewedBy; next Site Audit drops those 20 markup errors. Follow-up: next Site Audit crawl (≈Dec 3–4).
2. **Schema fix — `MedicalClinic` stubs on team/index, team/zubair-fayyaz-dpt, team/justin-jwad-dc** got the address + phone already published on the home page. Semrush: LOCAL_BUSINESS "REQUIRED address". Acceptance: 3 errors cleared next crawl.
3. **Internal links to 10 under-linked guides** (Semrush "pages with only one internal link": TMJ, spinal stenosis, snapping hip, shoulder impingement, piriformis, pinched nerve neck, knee bursitis, groin strain, golfer's elbow, Achilles) — "Related reading" links added on conditions/neck-pain, sciatica, back-pain, headaches-migraines, foot-ankle-pain, elbow-wrist-hand-pain and services/sports-injury-rehabilitation, orthopedic-physical-therapy. No clinical text changed. Acceptance: each guide ≥2 inbound internal links; Follow-up: next Site Audit crawl (≈Dec 3–4).
4. **Test:** test/ci_static.py now fails on reviewedBy/lastReviewed on an Article node and on a LocalBusiness-type node without an address (verified it catches the pre-fix markup).

Skipped / held, and why:
- **WebApplication markup on the 6 tool pages** (Semrush SOFTWARE_APP "REQUIRED aggregateRating/review"): left as is — Proof has no genuine ratings and will not add self-serving review markup. The error only means no Software-App rich result; noted, not fixed.
- **FCE cannibalization** (Macomb page ranking for FCE / workers' comp): both pages frozen; internal-link changes toward the FCE page are allowed but deferred one week so the 4th weekly read (Dec 2) of the Nov 7 rank experiment stays clean. FCE reviewed-by byline (Zubair, 2026-11-25) stays held until the freeze lifts.
- Eastpointe/Roseville + 8 short condition pages (core-update deferral), long titles on 7 pages (cosmetic), HSTS (GitHub Pages host setting — not ours to change).
- No new pages; no clinical claims created or changed → nothing added to the clinical review queue.

Measure next run: Dec 2 position read (does FCE #7 hold; which URL ranks; first reads for the 10 new keywords incl. "physical therapy sterling heights"); next Site Audit — errors should fall from 195 to ≲6 (the tool-page SOFTWARE_APP items); after Dec 2 read completes the freeze window, consider pointing FCE-intent anchors on work-injury pages at /services/functional-capacity-evaluation.html.

### 2026-11-25 — manual run (Yousef: "ensure the site meets UI/UX + further enhance AI and SEO visibility")

Operator: Claude (interactive, not the scheduled autopilot). Data used: local render/audit of all 164 pages (Playwright + static scans); Semrush not pulled this run.

UI/UX + accessibility audit (no defects warranting change):
- Rendered home, clinic, condition, service, tool, guide, insurance, about, refer, faq at 390px + 1280px. No horizontal overflow anywhere; one descriptive H1/page; all images carry alt; hero eager / rest lazy; skip link + `main` landmark present; `:focus`/`:focus-visible` styles on every page.
- `.reveal` opacity-0 sections are added by JS only to below-fold blocks (progressive enhancement) and are forced visible under prefers-reduced-motion — content is fully visible without JS. Working as designed; left alone.
- Automated contrast scan flagged 23 items, but all are false positives from gradient/image/dark-section backgrounds the walker resolved to white (e.g. white-on-navy hero read as 1.0 white-on-white). The one dark-bg hit (`--mut` #4E5F82 caption) actually sits on white (~7:1). No real contrast defect; no color changes made.
- Internal linking: 0 orphan pages; the 3 Dataset guides each have 3–5 relevant inbound links.

Shipped:
- **PR #6** (merged 18dc376) — structured-data coverage: `Dataset` schema on the 3 data-asset guides (gov agency as data creator, Proof as publisher, temporal/spatial coverage, variableMeasured, real CSV as DataDownload → eligible for Google Dataset Search + AI answer engines); `WebApplication` schema on the 4 planning tools (+breadcrumb where missing); `MedicalWebPage`/`CollectionPage` + `BreadcrumbList` on first-visit-checklist, progress-report-example, tools/index, areas-served/index. 162 JSON-LD blocks valid.
- **PR #7** (merged 5bc0ebe) — repaired 3 truncated meta descriptions (knee-bursitis, pelvic-floor-exercises ended mid-sentence; og:/twitter: synced) + sports-performance; refreshed sitemap `lastmod` to 2026-11-25 for the 14 pages changed this session.

Checks: npm test (90) + ci_static (164 pages, 0 problems) passed on both PRs; verify green; deploy:success. Production verified live after CDN propagation.

Skipped / deferred: title-length trims (74 pages 63–70 chars — kept the local "in Sterling Heights, MI" qualifier; not worth the ranking risk); long-meta trims (minor, cosmetic truncation only); FCE + Macomb left frozen per policy; GBP `sameAs` not added (owner-gated, unverified profiles).

Measure next run: whether Dataset guides pick up Dataset-Search / AI-citation surfaces; tool pages' rich-result eligibility in Search Console once indexed.

### Clinical review workflow (set 2026-11-25, prior turn)
- docs/clinical-review-queue.md (PR #5) holds 42 condition/service pages awaiting a real dated reviewer sign-off (Justin broad; pelvic/balance/vestibular/post-surgical → Zubair). Apply dated "Reviewed by <name> — <date>" byline + reviewedBy schema ONLY when the queue records reviewer + date. Never stamp an unreviewed byline.
