# Proof website autopilot log

Newest run first. Keep the last 20 runs.

## Waiting for the clinical reviewer

(none)

## Approved

(none)

## Runs

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
