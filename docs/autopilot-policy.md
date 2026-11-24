# Proof Physical Therapy website autopilot policy

Set up Nov 24, 2026 at Yousef's request ("utilize this for all my website projects"), modeled on the Grove autopilot.
The scheduled autopilot reads this file at the start of every run. Change it by pull request; the autopilot follows the
version on main.

Proof Physical Therapy is a pre-opening outpatient PT clinic in Sterling Heights, MI, opening February 2027.
Clinical oversight on the site: Zubair Fayyaz, PT, DPT (the "Clinical oversight" line and accountablePerson schema added
in commit 9d958bd). Phone (586) 800-8488.

## Pre-approved: the autopilot may merge these once all checks pass

- Titles, meta descriptions and intros aimed at queries the data shows, kept accurate, one primary page per query
  (except the frozen pages below).
- Internal links, anchor text, related-page lists, breadcrumbs and menus.
- Structured data, sitemap, robots, 301 redirects, accessibility, page speed, broken links, mobile layout.
- Non-clinical clarity edits: opening date, hours, arrival details, insurance and payment wording that only restates
  what the site already says, FAQ entries on logistics (what to bring, parking, how requests work).
- Updates of official, sourced non-clinical figures (for example Michigan no-fault or workers' compensation rules),
  checked against a primary source fetched that run (legislature.mi.gov, DIFS, Michigan Workers' Disability
  Compensation Agency), cited on the page with "as of <month year>".
- Planning tools (coverage checker, visit budget estimator, FCE prep builder, recovery goal builder): bug fixes,
  accessibility, wording clarity. Any change to how a tool calculates goes to a pull request for Yousef.

## Needs the clinical reviewer (own pull request, not merged by the autopilot)

- Any new or changed clinical statement: what a condition is, what a treatment does or is for, who it suits,
  expected course, risks, contraindications, or evidence.
- New condition, service or guide pages (at most 2 proposed per run, each for a query with real demand, substantially
  unique, never a city-name swap).
- Anything about shockwave therapy (ESWT), therapeutic laser, dry needling or Functional Capacity Evaluations beyond
  logistics.
Approval counts once it is recorded in this repo (docs/autopilot-log.md, "Approved" line with the pull request number,
the reviewer's name and the date, relayed by Yousef counts).

## Frozen for now (no title, H1, meta or body changes)

- Until the Proof weekly rank check has 4 weekly reads after Nov 7, 2026 (it compares against the frozen Nov 7
  baseline): services/functional-capacity-evaluation.html and the Macomb Township areas-served page (areas-served/macomb-township-mi/). Internal links
  pointing to them may change.
- Until the Dec 1, 2026 core-update re-check records a decision in docs/core-update-compliance-2026-11.md: the
  deferred items in that doc (areas-served/eastpointe-mi/, areas-served/roseville-mi/ and the eight short condition
  pages it lists).

## Never

- Say or imply that Proof is open, that anything is bookable now, or that a visit is booked before February 2027;
  a request is not an appointment.
- Claims such as "no visit cap", "typically $0", "all carriers", "all major plans", "computerized testing",
  "guaranteed", "regenerates tissue", cure or recovery-time promises, superlatives ("best", "only", "leading").
- Invent testimonials, reviews, outcomes, statistics, credentials or clinician names.
- Mention Specialty Medical Center or SMC; Proof stays separate on this site.
- Change the intake or referral form handlers, their endpoints, or submit a real request to test anything.
- Change the Google Business Profile, Search Console, DNS, the CNAME file, GitHub settings, or anything that costs money.
- Delete a page without a 301.
