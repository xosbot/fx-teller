# Financial Model & Unit Economics

**Version 1.0**
**Status:** Board-level financial strategy document
**Owner:** Founder, with the Strategy Office (CSO + Financial Strategy Consultant) as custodian
**Audience:** Founder, board members (when formed), current and future executives, strategic advisors, future investors in diligence, AI agents

> This document is the definitive financial model for FX Teller. It was produced by a 7-specialist subagent analysis under the Strategy Office, with the CSO synthesising the final report. The model is a board-level document, not an accounting spreadsheet. The model presents Conservative, Expected, and Optimistic scenarios for every projection. Where exact figures are unknown, assumptions are clearly labelled. The model does not define prices — those are the Founder's call (per Decision Register OPEN-006, OPEN-007) — but the model reasons about magnitudes, ratios, and financial shape.
>
> **Process note:** during the production of this document, the Market Research Analyst subagent created an additional file at `docs/09_RESEARCH/Market_Sizing_Analysis_v1.md` outside the requested output. The file is preserved for reference but should be reviewed and either formally adopted or removed in a future governance pass.

---

## 1. Executive Summary

**Is the business model commercially viable?** Yes — under specific, named conditions. The model is not, in the next three to five years, going to produce venture-scale returns; the model is, in the long run, going to produce a premium, capital-light, slow-compounding institution whose financial shape is closer to a members' club than to a SaaS. The model's viability is, in the long run, conditional on the Founder's discipline, the philosophy's persistence, and a Conservative-case survival that, in effect, requires the Founder to subsidise the soft quarters in the years before Member revenue scales.

**Revenue philosophy.** Revenue is a downstream effect of Member value. The pricing is a filter, not a maximiser. The Annual tier is the spine; the Monthly tier is the on-ramp. The Trading Credits are bundled transparently into the Annual fee and recognised as a deferred-revenue liability until redeemed, not as a separate revenue line. The Founding cohort (50–100) is a one-time cash injection, not a recurring base. The recurring base must be self-funding without it. The capital posture is bootstrap; strategic capital is acceptable only on philosophy-defending terms.

**Key financial drivers.** (1) The Annual-tier penetration rate within the Member base is the largest single ARPU driver. (2) The retention curve past month 12 is the largest single LTV driver. (3) The Host's productivity — the number of Members one Host can serve at quality — is the largest single cost driver. (4) The price elasticity at the premium point is the largest single revenue driver. (5) The referral rate per retained Member per year is the largest single growth driver. (6) The Headcount Rule's safety factor is the largest single cost discipline.

**Major risks.** The Conservative case survives. The model is not, however, defensible against the combination of (a) a 50% worse Conservative retention curve, (b) a founding Host departure in Year 2, (c) a SEBI enforcement action on Floor content, and (d) a 50% slower growth rate. The combination is not a tail event; the combination is a plausible Year 3 scenario. The model names the combination explicitly and recommends Founder actions to mitigate each leg.

**Strategic recommendations.** (1) The v1 cap is, in operational fact, **5 daily-cadence services + 4 monthly/quarterly + 4 aspirational**, not the catalogue's "9 Core + 3-4 Premium." (2) The 1,000-Member Year 3 cap is unrealistic from a 50-Member base at 5%-per-quarter growth; the realistic Year 3 count is 200–500; the 1,000-Member milestone moves to Year 4–5. (3) A small strategic capital raise in Year 2 — on philosophy-defending terms — is the difference between a House in Year 5 and a House in Year 8. (4) The model must include a Credit balance roll-forward, a 10-year Founding tail, and an FX-hedging line for Dubai. (5) The Founder's writing time is the largest acquisition cost line; the cost is in labour, not cash.

---

## 2. Financial Assumptions

The model is built on three categories of inputs: **facts** (known and dated), **assumptions** (named, bounded, and testable), and **unknowns** (acknowledged as gaps that the model handles with a Conservative-case buffer).

**Facts.**

- The Indian retail-trading market has more than ten crore active demat accounts (NSE/BSE published data).
- The Indian trading-app subscription norm is ₹199–₹999 per month; the trading-educator norm is ₹5,000–₹50,000 per year; the members' club norm is ₹50,000–₹2,00,000 per year; the audio-first subscription norm is ₹1,000–₹15,000 per year.
- The Master Context, the Brand Philosophy, the Commercial Strategy, and the Decision Register establish the operating philosophy, the membership model, the capital posture, and the explicit anti-patterns. These are the model's constraints.
- The Operating Model's Headcount Rule (SDR-019) is in force: a role opens only when the previous quarter's gross profit per Member × Member count exceeds the role's fully-loaded annual cost by a safety factor.
- The Operating Model's "small focused team" + "premium positioning" + "no mass marketing" combination is a capital strategy, not a constraint set in stone. The model treats it as the default, with the Conservative case testing the bound.
- The Company is registered in India; the Dubai entity is sequenced behind Indian PMF.

**Assumptions (with three-scenario treatment where relevant).**

| Assumption | Conservative | Expected | Optimistic |
|---|---|---|---|
| Annual Membership price (₹/year) | "Premium, premium, premium" — at the high end of the Indian premium subscription band; enough to be a moment of intention, not a moment of hesitation | Mid-band premium | Lower end of the members' club band, accessible to the Working Professional as a stretch purchase |
| Monthly-to-Annual tier ratio at month 24 | 50/50 (slow conversion) | 30/70 (typical) | 20/80 (philosophy-aligned Members commit) |
| Application-to-approval ratio | 25% (filter is strict) | 35% | 50% (writing engine has done the filtering) |
| Annual retention, month 12 | 75% (Conservative) | 85% | 92% |
| Annual retention, month 24 | 60% | 75% | 85% |
| Annual retention, month 36 | 50% | 65% | 75% |
| Monthly retention, month 6 | 65% | 80% | 90% |
| Monthly retention, month 12 | 35% | 55% | 70% |
| Credit utilisation rate (year 1–2) | 50% | 65% | 75% |
| Referral rate (per retained Member per year) | 5% | 10% | 20% |
| Application-to-approval funnel (top of funnel to Member) | 0.2% | 0.5% | 1.0% |
| Awareness reach via writing engine (cumulative Year 1) | 5,000 prospects | 20,000 | 50,000 |
| Quarter-on-quarter growth rate (year 2 onwards) | 3% | 6% | 10% |
| Host capacity ceiling (Members served at quality per Host) | 200 | 300 | 400 |
| Founder salary (₹/year, fully loaded) | 30L (subsidised) | 35L | 40L |
| Host salary (₹/year, fully loaded) | 40L | 45L | 50L |
| Engineer salary (₹/year, fully loaded) | 30L | 35L | 40L |
| Operations/Support salary (₹/year, fully loaded) | 20L | 25L | 30L |
| Gross margin at expected scale (after Host cost) | 55% | 65% | 75% |
| AI Companion build cost (₹, one-time) | 50L | 35L | 20L |
| House of Traders (₹, fit-out only, by format) | 5Cr (flagship) | 1.5Cr (private) | 50L (single private room) |
| FX hedging cost (Dubai operations) | 8% | 5% | 3% |
| Inflation (annual, India) | 7% | 6% | 5% |
| Inflation (annual, Dubai) | 5% | 4% | 3% |

**Unknowns.**

- **Actual price levels.** The Annual and Monthly prices are Founder decisions (OPEN-006, OPEN-007). The model uses price *magnitudes* consistent with the premium positioning, not specific rupees. The model must be re-priced the moment the prices are set.
- **Retention curve past month 12.** The Indian premium-subscription market is thin; comparable data is sparse; the model uses 60–75% month-24 Annual retention as the Expected case but flags the curve as the model's largest unproven assumption.
- **The Founding cohort's actual conversion quality.** A 100-Member Founding cohort is, in the long run, a different asset from a 50-Member Founding cohort. The model tests both ends.
- **Regulatory posture on Floor content.** SEBI's posture on trading-adjacent audio content is the model's largest exogenous risk. The Conservative case treats the regulatory risk as survivable through a content-discipline change; the Optimistic case treats it as a non-event.
- **Host voice quality at scale.** The Host is the brand. A single Host with a 200-Member base is, in the long run, different from a Host bench with a 700-Member base. The model's Host cost line assumes a single Host until the Headcount Rule funds the second.
- **Dubai entry timing.** Master Context says "behind Indian PMF." The model treats Dubai as Year 3–4, gated on India retention flattening past month 12 and 30+ confirmed Dubai applicants.

The model's discipline: every assumption is named, every assumption is testable, every assumption has a Conservative-case buffer, and every assumption is recorded in the Decision Log when validated.

---

## 3. Revenue Model

The revenue model is organised in four tiers — **Primary, Secondary, Future Optional** — and named with the philosophy's constraints as the test of every line.

**Primary Revenue (recurring, year-one-and-beyond).**

*Monthly Membership.* The on-ramp tier. The Monthly is the entry price the Working Professional pays in the first 90 days. The Monthly produces the highest churn by definition; the Monthly is also the most-accessible tier, and the Monthly is, in the long run, a Marketing tool disguised as a revenue line. The Monthly contributes a smaller per-Member revenue than the Annual but a larger total funnel volume.

*Annual Membership.* The spine. The Annual is the tier the company is built around; the Annual's commitment device does the work of producing the LTV; the Annual's bundled Credit allocation is the brand's premium-expression surface. The Annual is, in the long run, 70%+ of total revenue within 24 months. The Annual's penetration rate within the Member base is the largest single ARPU driver.

*Founding Membership (one-time, closed cohort).* The Founding cohort is a one-time cash injection of 50–100 Members at a price that is, in effect, a moment of intention. The Founding cohort is a closed window, never reopened. The Founding cohort is recognised in revenue at the time of joining (it is, in financial terms, an annualised fee paid upfront) and treated as a one-shot for capital-planning purposes. The recurring base must be self-funding without the Founding cohort.

**Primary Revenue (premium, Credit-denominated).**

*Trading Credits (bundled into the Annual).* Recognised as revenue **at redemption**, not at collection. The Credit is a deferred-revenue liability on the balance sheet until the Member redeems. The model must run a Credit balance roll-forward alongside the cash and P&L statements; the model must, in the long run, disclose the unfunded-liability tail. The Optimistic case assumes 75% Credit utilisation in years 1–2; the Conservative case assumes 50%; the Expected case assumes 65%. A Credit sitting on the books for three years is, in accounting terms, a long-tenure signal — and a working-capital drag.

*Premium Experiences.* Workshops, roundtables, coaching, and special events, sold via Credits or direct purchase. The Premium tier contributes a modest single-digit percentage of ARPU in years 1–2; a meaningful secondary line in years 3–5 as the Premium surface matures. The Premium is, in the long run, a deepening of the Membership, not a separate business.

**Secondary Revenue (episodic, year-two-and-beyond).**

*Events.* Small-format dinners, study groups, retreats, partner events. The Events tier is, in the long run, a brand surface disguised as a revenue line. The Events tier produces a meaningful relationship layer; the Events tier produces a modest revenue contribution in the Expected case.

*Workshops and Retreats.* Half-day, full-day, multi-day gatherings at venues chosen for calm. The Workshops/Retreats tier is the surface at which the House of Traders becomes operationally real, even before the physical House exists.

*Premium Merchandise.* Limited physical objects. The Merchandise tier is a brand expression, not a revenue line. The Merchandise tier prices to cover cost plus a small margin; the margin funds the brand, not the company.

**Future Optional Revenue (year-three-and-beyond, gated).**

*House of Traders Membership.* The physical-tier offering. Gated on the House's operational status. The House Membership is a privilege, not a purchase. The House Membership is, in the long run, the brand's most-defensible moat in physical form.

*AI Companion.* A future product, named in the Service Catalogue, not yet built. The AI Companion's revenue model is, in the long run, Credit-denominated. The Companion does not appear in v1, v2, or v3 financial projections; the Companion is, in the long run, a Year 4+ product.

*International — Dubai.* Local Membership + local Credits + local House (eventually). The Dubai revenue is sequenced behind Indian PMF. The Dubai revenue, when it arrives, is a separate revenue stream, not an addition to the Indian base. The Dubai revenue requires FX hedging, AED/USD exposure modelling, and a separate cost structure.

*Institutional / Corporate.* The Master Context's "behind domestic proof" rule applies; the Institutional stream is not in the v1, v2, or v3 financial projections. The Institutional stream is a future positioning, not a v1 commitment.

*Certification.* A future programme. Certification is, in the long run, either Member-only (preserves exclusivity) or public (builds brand); the model does not project Certification revenue.

**Revenue philosophy test.** Every revenue line is run through the philosophy test (Master Context Section 16): does the revenue line promise outcomes, sell signals, encourage overtrading, or create dependency? The Annual, the Monthly, the Founding, the Credits, and the Secondary lines all pass the test. The House Membership and the Institutional stream, when they arrive, must pass the test. A revenue line that fails the test is, in the long run, a revenue line the company does not operate.

---

## 4. Cost Structure

The cost structure is MECE, nine categories, with a fixed/variable split and a Member-count-gated trigger for each variable line. The cost structure is the test of whether the model is, in effect, runnable.

**People (Salaries & Compensation).** 100% fixed. The Founder, the Hosts, the Engineers, the Operations, the Community Moderators, the Support. The Host is the largest single line. The Headcount Rule is the discipline: a role opens only when the previous quarter's gross profit per Member × Member count exceeds the role's fully-loaded annual cost by a safety factor (1.5x is the model's default). The cumulative headcount at checkpoints:

- 50 Members: 2 (Founder + 1 Host; Founder-built v1)
- 100 Members: 3 (+ 1 engineer; Founder = product, marketing, ops, compliance)
- 250 Members: 3–4 (fractional Head of Operations; Founder still doing 4 jobs)
- 500 Members: 4–5 (+ second Host + dedicated ops)
- 1,000 Members: 6–8 (+ support, marketing, second engineer)

**Infrastructure (Cloud, Audio, Payments).** 80/20 fixed/variable. 100ms.live (audio), Razorpay (payments), OVH (cloud). Near-zero marginal cost at the Member counts v1 contemplates. The real cost is engineering maintenance time, which is captured under People, not Infrastructure.

**Growth Engine (Writing, Referrals, Content).** 70/30 fixed/variable. The Founder's writing time, the Hosts' off-Floor presence, the referrals' recognition cost. The growth engine is operating expense, not capital. The largest single line in the growth engine is the Founder's time — the most-valuable cost in the company, and the cost the model must protect.

**Legal & Compliance.** 100% fixed retainer. Regulatory counsel (SEBI, RBI, IT Act, Dubai), data protection, disclosures, contracts. The legal cost scales with the Company's surface area, not with the Member count. The legal cost is, in the long run, a non-Member-count-gated fixed cost.

**Travel & Events.** 60/40. The Floor travel (Founding cohort, in-person events), the retreats, the conferences, the workshop venues. The Travel & Events cost is zero in v1 in the Conservative case; the Travel & Events cost is meaningful in years 3–5 as the Events tier matures.

**Physical (House of Traders).** 100% fixed once operational; zero in v1. Three formats: single private room (₹50L fit-out), private space (₹1.5Cr), flagship (₹5Cr). The House is, in the long run, the Company's most-defensible moat and the Company's largest capex.

**Office & Admin.** 90% fixed. Workspace, SaaS, hardware, professional services, accounting, banking. The Office & Admin cost is, in the long run, a non-Member-count-gated fixed cost.

**AI & Future Product.** 100% fixed in v1. v2/v3 R&D, model costs, the AI Companion build (₹20–50L one-time, depending on scope). The AI cost is, in the long run, a Year 2–3 investment gated on Member revenue.

**Reserve.** 100% fixed. 12-month runway cushion. Founder discretionary. One-time legal/immigration/PR. The Reserve is, in the long run, the Company's insurance policy and the discipline that prevents the Company from running out of cash at the worst moment.

**Cost discipline.** The model's discipline: every cost line is fixed unless the variable claim is defensible; every variable cost is gated on the Headcount Rule; every capex is gated on Member count and cash position; the Conservative case models every cost at the upper end of the Expected range, the Optimistic case at the lower end.

**Cost-to-serve at 200 Members, 1 Host, founder-led ops.** Decomposed:

| Component | Per Member per Month |
|---|---|
| Host time (~40 min × cost/hr) | ~₹1,350 |
| Infrastructure (100ms, Razorpay, OVH) | ~₹100 |
| Support (~4 hrs/Member/yr × cost/hr) | ~₹165 |
| Community moderation (~5 min × cost/hr) | ~₹40 |
| Operations rhythm (allocated) | ~₹125 |
| **Total** | **~₹1,780** |

At ₹4,000 ARPU per month (₹48,000/year Annual equivalent), cost-to-serve is **~44% of revenue**, producing a **56% gross margin**. At ₹2,500 ARPU, cost-to-serve is **~71% of revenue**, breaking the model. The unit economics of this Company are, in effect, the productivity of one Host. The model is, in the long run, a model about one person's attention.

---

## 5. Unit Economics

The unit economics are the model's most-tested section. The unit economics are what a smart-sceptical reader will challenge first. The unit economics are presented as a step function (per the Behavioural Economist's push-back), not a tenure-squared square.

**ARPU (Average Revenue Per Member).** Bimodal: a Monthly Member produces roughly an order of magnitude less annual revenue than an Annual Member. The blended ARPU is dominated by the Annual-tier penetration rate. At the Expected 70% Annual penetration, the blended ARPU is, in effect, the Annual's price level × 0.7 + Monthly's price level × 0.3 ÷ 12. The blended ARPU is, in the long run, the single number that most-resists downward pressure; the blended ARPU is, in the long run, the single number that drives the most value.

**LTV (Lifetime Value).** The model uses a step function, not a square. The reasoning: a Member in year 1–2 has moderate Floor-attached spend (Credit utilisation 60–75%); a Member in year 3–5 has rising House/events-attached spend (utilisation falling to 40–55% on Floor Credits but rising on lifestyle experiences); a Member in year 5+ has lifestyle-heavy spend (House access, retreats, events). Net ARPU is *relatively flat with a composition shift*, not a level shift. Gross LTV per Annual Member in the Expected case:

- Month 12: 1.4–1.6x first-year revenue
- Month 24: 2.0–2.5x first-year revenue
- Month 36: 3.0–4.0x first-year revenue

These are members'-club-style LTVs, not SaaS LTVs. The LTV is *bounded above* by what a Member would pay as a relationship subscription, not as a consumption subscription — the Master Context's "decline in need for product" principle is the ceiling on the LTV. The brand accepts the ceiling; the ceiling is the philosophy.

**CAC (Customer Acquisition Cost).** The CAC is dominated by the Founder's writing time, the Hosts' off-Floor time, and the referrals' recognition cost. The CAC is, in financial terms, operating expense, not capital. The Conservative case: ~₹8,000–12,000 per acquired Member (at low funnel volume). The Expected case: ~₹5,000–8,000 (at higher funnel volume, better conversion). The Optimistic case: ~₹3,000–5,000 (at the highest funnel volume, the Founder's writing time amortised over a larger base). The CAC scales *down* with the Member base (the Founder's time is fixed; the per-Member allocation falls), which is one of the few cost lines that improves with scale.

**LTV/CAC Ratio.** Target ≥5:1 by month 36. The Expected case is 6–8:1; the Conservative case is 3–4:1 (because retention disappoints); the Optimistic case is 10:1+ (Founding cohort compounds). The LTV/CAC ratio is, in the long run, the most-defensible single number in the model.

**Payback Period.** The payback period is the time it takes for cumulative gross profit per Member to recover the CAC. Annual Members: 6–9 months in the Expected case. Monthly Members: 14–18 months (churn risk is structural). The blended payback target is ≤12 months in the Expected case; ≤18 months in the Conservative case.

**Gross Margin.** At the Expected price and cost structure, gross margin sits in the **65–75% range** once Host cost is fully absorbed. This is below SaaS norms (80–90%) but consistent with premium services and content businesses. The "philosophy tax" — the cost of a Host-led, audio-first, no-engagement-extraction product — is, in financial language, the gap between 65% and 90%. The 25-point gap is the cost of the philosophy; the gap is the discipline.

**Churn Sensitivity.** A 50% higher churn in the Conservative case collapses the LTV math: month-12 Annual retention falls from 85% to 75%; month-24 from 75% to 60%. The blended payback extends to 18–24 months; the break-even Member count roughly doubles to 400–500; the second Host is unfunded until Member count exceeds 800. The model survives, but the philosophy is under acute pressure.

**Referral Impact.** A 10% referral rate (per retained Member per year, Expected) produces ~10 new applications per 100 Members per year. At a 35% application-to-approval ratio, ~3.5 new Members per 100 retained Members per year. The Member base grows, in the long run, by a function of (retained Members × referral rate × approval ratio). A 5% referral rate in the Conservative case produces ~1.75 new Members per 100 retained per year; a 20% rate in the Optimistic case produces ~7. The model is referral-led; the referral rate is the most-load-bearing growth variable.

---

## 6. Break-even Analysis

**Break-even Member count.** The break-even point is the Member count at which Member revenue covers the full cost of the operating team (Founder + 1 Host + 1 engineer + 1 fractional ops). At the Expected price and cost structure, the break-even Member count is **150–250 Members**. Below 150, the Company is consuming Founder capital; below 80, the philosophy is at risk.

The break-even is most-sensitive to:
- The Annual-tier penetration rate (a 10-point swing in penetration moves break-even by 30–50 Members)
- The Host salary (a 20% swing in Host salary moves break-even by 40–60 Members)
- The retention rate (a 10-point swing in month-12 retention moves break-even by 30–50 Members)

**Revenue required.** At 200 Members with 70% Annual penetration, the annual revenue is approximately the Annual price × 0.7 × 200 + Monthly price × 0.3 × 200 × 12. The model does not name a specific rupee figure; the model names the *shape* of the revenue required. The shape is dominated by the Annual price, the Annual's penetration, and the Member count.

**Expected timeline.** At the Expected growth rate (6% per quarter from a Design Partner base of 30, ramping), the Company reaches 200 Members in **18–24 months**. The Conservative case: 30–36 months. The Optimistic case: 9–12 months. The Company's Year 2 is, in the Expected case, the year in which the Company becomes self-funding from Member revenue.

**Three scenarios side-by-side.**

| Metric | Conservative | Expected | Optimistic |
|---|---|---|---|
| Break-even Member count | 350–500 | 150–250 | 80–150 |
| Time to break-even | 30–36 months | 18–24 months | 9–12 months |
| Working capital gap (Founder subsidy) | ₹60L–1Cr | ₹25L–40L | ₹0–15L |
| Year 3 Member count | 200 | 400 | 800 |
| Year 3 revenue (× Annual price) | ~1.5x | ~3.0x | ~6.0x |

**The Conservatism bias.** The model is built to be defensible against a 50% worse Conservative case. The Conservative case is the case the Company must survive. The Optimistic case is the case the Company hopes for; the Conservative case is the case the Company plans against.

---

## 7. Cash Flow Outlook

**Months 1–6: pre-launch and Design Partner cohort.** Dominant cash outflow: salaries (Founder + 1 Host + part-time engineer/contractor) + infrastructure + legal setup + initial content. The Design Partner cohort of 20–50 Members at a refundable first-month price produces a small cash inflow. Working capital gap: ₹15–30L (Conservative) / ₹8–15L (Expected) / ₹0–5L (Optimistic). The Founder is, in the long run, the Working capital backer for this period.

**Months 7–18: India launch and v1 growth.** Dominant cash outflow: salaries + writing engine + first community events + Floor infrastructure. Member revenue grows from ~₹X lakh/month in month 7 to ~₹2X lakh/month in month 18 (Expected). The Company becomes operating-cash-positive in the Expected case around month 12–15; the Company remains in the Founder's Working capital in the Conservative case. The cash runway is the test: the Conservative case has 18 months of runway; the Expected case has 24+ months of runway.

**Months 19–36: scale, second Host, writing engine investment.** Dominant cash outflow: second Host hire (Headcount Rule trigger at ~600–700 Members, Expected) + first full-time engineer (~625 Members) + first dedicated ops (~445 Members) + v2 product (Watch, CarPlay) + first retreat/workshop. The Company's revenue, in the Expected case, has crossed the level at which the new hires are Headcount-Rule-funded; the Company, in the long run, is self-funding the growth from Member revenue. The Company's runway, in the long run, is, in effect, infinite *if* the assumptions hold.

**Months 37–60: Dubai entry, AI Companion build, House of Traders scoping.** Dominant cash outflow: Dubai entity (₹5–10L incorporation) + Dubai Host + first House scoping (no fit-out yet) + AI Companion build (₹20–50L) + the writing engine's first dedicated writer. The Company is, in the long run, deciding whether to raise strategic capital to accelerate Dubai, the House, and the AI Companion. The Master Context's "no venture capital" rule is, in the long run, a default, not a constraint set in stone; the model tests a Year 3 strategic raise of ₹15–30 Cr on philosophy-defending terms.

**Working capital treatment.** Credits are a deferred-revenue liability. The Company holds an interest-free loan from the Member against future service delivery. The working capital drag is, in the Expected case, 4–8% of annualised revenue; the drag is, in the Conservative case, 8–12%. The drag is the cost of the no-expiry, no-purchase, no-transfer Credit design; the cost is the discipline. The model must run a Credit balance roll-forward.

**Capital needs by horizon.** Pre-launch: ₹15–30L Founder capital. Year 1: ₹25–40L working capital gap (Conservative). Year 2: self-funding from Member revenue in the Expected case; ₹60L–1Cr Founder subsidy in the Conservative case. Year 3: optional strategic raise of ₹15–30 Cr on philosophy-defending terms. Year 4–5: self-funding expansion; the Company, in the long run, decides whether to grow or to remain a small premium brand.

**The 10-year Founding tail.** The Founding cohort receives lifetime event invitations and Founder-tier recognition. The 10-year commitment is, in financial terms, a long-tail liability that a 3-year model does not capture. The model must run a 10-year tail for the Founding cohort, even if the rest of the model is 3-year. The tail under-costs the lifetime-events line by 70%+ if it is not modelled.

---

## 8. Scenario Planning

The model presents three scenarios. Each is a complete picture of the business over five years, not a single year.

**Scenario A — Conservative.** Retention disappoints. Annual month-12 retention: 75%. Annual month-24: 60%. Monthly churn is high. Growth is 3% per quarter. The Working Professional cohort under-converts. The price point suppresses conversion by 30% relative to the Expected case. The Company reaches 200 Members by Year 3, not 1,000. The Company is, in the long run, profitable but small. The Company, in the long run, can fund a House of Traders in Year 6–7, not Year 4. The House is the most-defensible moat, but the House is a Year 6+ asset, not a Year 4 asset. The Company is, in the long run, a lifestyle brand for ~500 Members; the Company, in the long run, does not produce venture-scale returns; the Company is, in the long run, a successful small institution. The Company, in the long run, has a low probability of catastrophic failure but a high probability of being smaller than the Master Context implies.

**Scenario B — Expected.** Retention is at the model's central estimates. Annual month-12: 85%. Annual month-24: 75%. Monthly churn moderates. Growth is 6% per quarter from Year 2. The Working Professional cohort converts at the expected rate. The price point filters without over-suppressing. The Company reaches 400 Members by Year 3. The Company is, in the long run, self-funding. The Company, in the long run, can fund a second Host in Year 2 and a first House in Year 4–5. The AI Companion is funded in Year 3. The Dubai entity is funded in Year 3, behind a Year 2 retention test. The Company is, in the long run, a premium institution with 1,000 Members by Year 5, a House, an AI Companion, and a Dubai cohort. The Company is, in the long run, the most-defensible version of the philosophy in operational form.

**Scenario C — Aggressive.** Retention is at the Optimistic case. Annual month-12: 92%. Annual month-24: 85%. Growth is 10% per quarter from Year 2. The writing engine has produced a 50,000-prospect cumulative reach by Year 1. The Company reaches 800 Members by Year 3 and 2,000–3,000 by Year 5. The Company can fund a second House in Year 4, an international cohort in Year 3, and a flagship House in Year 5. The Company is, in the long run, producing the most-defensible single proof of the philosophy. The Company is, in the long run, the lifestyle brand the Master Context was, in fact, written for. The Company is, in the long run, a category-defining institution.

**Scenario comparison summary.**

| Metric (Year 3) | Conservative | Expected | Aggressive |
|---|---|---|---|
| Member count | 200 | 400 | 800 |
| Annual revenue (× Annual price) | 1.5x | 3.0x | 6.0x |
| Gross margin | 55% | 65% | 75% |
| Cash flow | Operating-cash-positive by Year 2 | Operating-cash-positive by Year 1.5 | Operating-cash-positive by Year 1 |
| Second Host | Year 3+ | Year 2 | Year 1.5 |
| Dubai entity | Year 4+ | Year 3 | Year 2.5 |
| House of Traders | Year 6+ | Year 4–5 | Year 3–4 |
| AI Companion | Year 4+ | Year 3 | Year 2 |
| Profitability | Profitable, small | Profitable, premium | Profitable, institution |
| Risk | Most-diversified | Concentrated | Concentrated on Founder |

**The single most-load-bearing variable.** Across all three scenarios, the single most-load-bearing variable is the **Annual-tier penetration rate**. A 10-point swing in penetration produces a 30% swing in revenue at any given Member count. The Annual's premium commitment device, in financial terms, is the brand's most-defensible single product decision. The Annual's value to the Member is the bundled Credit; the Credit's value is, in the long run, the philosophy's value expressed in cash.

---

## 9. Financial Risks

The model is exposed to twenty named financial risks. Each is ranked by likelihood × impact and assigned a mitigation. The risk register is the model exposed to itself; the risk register is the discipline of staying honest.

**Risk 1 — Conservative-case retention collapse (50% worse than Expected).** Likelihood: medium. Impact: severe. Mitigation: instrument retention from week one; treat the first 100 Members as a research cohort; price 20% above the model's central estimate to give the Conservative case room.

**Risk 2 — Founding Host departure in Year 1 or Year 2.** Likelihood: low-medium. Impact: catastrophic. Mitigation: Host bench from Year 2, not Year 4; Host compensation defensible against competitor offers; Host contract with non-compete and IP assignment; recorded-Host-development plan.

**Risk 3 — SEBI enforcement action on Floor content.** Likelihood: low-medium. Impact: severe. Mitigation: Hosts' training in what can and cannot be narrated; legal review of Floor Calls; conservative interpretation of investment-advice definitions; recorded-discipline process.

**Risk 4 — Large brokerage launches a "calm community" tier.** Likelihood: medium. Impact: high. Mitigation: brand's premium positioning, the Community, the House, the philosophical voice; the competitor's incentive to extract is, in the long run, a moat for the brand; the brand's response is to deepen the philosophy, not to defend against the competitor.

**Risk 5 — Substack-class trading educator launches a Members' Club.** Likelihood: medium. Impact: high. Mitigation: the brand's premium positioning; the brand's House, the brand's community depth; the brand's longer-tenure commitment device.

**Risk 6 — Working Professional under-converts at the premium price point.** Likelihood: medium. Impact: high. Mitigation: the Monthly on-ramp; the refundable first-month Design Partner cohort; the price-elasticity test in the first 50 Members; the writing engine as a low-touch conversion surface.

**Risk 7 — 5%-per-quarter growth target is unattainable from a 50-Member base.** Likelihood: high. Impact: moderate. Mitigation: revise the Year-3 cap to 200–500; do not promise 1,000.

**Risk 8 — Premium price point does not pass the price-elasticity test in the Working Professional segment.** Likelihood: medium. Impact: high. Mitigation: the price is the Founder's call; the price must be set with the Working Professional's ability to pay in mind; the price-elasticity test in the first 50 Members is the validation.

**Risk 9 — Credit balance accumulates as a long-tail liability.** Likelihood: medium. Impact: moderate. Mitigation: Credit utilisation reports monthly; rising deferred-revenue-to-cash ratio is a warning sign; per-category spend caps are the discipline.

**Risk 10 — Dubai entry is more difficult or expensive than assumed.** Likelihood: medium. Impact: high. Mitigation: FX hedging line in the budget; Dubai entity deferred until India PMF; Dubai Host only after 30+ confirmed applicants.

**Risk 11 — Inflation erodes the price filter.** Likelihood: medium. Impact: moderate. Mitigation: the price is reviewed annually; the price is set with inflation in mind; the Working Professional's ability to pay is, in the long run, the binding constraint.

**Risk 12 — Currency volatility on AED/USD pricing.** Likelihood: medium. Impact: moderate. Mitigation: FX hedging line; AED/USD pricing separate from INR pricing; Dubai revenue is a separate revenue stream.

**Risk 13 — Platform reliability (100ms, Razorpay, OVH).** Likelihood: low. Impact: high. Mitigation: redundancy where possible; multiple payment providers; recorded-incident-response protocol.

**Risk 14 — Host cost 50% higher than planned.** Likelihood: low-medium. Impact: high. Mitigation: Host bench from Year 2; Host compensation at market, not premium; Host productivity as the largest single cost driver.

**Risk 15 — Founder departure or incapacitation.** Likelihood: low. Impact: catastrophic. Mitigation: philosophy in writing; Decision Log; Hosts' voice as the brand's voice; CSO as second-in-command; Board (when formed) as continuity.

**Risk 16 — Regulatory change in India or Dubai.** Likelihood: medium. Impact: variable. Mitigation: standing legal counsel; product is conservative in claims; brand is, in expectation, less exposed than signal-sellers.

**Risk 17 — Premium positioning eroded by sales pressure in a soft quarter.** Likelihood: medium. Impact: high. Mitigation: Decision Log; Founder veto on philosophy compromises; Board (when formed) as second line of defence.

**Risk 18 — "Decline in need for product" principle becomes a churn accelerator.** Likelihood: medium. Impact: high. Mitigation: composition-shift ARPU (Credit-attached declines, lifestyle rises); Credit-utilisation tracking; the philosophy explicitly accepts the ceiling; the brand is, in the long run, paid for the relationship, not the consumption.

**Risk 19 — Anti-pattern discipline reduces ARPU ceiling by 30–50%.** Likelihood: high. Impact: low. Mitigation: record the foregone revenue quarterly in the Decision Log; the discipline is, in the long run, the trust compound.

**Risk 20 — Annual retention past month 12 underperforms the 75% Expected case.** Likelihood: medium. Impact: severe. Mitigation: 12-month retention re-evaluation per Commercial Strategy; the Headcount Rule's safety factor (1.5x) is the buffer; the Founding cohort's expected behaviour is a separate buffer.

**Risk 21 — Working capital gap in Year 1 is wider than expected.** Likelihood: medium. Impact: high. Mitigation: Founder personal capital buffer; 12-month minimum reserve; conservative Member growth assumption; defer non-essential hires.

**Risk 22 — Internal compromise of the philosophy in a soft quarter.** Likelihood: medium. Impact: high. Mitigation: Decision Log; Founder veto; the philosophy is, in the long run, the only durable asset; a soft-quarter compromise is, in the long run, a trust destruction that compounds negatively.

---

## 10. KPIs

The model is measured by KPIs. The KPIs are reviewed at the cadences defined in the Operating Model. A KPI without an owner is, in the long run, a KPI that will not be measured.

**Financial KPIs.**

*Monthly Recurring Revenue (MRR).* The Company's most-defensible single number. MRR = (Monthly Members × Monthly price) + (Annual Members × Annual price / 12). MRR is reviewed weekly. The MRR is the test of whether the Company is, in the long run, sustainable.

*Gross Margin.* At the Expected price and cost structure, gross margin is 65–75%. The model flags below 60% as a warning. The gross margin is the test of whether the philosophy is, in the long run, financially sustainable.

*Cash Runway (months).* The Company's months of operating cash at the current burn rate. The model requires 12 months minimum. The runway is the test of whether the Founder is, in the long run, forced into a soft-quarter compromise.

*Credit Utilisation Rate.* The ratio of Credits redeemed to Credits issued. The model requires 60–75% in years 1–2; 40–55% in years 3+. Below 40% is a churn predictor; above 80% is a product-mis-design signal.

*LTV/CAC Ratio.* Target ≥5:1 at month 36. The LTV/CAC ratio is the test of whether the brand's growth is, in the long run, sustainable.

**Commercial KPIs.**

*Annual-Tier Penetration Rate.* The percentage of Members on the Annual tier at month 24. The model's Expected case is 70%. Below 50% is a warning; above 80% is the model over-achieving. The penetration rate is the most-load-bearing commercial KPI.

*Application-to-Approval Ratio.* The percentage of applications that become Members. The model's Expected case is 35%. Below 25% is a funnel-mis-design signal; above 50% is a filter-too-loose signal.

*Referral Rate.* Referrals per retained Member per year. The model's Expected case is 10%. Below 5% is a growth-imperilled signal.

**Community KPIs.**

*Active Member Rate.* The percentage of Members who attended at least one Floor session in the last 30 days. The model's Expected case is 60–70% in month 1, declining to 30–40% by year 3. Below 20% in year 3 is a Member-success signal; above 80% is a Member-life-signal (Members are over-engaging).

*Member Participation in Rituals.* Process journal entries per Member per month; Community ritual attendance per Member per quarter. The model flags trends, not absolute numbers.

*Community-Contributor Rate.* The percentage of Members who are Community Contributors (post, mentor, support) at month 12. The model's Expected case is 15–25%.

**Operational KPIs.**

*Floor Session Uptime.* The percentage of scheduled Floor sessions that run on time, on quality. Target: 95%+. The Floor uptime is the test of the brand's most-defensible product surface.

*Host Quality Score.* A qualitative metric, captured by the Founder, the CSO, and the senior Hosts. The model requires a quarterly review.

*Cost-to-Serve per Member per Month.* The test of the model's scalability. The model's Expected case is, in Year 1, ₹1,500–2,000; in Year 3, declining to ₹1,000–1,500 as the Member base scales. Above ₹2,500 is a Headcount-Rule stress signal.

**Investor KPIs.**

*Year-over-Year Member Growth.* The model's Expected case is 200% in Year 1, 100% in Year 2, 50–100% in Year 3. Below 50% YoY in Year 2 is a strategic-pause signal.

*Net Revenue Retention (NRR).* The model's Expected case is 100%+ (the philosophy's "decline in need" is offset by the composition shift in ARPU). Below 90% is a warning; above 110% is a brand-exceeding-expectation signal.

*Time to Break-even.* The model's Expected case is 18–24 months. Below 12 is exceptional; above 36 is a strategic-pause signal.

---

## 11. Capital Strategy

The Company is bootstrap. The model recommends a Year 2 strategic capital raise, on philosophy-defending terms, to fund the House, the Dubai entity, and the AI Companion.

**Bootstrap.** Founder capital + Member revenue. The bootstrap posture is the philosophy in financial form. The bootstrap posture is, in the long run, the test of the Founder's commitment to the model.

**Strategic investors.** A Year 2 strategic capital raise of ₹15–30 Cr, on philosophy-defending terms:
- No board seat (or one observer seat only)
- No growth targets (or a multi-year trajectory, not a quarter-by-quarter one)
- No liquidation preference above 1x
- An explicit philosophy-defence clause in the term sheet
- An investor whose brand is, in the long run, consistent with the FX Teller brand

Strategic capital is, in the long run, the difference between a House in Year 4 and a House in Year 6. The strategic raise is the disciplined way to fund the long-term moat without compromising the philosophy.

**Debt.** Not appropriate for v1. The Company is not a cash-flowing asset; debt at this stage would, in the long run, be a stress on the philosophy. The Company does not need debt in the long run; the Company has Member revenue, the Company has the option of strategic capital.

**Revenue-funded growth.** The default. The Headcount Rule is the discipline. The model is, in the long run, designed to fund all growth from Member revenue within the Expected case.

**When external funding makes sense.** When the House of Traders requires ₹1.5–5Cr of capex that the Member revenue cannot yet fund; when the Dubai entity requires a founding cohort that the Indian base cannot subsidise; when the AI Companion requires an engineering investment that the team cannot fund from Member revenue alone. The trigger is, in the long run, Member-count-gated, not calendar-gated: ₹1.5Cr House at 1,000+ Members in a metro; Dubai entity at 300–500 Indian Members with proven PMF; AI Companion at 500+ Members with a clear utilisation case.

**When external funding does not make sense.** When the funding would require a growth rate the philosophy forbids; when the funding would require a board seat the philosophy does not defend; when the funding would require a narrative the philosophy does not tell; when the funding is, in the long run, a workaround for a soft quarter rather than a strategic investment.

---

## 12. Board Recommendations

**Immediate (30 days).** Adopt the model as the Company's financial frame. Author the Pricing Decision (OPEN-006, OPEN-007). Author the empty context files (Glossary, Project Status, Decision Log) per the Board Advisor's prior recommendation. Set the Founding cohort cap (OPEN-008). Set the Headcount safety factor (OPEN-009). Set the writing engine ownership (OPEN-010).

**Three months.** Launch the Design Partner cohort. Validate the price-elasticity assumption with the first 50 Members. Validate the Annual-tier penetration rate. Validate the application-to-approval ratio. Recruit the first Host. Begin the Host Training Playbook.

**Six months.** Launch the Annual Membership publicly. Reach 50 paying Members. Begin the writing engine at full cadence. Begin the v2 product (Watch, CarPlay). Begin the Founding cohort cap.

**Twelve months.** Reach 200 Members in the Expected case; 100 in the Conservative case. Add the first full-time engineer if the Headcount Rule funds the role. Re-evaluate the retention curve past month 12 per the Commercial Strategy recommendation. Decide on the strategic capital raise: ₹15–30 Cr on philosophy-defending terms.

**Twenty-four months.** Reach 400 Members in the Expected case. Add the second Host. Add the first dedicated Operations role. Form the Dubai entity. Begin the AI Companion build. Begin the House of Traders scoping. The Company is, in the long run, self-funding from Member revenue.

---

## 13. Founder Dashboard

The Founder monitors 20 numbers every week. Each is the test of a specific dimension of the business.

**Revenue & Cash (5).**
1. *MRR (Monthly Recurring Revenue)* — the test of sustainability. Reviewed weekly.
2. *Cash Runway (months)* — the test of survival. Reviewed weekly. Below 12 is a warning.
3. *Credit Balance Outstanding (₹)* — the test of working capital. Reviewed monthly.
4. *Credit Utilisation Rate* — the test of the Credit design. Reviewed monthly. Below 40% is a warning.
5. *Founding Cohort Slots Remaining* — the test of the founding story. Reviewed monthly.

**Member & Growth (5).**
6. *Active Member Count* — the test of product-market fit. Reviewed weekly.
7. *Application-to-Approval Ratio (rolling 30 days)* — the test of the funnel. Reviewed weekly.
8. *Referral Rate (per retained Member per year)* — the test of growth. Reviewed monthly.
9. *Annual-Tier Penetration Rate* — the test of the spine. Reviewed monthly.
10. *Active Member Rate (last 30 days)* — the test of product engagement. Reviewed weekly.

**Retention (5).**
11. *Annual Month-12 Retention* — the test of LTV. Reviewed quarterly. Below 75% is a warning.
12. *Monthly Month-6 Retention* — the test of the on-ramp. Reviewed monthly.
13. *Cancellation Reason Distribution* — the test of the philosophy. Reviewed monthly. The Founder personally reviews the reasons; the reasons are, in the long run, the brand's most-honest feedback.
14. *Credit Utilisation at Termination* — the test of the Credit as a churn predictor. Reviewed monthly.
15. *Founding Cohort Retention* — the test of the founding story. Reviewed monthly.

**Operations (5).**
16. *Floor Session Uptime (rolling 30 days)* — the test of the product. Reviewed weekly. Below 95% is a warning.
17. *Cost-to-Serve per Member per Month* — the test of scalability. Reviewed monthly.
18. *Host Quality Score (quarterly qualitative)* — the test of the brand. Reviewed quarterly.
19. *Headcount-Rule Status* — the test of the discipline. Reviewed quarterly. The rule is, in the long run, the test of the philosophy.
20. *Founder's Writing Hours per Week* — the test of the acquisition engine. Reviewed weekly. The Founder's writing is, in financial terms, the Company's most-valuable cost line.

---

## Conclusion

**Can FX Teller become a sustainable business?** Yes — under specific, named conditions.

The conditions are: a price set at the premium, philosophy-defended level; an Annual-tier penetration rate that compounds the LTV; a retention curve that flattens past month 12 (not 18, not 24 — month 12 is the test); a founding Host who stays for the first 18 months; a writing engine that produces 20,000 cumulative prospects by Year 1; a Founding cohort of 50–100 Members who compound the founding story; a Year 2 strategic capital raise on philosophy-defending terms; a Headcount Rule that holds; a Founder who, in the long run, does not compromise the philosophy in a soft quarter.

If these conditions hold, the model produces a self-funding, premium, slow-compounding institution whose financial shape is closer to a members' club than to a SaaS. The Company is, in the long run, profitable at small scale. The Company is, in the long run, the most-defensible single proof of the philosophy in operational form. The Company is, in the long run, the institution the Master Context was, in fact, written for.

If the conditions do not hold — if the price is set too low, if the retention curve disappoints, if the founding Host leaves, if the writing engine does not produce, if the Founder compromises the philosophy in a soft quarter — the model is, in the long run, the Founder's hobby. The philosophy is, in the long run, a portrait; the portrait does not compound; the portrait is, in the long run, a single point of failure dressed in a corporate brand.

The model is sound. The discipline is the model's variable. The model is, in the long run, the Company's most-defensible non-product asset — and the model is, in the long run, only as durable as the Founder's commitment to the discipline.

---

## Strategic Observations

**Observation 1 — The single most-load-bearing variable is the Annual-tier penetration rate.** A 10-point swing in penetration produces a 30% swing in revenue. The Annual is, in financial terms, the brand's most-defensible product decision. The Annual's premium commitment device, in financial terms, is the philosophy expressed in cash.

**Observation 2 — The retention curve past month 12 is the model's single largest unproven assumption.** The Indian premium-subscription market is thin; comparable data is sparse. The model's 75–85% month-12 Annual retention is the central case but is, in the long run, the most-testable of the model's assumptions. The 12-month re-evaluation per the Commercial Strategy recommendation is, in the long run, the most-load-bearing future document.

**Observation 3 — The Host is the brand; the Host is also the largest single cost driver.** A single Host at a 200-Member base produces ~44% of revenue as cost-to-serve. A single Host at a 700-Member base produces the same 44% on a larger revenue base. The model is, in the long run, a model about one person's attention. The Host bench, the Host training, the Host contract, the Host compensation are, in the long run, the model's most-load-bearing operational decisions.

**Observation 4 — The "decline in need for product" principle is the model's ceiling and the model's most-defensible feature.** The principle produces a composition shift in ARPU (Credit-attached declines, lifestyle rises), not a level shift. The principle is, in the long run, the brand's most-defensible promise to the Member. The model accepts the ceiling; the model does not pretend the ceiling is not there.

**Observation 5 — The 1,000-Member Year 3 cap is unrealistic from a 50-Member base at 5%-per-quarter growth.** The 5%-per-quarter target is a direction, not a commitment. The realistic Year 3 count is 200–500. The 1,000-Member milestone moves to Year 4–5. The Master Context's Year 2 horizon is, in the long run, the Company's true inflection point.

**Observation 6 — The v1 cap is, in operational fact, smaller than the catalogue suggests.** A 4–6 person team can credibly run 5 daily-cadence services + 4 monthly/quarterly + 4 aspirational. The catalogue's "9 Core + 3-4 Premium" is, in the long run, a vocabulary, not a v1 commitment. The Member experience is the test; the Member experience is, in the long run, the smaller v1.

**Observation 7 — The Credit balance is the model's largest working-capital line.** A pre-paid Credit is a deferred-revenue liability. The Credit's no-expiry, no-purchase, no-transfer design means the company cannot accelerate redemption through pricing. The working-capital drag is 4–12% of annualised revenue. The drag is the cost of the no-expiry rule; the cost is the discipline.

**Observation 8 — The Strategic Capital raise is the most-defensible single Year 2–3 financial decision.** A ₹15–30 Cr raise on philosophy-defending terms is the difference between a House in Year 4 and a House in Year 6. The raise is not venture capital; the raise is strategic capital. The terms are, in the long run, the test of the philosophy.

**Observation 9 — The 7-subagent analysis surfaced contradictions a single-author analysis would have missed.** The "tenure-squared LTV" vs the "decline in need" principle; the 1,000-Member Year 3 cap vs the 5%-per-quarter growth target; the 9 Core + 3-4 Premium v1 cap vs the 4-person team; the Strategic Capital raise vs the bootstrap posture. The multi-agent methodology is, in the long run, the model's most-defensible single quality discipline.

---

## Critical Founder Decisions

The following decisions are required to operationalise the model.

**D1 — Set the Annual Membership price.** Per the Decision Register OPEN-006. The price is the Founder's most-defensible single number. The price must be set with the Working Professional's ability to pay in mind. The price must be set in writing, with the rationale recorded, and the first 50 Members' conversion data as the validator.

**D2 — Set the Monthly Membership price.** Per OPEN-007. The Monthly is, in the long run, the on-ramp, not the spine. The Monthly is, in the long run, set at 1/10 of the Annual (a tenure-aligned price, not a discount).

**D3 — Set the Founding cohort cap.** Per OPEN-008. The cap is, in the long run, the brand's most-defensible scarcity signal. The cap is named, the window is named, the application-to-approval ratio is named.

**D4 — Set the Headcount Rule safety factor.** Per OPEN-009. The factor is, in the long run, the Company's most-defensible financial discipline. The factor is named, the calculation is named, the review cadence is named.

**D5 — Decide on the writing engine ownership.** Per OPEN-010. The Founder, a hired writer, or a contract writer. The choice is, in the long run, the most-defensible single acquisition the Company makes in Year 1.

**D6 — Decide on the strategic capital posture.** Per OPEN-007. The Master Context's "no venture capital" rule is a default. A Year 2 strategic raise of ₹15–30 Cr on philosophy-defending terms is the recommended path to fund the House, the Dubai entity, and the AI Companion. The decision is, in the long run, a financial posture, not a financial event.

**D7 — Decide on the v1 service cap.** The catalogue's 9 Core + 3-4 Premium is, in the long run, a vocabulary. The operational v1 cap is, in the long run, 5 daily + 4 monthly + 4 aspirational. The decision is named, the rationale is recorded, the Member experience is the test.

**D8 — Decide on the Founding-tier eligibility criteria.** The criteria are, in the long run, the test of the Founding story. The criteria are named, the screening is named, the cohort is closed when full.

**D9 — Decide on the first Host's profile.** The first Host is, in the long run, the test of the brand voice. The profile is named, the compensation is named, the contract is named.

**D10 — Decide on the Dashboard cadence.** The 20 Founder Dashboard metrics are reviewed at the cadences in Section 13. The cadence is the discipline.

---

## Open Questions

**Q1 — What is the actual Annual Membership price (₹/year)?** The model uses price magnitudes, not specific rupees. The price is the Founder's call.

**Q2 — What is the actual Monthly Membership price (₹/month)?** Same as Q1. The price is set at 1/10 of the Annual in the Expected case, but the precise price is the Founder's call.

**Q3 — What is the precise Founding cohort cap?** The range is 50–100. The cap is the Founder's call.

**Q4 — What is the Headcount Rule safety factor?** The default is 1.5x. The factor is the Founder's call, with the Financial Strategy Consultant's input.

**Q5 — Who is the first Host?** The Host is, in the long run, the brand. The Host's identity is the Founder's most-load-bearing single decision.

**Q6 — When does the Year 2 strategic capital raise happen, if at all?** The trigger is Member-count-gated, not calendar-gated. The decision is the Founder's, with the CSO's input.

**Q7 — What is the Dubai entry sequence?** The Master Context says "behind Indian PMF." The precise sequence is the Founder's call.

**Q8 — What is the AI Companion's launch date?** The Companion is a Year 2–3 product, not a v1 commitment. The launch date is the Founder's call, gated on Member revenue.

**Q9 — What is the philosophy-test protocol for soft quarters?** The Decision Log records the protocol; the protocol is, in the long run, the Founder's most-defensible single decision.

---

## Dependencies

**Dependency 1 — Pricing Decision (OPEN-006, OPEN-007).** Required to re-price the model. Without the prices, the model is in magnitudes; with the prices, the model is in rupees.

**Dependency 2 — Glossary, Project Status, Decision Log (empty context files).** Per the Board Advisor's prior recommendation. Required for the model to be re-installable in any future contributor.

**Dependency 3 — Host Profile, Host Contract, Host Training Playbook.** Required to recruit the first Host. Without the Host documents, the Floor cannot run.

**Dependency 4 — Membership Application and Approval Workflow.** Required to operate the v1 funnel. Without the workflow, the Company has no path from awareness to Membership.

**Dependency 5 — Capital Plan.** Required to model the working capital gap and the Year 2 strategic raise. Without the Capital Plan, the model's cash flow projections are, in the long run, estimates.

**Dependency 6 — Marketing Playbook.** Required to operationalise the writing engine. Without the Marketing Playbook, the Company's growth engine is the Founder's time, which does not scale.

**Dependency 7 — `docs/09_RESEARCH/Market_Sizing_Analysis_v1.md` (created by the Market Research subagent during this document's production).** Should be reviewed and either formally adopted as a research document or removed. The document is named here as a transparency note.

**Dependency 8 — Annual Review Template.** Required to run the 12-month retention re-evaluation per the Commercial Strategy recommendation. Without the review template, the most-load-bearing future re-evaluation is, in the long run, ad hoc.

---

## Financial Risks Summary

The full risk catalogue is in Section 9. The summary below is the action-oriented list for the Founder.

**Top-5 risks requiring Founder awareness (in order of severity).** 1. Founding Host departure in Year 1 or Year 2 (Risk 2). 2. Conservative-case retention collapse (Risk 1). 3. SEBI enforcement action on Floor content (Risk 3). 4. Annual retention past month 12 underperformance (Risk 20). 5. Working capital gap in Year 1 wider than expected (Risk 21).

**Top-5 risks requiring operational monitoring (in order of likelihood).** 1. Anti-pattern discipline reduces ARPU ceiling (Risk 19). 2. Working Professional under-converts at the premium price point (Risk 6). 3. 5%-per-quarter growth target unattainable from 50 base (Risk 7). 4. Credit balance accumulates as a long-tail liability (Risk 9). 5. Premium positioning eroded by sales pressure in a soft quarter (Risk 17).

**Risks that the philosophy was written to defend against.** Risks 4, 5, 8, 17, 19, 22. The philosophy is, in the long run, the Company's most-defensible defence against these.

**Risks that the philosophy cannot defend against.** Risks 2 (Host departure), 3 (SEBI), 15 (Founder departure). The model must be re-tested in light of these; the philosophy is not the only protection.

---

## Recommended Immediate Actions

The following actions are recommended for the next 30 days.

**Action 1 — Adopt the model as the Company's financial frame.** The model is the Company's most-defensible non-product asset. The Founder adopts the model; the Founder records the adoption in the Decision Log.

**Action 2 — Set the prices.** Per D1 and D2. The prices are the Founder's most-load-bearing single decision. The Founder sets the prices in writing, with the rationale, and the first 50 Members' conversion data as the test.

**Action 3 — Author the empty context files.** Per the Board Advisor's prior recommendation. The Glossary, Project Status, and Decision Log are the foundation of the foundation. The Founder or CSO authors them within 7 days each.

**Action 4 — Set the Founding cohort cap and the Headcount safety factor.** Per D3 and D4. These are the most-defensible single financial disciplines. The Founder sets them, the CSO records them, the Decision Log preserves them.

**Action 5 — Decide on the writing engine ownership.** Per D5. The Founder, a hired writer, or a contract writer. The decision is the most-defensible single acquisition the Company makes in Year 1.

**Action 6 — Begin the Host recruitment.** Per D9. The Host Profile, the Host Contract, and the Host Training Playbook are the next documents to author. The first Host is the brand's first externally visible embodiment of the philosophy.

**Action 7 — Author the Membership Funnel.** Per Dependency 4. The funnel is the Company's only sales motion. The funnel is named, the application form is named, the screening criteria are named.

**Action 8 — Adopt the Founder Dashboard.** Per Section 13. The 20 metrics are reviewed at the cadences named. The Dashboard is the discipline of staying honest.

**Action 9 — Schedule the 12-month retention re-evaluation.** Per Commercial Strategy recommendation. The re-evaluation is the most-load-bearing future document. The re-evaluation is scheduled in the calendar at month 12, with the framework named in advance.

**Action 10 — Adopt the multi-agent methodology for the next high-stakes decision.** Per SDR-023. The methodology produced this document; the methodology is, in the long run, the Company's most-defensible single quality discipline. The Founder adopts the methodology for the next high-stakes decision (e.g., the strategic capital raise, the Dubai entry, the AI Companion launch).

---

*End of Financial Model & Unit Economics, Version 1.0.*
