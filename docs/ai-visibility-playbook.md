# Proof — AI visibility playbook (fixing the "AI visibility = 0")

Created 2026-11-26. Owner actions are marked **[Yousef/owner]**; site actions **[autopilot/Claude]**.

## The diagnosis (why it's 0, in one paragraph)
AI visibility at the **brand** level ("tell me about Proof PT", "is Proof good") is driven mostly by Proof's **off-site footprint** — the models answer from a web-wide consensus about the brand. Proof hasn't opened (Feb 2027), has no live Google Business Profile, no reviews, and almost no third-party citations, so that consensus doesn't exist yet and the brand score reads ~0. This is **not a site defect**: robots.txt allows every AI crawler (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, OAI-SearchBot), schema/llms.txt are in place, and the site is fully citable. The fix is building the off-site entity (GBP → citations → mentions → reviews), which compounds over months. In parallel, Proof can win **non-branded** AI citations ("best PT for a car accident in Sterling Heights", "how does Michigan no-fault pay for PT") on merit now, because the models cite the best answer regardless of brand fame — and that content largely already exists.

Two different games: **branded** (needs entity existence — the 0) and **non-branded** (needs topical authority — winnable pre-opening).

---

## 1. Canonical NAP — use this EXACT block on every listing [Yousef/owner]
Inconsistent name/address/phone across the web is the #1 thing that suppresses entity recognition. Copy-paste identical every time.

```
Name:     Proof Physical Therapy
Address:  44056 Mound Rd, Suite 103, Sterling Heights, MI 48314
Phone:    (586) 800-8488
Email:    hello@proofphysicaltherapy.com
Website:  https://www.proofphysicaltherapy.com
Hours:    Mon–Fri 7:00 AM–7:00 PM; Sat 8:00 AM–1:00 PM (planned; opening Feb 2027)
Category: Physical therapy clinic (primary)
Opening:  February 2027
```
Rules: always "Proof Physical Therapy" (never "Proof PT" as the listing name), always "Suite 103", always the (586) format, always the www URL. Do not vary abbreviations ("Rd" vs "Road" — use "Rd"). Clinicians for provider listings: Zubair Fayyaz, PT, DPT (NPI 1508250382; MI PT 5501016612) and Justin Jwad, DC (NPI 1770931545; MI 2301010442).

## 2. Google Business Profile — the single biggest lever [Yousef/owner]
GBP is the strongest entity signal for both Google's AI surfaces and the LLMs. A future-opening business is allowed to create and verify a profile with a month/year, and a verified future-dated profile can appear ~90 days before opening.
1. Create the profile at business.google.com with the exact NAP above; category "Physical therapy clinic".
2. Set the opening date to February 2027 (Google allows the future date).
3. Complete every field: services (map to the site's service lines), description, hours, photos when available, the two providers.
4. Start verification now (postcard/phone/video can take 1–3 weeks). Treat profile eligibility, verification, live visibility, and actual opening as four separate checkpoints.
5. Do **not** solicit incentivized reviews; after opening, invite genuine reviews per Google policy.

## 3. Bing Webmaster Tools + Bing Places [Yousef/owner]
ChatGPT and Copilot lean heavily on Bing's index, so Bing presence disproportionately helps AI visibility.
1. Add + verify the site at bing.com/webmasters (import from Search Console to save time).
2. Submit the sitemap: https://www.proofphysicaltherapy.com/sitemap.xml
3. Create a Bing Places listing with the canonical NAP.

## 4. Citation / directory targets — consistent NAP everywhere [Yousef/owner, or Semrush Local]
The Semrush **Local** listing-management add-on (we started setting this up — it needs the paid slot) can push these automatically; otherwise do the top tier by hand. Priority order:
- **Tier 1 (do first):** Google Business Profile, Bing Places, Apple Business Connect (Apple Maps / Siri), Healthgrades, WebMD/Vitals, Yelp.
- **Tier 2 (healthcare/PT):** Doctor.com, NPI registry profiles (already have NPIs), Zocdoc (if taking bookings), the APTA / Michigan Physical Therapy Association directory, local Michigan chiropractic directory for Justin.
- **Tier 3 (local/geo):** Sterling Heights Regional Chamber of Commerce, Macomb County business directories, Nextdoor business page, Facebook + Instagram business profiles, LinkedIn company page.
Each listing must use the Section-1 block verbatim and link to the www homepage.

## 5. Schema `sameAs` — drop-in once profiles exist [autopilot/Claude]
The moment the real profile URLs exist, add them to the site-wide Organization/MedicalClinic node so the models can resolve Proof's verified identities. Pre-written for when the URLs are in hand:
```json
"sameAs": [
  "<Google Business Profile URL>",
  "<Facebook page URL>",
  "<Instagram URL>",
  "<LinkedIn company URL>",
  "<Healthgrades profile URL>",
  "<Yelp URL>"
]
```
Send me the live URLs and I'll ship this as a one-line-per-page PR.

## 6. Non-branded content — mostly built; make it get cited [autopilot/Claude]
Coverage is already strong (no-fault, direct access, PT cost, workers-comp, 2 original data assets, auto-accident, insurance, outcomes). The lever here is **authority** (Section 7), not more pages. Two genuine net-new assets worth building, both high AI-prompt demand, both buildable without new clinical claims:
- **"How long does recovery take after a car accident?"** — a timeline/expectations resource (data + process, not a treatment promise). High-frequency AI question; complements the existing first-30-days guide.
- **"How to choose a physical therapist in Michigan"** — a decision guide (what to ask, direct access, coverage, measurement). Pure consumer-guidance, no clinical claim; naturally positions Proof's differentiators.
Both can be drafted and shipped on your go-ahead. Everything clinical still routes through the review queue.

## 7. Third-party mentions & links — what earns the citations [Yousef/owner]
AI models weight consensus across independent sources. A few quality ones move the needle more than volume:
- Partner/referral pages linking to Proof (Medicina Scarlett co-location, referring physicians, attorney partners).
- Local press / community coverage of the Feb 2027 opening and the free community workshops.
- The Michigan PT/chiropractic association member pages.
Avoid paid link schemes — they're a spam-policy risk and the models don't reward them.

## 8. Dated sequence
- **By Dec 10, 2026 [owner]:** GBP created + verification started; Bing Webmaster + Bing Places; Tier-1 citations live. → This is what starts moving the number.
- **By Dec 20, 2026 [Claude]:** ship the 2 non-branded assets (on your go-ahead); add `sameAs` once GBP URL exists.
- **By Jan 15, 2027 [owner]:** Tier-2 + Tier-3 citations; secure 2–3 partner/press links.
- **Opening (Feb 2027) [owner]:** switch GBP to open; begin genuine review invitations.

## 9. How to measure
- Semrush AI Toolkit / AI Brand Performance: re-run monthly; expect branded score to stay low until GBP + citations land, then climb.
- Manual spot-check (free): ask ChatGPT, Gemini, Perplexity, and Google AI Mode the non-branded questions ("best physical therapy for a car accident in Sterling Heights MI") and note whether a Proof page is cited — this tells you the non-branded game directly.
- Watch the gap: branded mentions will lag non-branded citations by months — that's expected.

---
**Bottom line:** the site is already doing its job (citable, crawlable, schema-rich). The 0 moves when the **off-site entity** exists — GBP first, then citations and mentions. Start with Sections 2–4; hand me the profile URLs and I'll wire up `sameAs` and build the two content assets.
