# Proof — open tasks, assigned to Ali

Created 2026-11-28 (assigned by Yousef). Clinic opens **February 2027**. The website itself is built and in strong
shape; what's left is mostly **off-site** work (the real lever for getting found) plus relaying a few clinical
sign-offs back so the site can be updated. Full detail for the SEO items is in `docs/ai-visibility-playbook.md`;
the canonical business info is repeated below so you don't have to hunt.

**Canonical NAP — use this EXACT text on every listing (consistency is what makes Google/AI recognize the business):**
```
Proof Physical Therapy
44056 Mound Rd, Suite 103, Sterling Heights, MI 48314
(586) 800-8488 · hello@proofphysicaltherapy.com
https://www.proofphysicaltherapy.com
Mon–Fri 7:00 AM–7:00 PM; Sat 8:00 AM–1:00 PM (planned; opening Feb 2027)
Category: Physical therapy clinic
```

## A. Off-site visibility — the biggest levers (do these first)
| # | Task | Why it matters | Target | Needs / notes |
|---|---|---|---|---|
| A1 | **Create + start verifying the Google Business Profile** with the NAP above; set opening date Feb 2027 | Single biggest signal for Google + AI search; a verified future-dated profile can show ~90 days before opening | **Dec 10** | Owner's Google account. business.google.com. Do NOT solicit incentivized reviews. |
| A2 | **Bing Webmaster Tools** (import from Search Console) + submit sitemap; create **Bing Places** listing | ChatGPT/Copilot lean on Bing's index | **Dec 10** | bing.com/webmasters · sitemap: proofphysicaltherapy.com/sitemap.xml |
| A3 | **Tier-1 citations** with the exact NAP: Apple Business Connect, Healthgrades, WebMD/Vitals, Yelp | Consistent listings build the entity AI engines cite | **Dec 15** | Identical NAP every time; link the www homepage |
| A4 | **Tier-2/3 citations**: APTA / MI Physical Therapy Assn, MI chiro directory (Justin), Sterling Heights chamber, Nextdoor, FB/IG/LinkedIn business pages | Breadth of consistent mentions | **Jan 15** | Semrush Local can automate if the paid slot is added |
| A5 | **Clinician headshots** (Zubair + Justin), professional; facility photos once built out | Real faces lift conversion + E-E-A-T; site currently uses illustrations | Headshots **Dec 20** | Short photoshoot |
| A6 | **Confirm GA4 is counting conversions** (form-submit + call-click) and call tracking is live | Event wiring is already in the site code; someone must mark them as conversions in GA4, or we're blind on what works | **Dec 10** | GA4 property access |
| A7 | **Set up a pre-opening lead nurture** (LeadConnector email/text) for people who request an appointment now | A Nov/Dec request won't be seen until Feb — without nurture those leads go cold | **Dec 15** | LeadConnector |
| A8 | **Collect the live profile URLs** (GBP, Facebook, Instagram, LinkedIn, Healthgrades, Yelp) and send them to Yousef → Claude | Claude wires them into the site's `sameAs` schema so AI engines resolve Proof's verified identities | After A1–A4 | One-line hand-back |

## B. Clinical content — relay sign-offs back
| # | Task | Target | Hand back |
|---|---|---|---|
| B1 | Get **Zubair / Justin** to review the **6 new DRAFT handouts** (P03 warning-signs, P08 shoulder, P09 hip, P10 after-surgery cards; H05 shoulder, H06 hip pamphlets) and confirm the exact wording | **Dec 5** | Send reviewer name + date per handout to Yousef → Claude. Then Claude stamps the dated "Reviewed by" byline and wires the downloads live. (The first 10 are already reviewed + live.) |

## C. Watch (not Ali — handled by the autopilot)
- The **Dec 1** post-core-update ranking re-check runs automatically; no action needed.

## How results come back to the site
Anything that changes the website (sameAs URLs in A8, clinical sign-offs in B1) goes: **Ali → Yousef → Claude**, and
Claude ships it through the PR gate. Off-site items (A1–A7) are Ali's to complete directly with the owner's accounts.
