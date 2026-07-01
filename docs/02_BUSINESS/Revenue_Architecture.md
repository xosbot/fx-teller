# Revenue Architecture

**Version 1.0**
**Status:** Internal strategy document — Board of Directors grade
**Audience:** Founders, board members, current and future executives, strategic advisors, investors in diligence, AI agents

> This document sits in `02_BUSINESS/` and is read together with `00_CONTEXT/FXTeller_Master_Context.md`, `01_FOUNDATION/Vision_Mission_Values.md`, `01_FOUNDATION/Brand_Philosophy.md`, and `02_BUSINESS/Business_Model.md`. The Master Context is the governing document and takes precedence in any conflict. This document is the financial complement to the Business Model: where the Business Model describes how the company creates value, this document describes how the value is monetised — across the ecosystem, over the Member lifecycle, and through the architectural decisions that protect the philosophy while funding the long-term ambition.

---

## 1. Executive Summary

A company's revenue architecture is, in the long run, more important than its product. The product is what the company sells today; the revenue architecture is what the company is allowed to sell tomorrow. A company with a strong product and a weak revenue architecture will, in time, run out of ways to monetise the product without breaking the philosophy. A company with a strong revenue architecture and an ordinary product can iterate the product. The architecture is the harder thing to get right and the harder thing to change.

The distinction that this document is built on is the distinction between **monetisation** and **value capture**. Monetisation is the act of converting a user into a paying customer; value capture is the act of being paid for value that has been genuinely created. The two are not the same. A company that monetises without creating value is, in the long run, in the fraud business. A company that creates value without capturing it is, in the long run, in the charity business. The company's revenue architecture is the design by which value capture is allowed to follow value creation, and is not allowed to precede it.

The second distinction is between **trust and recurring revenue**. The two are not in tension in the long run; in the long run, they are the same thing. A company that protects trust compounds recurring revenue, because the recurring revenue is the result of a Member choosing, every month, to stay. A company that compromises trust can still produce recurring revenue, but the revenue is the result of friction, of switching cost, of contracts, of lock-in. The first kind of revenue is what the company is building; the second kind is what the company refuses to build.

The architecture described here is a four-tier system: Primary, Secondary, Strategic, and Future. Each tier has a different role, a different timescale, and a different test for whether a new stream belongs in it. Each tier strengthens the philosophy or it does not get included. Each tier is sized to its role — the Primary tier is the largest, the Strategic tier is the smallest, the Future tier is unbuilt but designed-for. The architecture is, in the long run, a portfolio of revenue streams, each of which compounds, and each of which is, on its own, replaceable.

The remainder of this document defines the philosophy, the tiers, the streams within each tier, the principles that govern every revenue decision, the lifecycle in which revenue is allowed to grow, the architectural role of Trading Credits, the membership model that anchors recurring revenue, the long-term revenue opportunities that the company is positioning for, the risks the architecture is exposed to, and the decision framework that holds it all together.

---

## 2. Revenue Philosophy

The company's revenue philosophy is the operating constraint on every monetisation decision. The philosophy is not aspirational; it is the test the company runs every quarter when the easier revenue is on the table.

**Revenue is the outcome of member value.** A revenue line that has not been preceded by member value is a revenue line that will not last. The company does not pursue revenue; the company pursues member value, and the revenue is the byproduct. A feature, a partnership, or a pricing change is evaluated first for whether it serves the Member, and only second for whether it produces revenue. A feature that serves the Member and produces no revenue is built; a feature that produces revenue and serves no Member is rejected.

**Trust before monetisation.** Every monetisation decision is a decision about whether to spend trust for revenue. The company's policy is that trust is not spent. A pricing change that produces revenue at the cost of trust is rejected. A partnership that produces revenue at the cost of trust is rejected. A feature that produces revenue at the cost of trust is rejected. The trust is the asset; the revenue is the byproduct. The Master Context (Section 11) names this as a Company Principle (number 5: *Protect Trust Above Revenue*). The principle is repeated here because the principle is the most-often-violated principle in any revenue-led company, and the most-often-violated principle is the principle most worth repeating.

**Long-term relationships over transactions.** A Member is a relationship; a transaction is a single point on the relationship. The company optimises for the relationship. A pricing model that maximises per-transaction revenue at the cost of the relationship is rejected. A billing model that produces churn because the friction is too high is rejected. The relationship is the asset, and the relationship is measured in years, not in sessions.

**Premium positioning.** The company is a premium product. A premium product is priced by the value the Member receives, not by the cost the company bears. A premium product is also selective about who it serves; the price filters. The company is willing to leave revenue on the table in exchange for the Members the price selects for. The Members the price selects for are, in the long run, the Members who stay, the Members who refer, the Members who make the company what it wants to be.

**Avoid maximising short-term income.** A short-term revenue decision is, by definition, a decision that the company would not make if it were planning against a five-year horizon. The company plans against a five-year horizon. A short-term revenue decision is therefore, by definition, a decision the company does not make. The decision is recorded in the Decision Log. The decision is reviewed at the one-year mark. The decision is reversed, in most cases, by the review.

The five statements are not new. They are the operating expression of the philosophy in the Master Context, the Vision-Mission-Values document, the Brand Philosophy, and the Business Model. The statements are written here because the revenue function is the function most likely, under pressure, to forget the philosophy, and the statements are the most-likely-forgotten thing in the company.

---

## 3. Revenue Architecture Overview

The company's revenue architecture is a four-tier system. Each tier has a role, a timescale, and a test. Each tier is sized to its role. Each tier is replaceable, in the sense that no single stream in any tier is the sole carrier of the tier.

**Tier 1 — Primary Revenue.** The Primary tier is the largest, the most recurring, and the most philosophically aligned. The Primary tier is the tier the company is built on. The Primary tier contains the streams that pay for the product, the Hosts, the Community, and the operating overhead of the company. The Primary tier is the steady state of the business. The Primary tier grows with Member growth, with Member tenure, and with Member upgrade within the membership model. The Primary tier is governed by the most conservative revenue principles. A stream in the Primary tier is a stream the company could, in principle, run on for a decade.

**Tier 2 — Secondary Revenue.** The Secondary tier is the smaller, more episodic, more event-driven set of revenue streams. The Secondary tier contains streams that emerge from the Primary tier: events the company hosts, workshops the company runs, retreats the company convenes, premium merchandise the company sells. The Secondary tier is a function of the Primary tier's health. The Secondary tier is allowed to grow faster than the Primary tier in a given quarter; the Secondary tier is also allowed to shrink to zero in a given quarter. The Secondary tier is governed by the same principles as the Primary tier, with the additional rule that a Secondary stream is allowed only if it does not dilute the brand the Primary tier depends on.

**Tier 3 — Strategic Revenue.** The Strategic tier is the smallest and the most deliberate. The Strategic tier contains revenue streams that are designed to fund the next phase of the company's long-term strategy. The Strategic tier is where the House of Traders, the international expansion, the publishing imprint, the institutional programmes sit. The Strategic tier is funded by the Primary and Secondary tiers and is allowed to be unprofitable in the short run in exchange for the long-term asset it is building. The Strategic tier is governed by the same principles as the Primary tier, with the additional rule that a Strategic stream is reviewed annually against its long-term thesis.

**Tier 4 — Future Revenue.** The Future tier is the unbuilt portfolio. The Future tier contains revenue streams the company is not yet operating, may operate in five to ten years, and is designing for now. The Future tier is the AI Companion, the institutional programmes, the international markets, the licensing arrangements, the marketplace. The Future tier is governed by the same principles as the Primary tier, with the additional rule that a Future stream is not built until the philosophy, the platform, and the timing are aligned.

Diversified revenue creates resilience for three reasons.

**First, no single stream can break the company.** A company whose revenue depends on a single stream is a company that has, in effect, made a single bet with the entire business. A company with diversified revenue has made many small bets. The variance of the portfolio is lower than the variance of any single stream. The company is allowed to be wrong about one stream without being finished.

**Second, the streams reinforce each other.** A Member in the Primary tier is more likely to buy a Secondary-tier workshop. A Member in a Secondary-tier workshop is more likely to upgrade in the Primary tier. A Member who attends a Strategic-tier event is more likely to advocate for the company. The streams are not independent; the streams are a system. The system is more valuable than the sum of the streams.

**Third, the streams mature at different times.** A Primary stream matures in the first two years. A Secondary stream matures in the second to fourth year. A Strategic stream matures in the third to seventh year. A Future stream matures in the fifth to tenth year. The company's revenue profile over a decade is, in this sense, a portfolio that ages. The company that builds only Primary streams is a company that has aged out of growth by year three.

---

## 4. Primary Revenue Streams

The Primary tier contains five streams. Each stream has a purpose, a relationship to the philosophy, and a Member-outcome it is built around. No prices are defined in this document; pricing is an operational decision documented elsewhere.

**Stream 1 — Hybrid Membership.** The Hybrid Membership is the company's recurring-revenue base. The model is a base subscription that gives the Member continuous access to the Trading Floor, the Community, the Library, and the standard surface of the product, plus a separate in-product unit (Trading Credits; see Section 8) that the Member can spend on premium experiences. The hybrid is the alternative to a single-tier subscription, which would either overcharge casual Members or undercharge heavy ones. The hybrid is the company's structural commitment to the long-term Member and the à la carte economy at the same time.

**Stream 2 — Trading Credits.** Trading Credits are the in-product currency. Credits are applied to premium experiences beyond the base floor: special-format sessions, single-stock deep dives, weekend workshops, in-person event seats, House of Traders access, AI Companion minutes. The Credits are the company's answer to the à la carte economy. The Member decides when and how to spend; the company is not transactional at the wrong moment. Section 8 elaborates the architecture.

**Stream 3 — Premium Experiences.** Premium Experiences are the curated, higher-touch products the company operates: deep-dive sessions, mentorship-format sessions, multi-day workshops, exclusive events. Premium Experiences are sold via Credits and, in some cases, via direct purchase. The Premium Experiences are designed to deepen the Member's relationship with the philosophy, not to broaden the company's product line. A Premium Experience that does not deepen the relationship is rejected.

**Stream 4 — House of Traders Membership.** The House of Traders Membership is the company's premium, physical-tier offering. The House Membership grants the Member access to the physical spaces, to in-person events, to small-format sessions with the Hosts, and to the social capital of being part of a smaller, more selective group. The House Membership is a privilege, not a purchase. The House Membership is priced to filter; the price is set by the value the House represents, not by the cost of running the House.

**Stream 5 — Future Digital Services.** The Future Digital Services stream is the placeholder for revenue streams the company will add as the product matures: the AI Companion, advanced analytics, written research, custom session formats. The Future Digital Services stream is unbuilt in detail. The stream exists in the architecture so that future revenue decisions have a designated tier and so that the company does not, by default, add new streams to the Primary tier in a hurry. The stream is built when the philosophy, the platform, and the timing are aligned.

The five streams are the steady state. The company plans against these five streams; the company reviews the streams quarterly; the company adds a stream to this tier only when the stream has been demonstrated to belong here.

---

## 5. Secondary Revenue Streams

The Secondary tier contains revenue streams the company may operate, may not, and is allowed to turn on and off without breaking the business. The streams are described here so the company has a vocabulary for them, not as commitments to build them.

**Events.** Curated in-person or virtual events: small-format dinners, study groups, market-debrief sessions, Fireside Chats with senior Members. Events are typically paid for in Credits or in dedicated tickets. Events are sized to the room; an event with 500 attendees is a different product from an event with 25. The company's events are smaller, not larger.

**Workshops.** Half-day or full-day workshops on specific topics: process design, risk management, trading psychology, written reflection. Workshops are paid for in Credits. Workshops are taught by Hosts, by senior Members, and by external practitioners the company has vetted.

**Trading Retreats.** Multi-day, off-site gatherings at venues chosen for calm. Retreats are designed for Members who want a concentrated period of practice, reflection, and community. Retreats are limited in size, in frequency, and in scope. A retreat is the most expensive Secondary-tier product the company operates.

**Corporate Memberships.** Membership products for small, professional teams of traders: prop desks, family offices, boutique funds. Corporate Memberships are sold selectively, to organisations whose culture is consistent with the brand. A Corporate Membership that introduces the brand to a culture that does not fit is rejected.

**Professional Certifications.** Long-form, multi-week programmes that certify a Member in a specific practice the company teaches: a process-design certification, a trading-psychology certification, a community-moderator certification. Certifications are paid for in Credits and are limited in cohort size. Certifications are not a degree and are not a credential; the company does not sell credentials.

**Premium Merchandise.** A small, limited line of physical objects: writing journals, a calendar, a print series, a member pin, a small selection of clothing. Merchandise is a brand expression, not a revenue line. Merchandise is priced to cover cost plus a small margin; the margin funds the brand, not the company.

**Private Networking Events.** Invite-only, members-only events for senior Members: small dinners, study retreats, Fireside Chats with founders. Private Networking Events are the most exclusive Secondary-tier stream and are the most carefully governed. A Private Networking Event that becomes a sales surface is rejected.

The streams are listed for the architecture; the streams are not commitments. A stream that is built is built deliberately, with a Member outcome, with a brand fit, and with an exit plan if the stream does not work.

---

## 6. Revenue Principles

The revenue function is governed by fifteen permanent principles. The principles are operational, not aspirational. A revenue decision that violates any principle is rejected.

**1. Never Monetise Trust.** Trust is the most valuable and most fragile asset the company has. A monetisation that spends trust for revenue is a monetisation the company will not run. The cost of a trust-monetisation is recorded; the alternative is not considered. *Never Monetise Trust* is the only revenue principle that overrides all others when the conflict is between the company and a Member's wellbeing.

**2. Membership Before Transactions.** The company is a membership business, not a transactional business. A pricing model that converts the relationship into a series of transactions is rejected. The relationship is the product; the transactions are a side effect.

**3. Premium Over Discounting.** The company does not run promotions, does not run discounts, does not run sales. The price is the price. A Member who pays the full price is a Member who has been filtered by the price; the company wants that filter.

**4. Reward Loyalty.** The company rewards tenure, not acquisition. A Member who has been present for five years is more valuable than a Member acquired last week, and the company's revenue architecture reflects that. Loyalty rewards are non-transactional; they are expressed as access, recognition, and invitation, not as discounts.

**5. Quality Before Scale.** A revenue stream that is below the quality bar does not scale. A revenue stream that requires the company to lower the bar to scale is rejected. The revenue architecture grows by improving the streams, not by multiplying them.

**6. Every Product Must Create Value.** A revenue stream that does not produce a Member outcome is rejected. The product comes first; the revenue is the byproduct. A pricing decision that produces revenue without producing an outcome is rejected on net.

**7. Revenue Should Never Encourage Bad Trading Behaviour.** A pricing model that incentivises more trades, more volume, more leverage, or more activity is rejected. The Master Context (Section 16) explicitly forbids encouraging overtrading. The revenue architecture is consistent with that rule. A pricing model that produces a Member outcome the brand does not want is rejected regardless of the revenue.

**8. Pricing Filters, Not Maximises.** The price is set to admit the right Members, not to maximise revenue. A price that maximises revenue is, in expectation, a price that admits Members who do not fit. The company accepts the lower revenue in exchange for the higher trust.

**9. Hybrid Beats Pure Subscription.** The Hybrid Membership (base + Credits) is the company's structural commitment. A pure subscription is rejected because it forces the company to choose between overcharging casual Members and undercharging heavy ones. The hybrid is the more honest model.

**10. Revenue Compounds Quietly.** A revenue line that spikes is, in expectation, a revenue line that the company does not have. A revenue line that compounds quietly over years is the only revenue line the company is building. Spikes are a sign of a product the company is not running well; compounding is a sign of a product the company is running well.

**11. Diversify Over Concentrate.** The company's revenue is diversified across streams, tiers, and time horizons. No single stream is the sole carrier of the company. A stream that becomes too large is reviewed; a stream that becomes dominant is reduced. The portfolio is more important than any position.

**12. Cash Discipline Beats Growth Spend.** The company is willing to grow slowly to preserve the philosophy. The company is willing to be smaller to be more disciplined. A revenue decision that requires aggressive growth spend is rejected on principle. The company is paid for the philosophy, not for the growth.

**13. Revenue Is Auditable.** Every revenue decision is recorded in the Decision Log. The decision is dated, named, and reasoned. The decision is reviewed at the next quarterly review. A revenue decision that is not in the log is a revenue decision that has not been made.

**14. International Revenue Follows Domestic Proof.** A revenue stream in a new market is built only after the equivalent stream in the home market has produced the outcome it was designed to produce. International expansion is sequenced behind proof. A revenue decision that races ahead of proof is rejected.

**15. Long-Term Members Are the Asset.** The revenue architecture exists, in the long run, to serve the long-term Member. A revenue decision that serves a short-term Member at the cost of a long-term Member is rejected. The long-term Member is the metric by which the revenue architecture is judged.

These fifteen principles are the operating constraint on the revenue function. A revenue function that operates within the principles is, in expectation, a revenue function the company can defend for a decade.

---

## 7. Revenue Lifecycle

The revenue lifecycle is the path a Member's relationship with the company takes, with the revenue implications of each stage. The lifecycle is a sequence, not a funnel: each stage compounds into the next, and the longest stage is, by design, the last.

**Stage 1 — Prospect.** A potential Member encounters the brand. The Prospect has not yet applied. Revenue implication: zero. The Prospect stage is, by design, a filter. The company does not run paid acquisition, and the Prospect is, in most cases, referred by an existing Member, a piece of long-form writing, or an in-person event. A Prospect who has not been pre-filtered by the slow channels is, in expectation, a less-aligned Prospect.

**Stage 2 — Applicant.** The Prospect applies for membership. The application is short and is itself a filter. Revenue implication: zero. The Applicant has not yet paid; the Applicant has, however, signalled intent. The company is in the position of a gatekeeper, and the gatekeeping is a brand expression.

**Stage 3 — Member.** The Applicant is approved and becomes a Member. Revenue implication: the first revenue. The Member pays the base subscription. The Member also receives an opening allocation of Trading Credits as part of the membership package. The Member is, in the first days, a high-cost-to-serve Member; the company invests in onboarding, in welcoming, in the first Floor session, in the first written introduction to the Community. The investment is recovered over the Member's tenure.

**Stage 4 — Active Member.** The Member uses the product. The Active Member attends sessions, writes process journals, engages with the Community, and begins to spend Credits on premium experiences. Revenue implication: recurring base + Credits spend. The Active Member is the most common Member state; the Active Member is also the Member whose revenue is most variable month to month. The Active Member is governed by the principles of price as filter and revenue as byproduct.

**Stage 5 — Community Contributor.** The Active Member begins to contribute: answering questions, sharing process, supporting newer Members. The Community Contributor is, in effect, a member of the staff, voluntarily. Revenue implication: stable. The Community Contributor's tenure is longer than the Active Member's; the Community Contributor's spend is more selective. The Community Contributor is the brand's quality control.

**Stage 6 — Ambassador.** The Community Contributor becomes an Ambassador: a Member who refers other potential Members, defends the brand in public, writes testimonials, represents the brand at events. Revenue implication: a multiplier. A single Ambassador referral is, structurally, the highest-quality acquisition the company has, because the referred Member arrives pre-trusting. The Ambassador is not paid for the referral; the Ambassador is rewarded with the relationship. The Ambassador's role in the revenue architecture is the role of a force multiplier, not a sales rep.

**Stage 7 — Lifetime Member.** The Ambassador becomes a Lifetime Member: a Member whose presence is, in the brand's view, the brand's most durable asset. The Lifetime Member is not a financial category; the Lifetime Member is a recognition. Revenue implication: stable, long-tenure, high-LTV. The Lifetime Member is, in the long run, the only Member the company needs to be optimising for, because the Lifetime Member is the only Member the company is, in the long run, building the company for.

Revenue grows naturally at four points in the lifecycle: at the Member stage (the first payment), at the Active Member stage (Credits spend begins), at the upgrade points within the membership model (e.g. move to Annual, move to Founding), and at the cross-tier movements (e.g. Active Member buys a workshop, Community Contributor attends a retreat). The architecture is designed so that revenue grows with tenure and with engagement, not with acquisition; the company is paid for the relationship, not the conversion.

---

## 8. Trading Credits Architecture

Trading Credits are the company's most important architectural decision. Credits are a fungible, in-product unit held by Members, applied to premium experiences beyond the base floor. Credits are the answer to a question every membership business eventually faces: how does the company sell premium experiences to a Member who is already paying for membership, without converting the relationship into a transaction?

**The philosophy behind Credits.** Credits represent participation, not gambling. The Member who spends Credits is the Member who is investing in their own development: paying for a deeper session, a longer workshop, a seat at a dinner. The Credits are not a stake on an outcome. The Credits are not a bet. The Credits are not a multiplier. The Credits are, in the brand's view, the Member's expression of intent: *I want to go deeper; here is the budget I have set for going deeper.* The Credits are the company's expression of respect: *we will not surprise you with a charge at the wrong moment; you have already paid for the moment to come.*

**Credits reduce payment friction.** A Member who is asked to pay for a workshop at the moment of the workshop is, in expectation, a Member who is friction-taxed. The friction is a tax on the Member's decision, and the tax is paid in attendance. A Member who has pre-paid via Credits is, in expectation, a Member who attends. The Credits are, in this sense, an attendance mechanism: the company is paid in advance, the Member is committed in advance, and the workshop is delivered to a room that is, in effect, already full.

**Credits unify the ecosystem.** A single Credit is, in principle, redeemable across the company's offerings: a special session, a workshop, a retreat, a House seat, an AI Companion minute, a future digital service. The unity is operational: a single in-product wallet, a single transaction history, a single balance. The unity is also psychological: the Member who holds a Credit balance is, in effect, holding a small piece of the brand; the brand's offerings are not separate purchases, they are ways of spending a single resource the Member has already committed to the brand. The Credits are, in this sense, a moat as well as a revenue line: a Member who has accumulated a Credit balance is a Member whose switching cost is the Credit balance, and the switching cost is high precisely because the Credits are valuable to the Member.

**Credits may be used across the ecosystem.** The architectural commitment is that Credits are, in principle, a single currency usable across digital, physical, events, experiences, and the future ecosystem. A Credit that is restricted to one use case is, in effect, a coupon; a Credit that is usable across the ecosystem is, in effect, a membership privilege. The company commits to keeping the currency unified as the ecosystem grows, with the operating discipline that no single use case is allowed to dominate the redemption pattern in a way that would, in effect, make the Credits a coupon for that use case.

**The psychological benefits of Credits.** The Credits produce four psychological effects the company considers load-bearing.

*First, the Credits are decoupled from the act of consumption.* A Member who buys a workshop is making a transactional decision in the moment. A Member who spends a Credit is making a pre-committed decision. The pre-commitment produces a different emotional posture: the Member is not spending; the Member is using what they have already set aside. The posture is more relaxed, more engaged, more aligned with the brand.

*Second, the Credits create a small, healthy sense of budget.* A Member who has a Credit balance is making a small budgeting decision every time the Member considers a spend. The budgeting is, in expectation, healthy: the Member is asking *is this the right use of my Credits?* The asking is the discipline the brand is teaching. The Credits are, in this sense, a training tool: the company is teaching the Member to make small, deliberate, value-aligned decisions, and the Credits are the medium of the teaching.

*Third, the Credits create a sense of belonging to the ecosystem.* A Member who holds a Credit balance is, in effect, a Member who has a stake in the brand's offerings. The Member is not a passive recipient; the Member is an active participant, and the Credits are the participation. The belonging is durable.

*Fourth, the Credits create a small, durable switching cost that is also a value.* A Member who has accumulated Credits is, in the long run, more likely to stay, not because of the switching cost, but because the Credits are a representation of the value the Member has already received from the brand. The Credits are not a lock-in; the Credits are a memory of the relationship.

The architectural commitment to Credits is one of the company's longest-standing and most distinctive decisions. The commitment is, in the long run, a commitment to a more honest relationship with the Member: the company is paid in advance, the Member is committed in advance, and the product is delivered to a room that has already chosen to be in the room.

---

## 9. Membership Philosophy

The membership model is the company's recurring-revenue anchor. The model has five levels, each with a different role, a different Member, and a different relationship to the philosophy. No prices are stated in this document; the pricing is an operational decision documented elsewhere.

**Monthly Membership.** The Monthly Membership is the entry-level tier. The Monthly Membership is the lowest commitment a Member can make to the brand, and the lowest commitment the brand can make to the Member. The Monthly Membership is the right tier for Members who are testing the product, who are uncertain about their tenure, or whose financial situation is best served by a monthly outflow. The Monthly Membership is the most common starting tier; the Monthly Membership is also the tier with the highest churn. The company optimises the Monthly Membership for early-tenure experience, not for retention at the boundary.

**Quarterly Membership.** The Quarterly Membership is a middle tier. The Quarterly Membership is for Members who are committed to a longer stay but whose financial situation does not favour an annual commitment. The Quarterly Membership is, in effect, a stepping stone between the Monthly and the Annual: a Member who has been on Monthly for a quarter is, in the brand's view, a Member who is ready to consider Quarterly. The Quarterly Membership rewards the longer commitment with a price benefit the company documents but does not market as a discount.

**Annual Membership.** The Annual Membership is the company's primary tier. The Annual Membership is the tier the brand is built around; the Annual Membership is, in expectation, the tier most Members graduate to within their first year. The Annual Membership rewards the longest commitment with the largest benefit and the most stable revenue. The Annual Membership is, in the long run, the dominant revenue line.

**Founding Members.** The Founding Members tier is a closed, limited tier reserved for the earliest Members. The Founding Members tier is a privilege, not a price point. Founding Members receive, in addition to the standard membership, lifetime recognition, an invitation to all in-person events for the life of the company, and a direct line to the founders. The Founding Members tier is offered only to Members who joined in the company's first cohort and is closed after a defined window. The Founding Members tier exists because the company believes the earliest Members deserve a different relationship with the brand, and the relationship is, in the long run, a strategic asset.

**Future Enterprise Membership.** The Enterprise Membership is a future tier, unbuilt. The Enterprise Membership is designed for small, professional teams of traders: prop desks, family offices, boutique funds. The Enterprise Membership is sequenced behind a clear product fit (the company's offerings mature enough to support team-based usage), a clear sales motion (the company has decided to operate a small sales function), and a clear brand fit (the customers the Enterprise Membership is sold to are, in expectation, aligned with the philosophy). The Enterprise Membership is, in the long run, a Strategic-tier stream that is, in this document, mentioned for completeness.

The membership model is, in the long run, the company's most important revenue stream. The model is built around tenure, around relationship, and around the philosophy that the longer a Member stays, the more value the Member receives. The model is, in this sense, the operational expression of the company's most fundamental belief: that the relationship is the product, and the relationship is measured in years.

---

## 10. Future Revenue Opportunities

The Future tier contains revenue streams the company is positioning for, may operate in five to ten years, and is designing for now. The streams are described here so the company has a vocabulary for them and so that the company is not, by default, building them in a hurry.

**House of Traders.** The House of Traders is, in this document, a Strategic-tier stream that is, in the long run, a Future-tier asset. The House generates revenue from in-person memberships, from event rentals by other premium brands, and from a small line of in-House products. The House is also an asset whose value compounds in the brand's favour even when the House is not generating revenue. The House is a long-term investment.

**International Expansion.** International markets generate revenue through local memberships, local Credits, and local events. International revenue is sequenced behind domestic proof, local regulatory clarity, and a clear Host in the local market. International revenue is a Future-tier stream because the company's first international market is not yet operational; international revenue is also, in the long run, the company's largest addressable market.

**AI Companion.** The AI Companion is a Future-tier product that may, in time, become a revenue stream. The Companion is positioned in the Master Context (Section 10) as a long-context, philosophy-aligned assistant for the Member. The Companion's revenue model is, in the long run, a Credit-denominated utility: Members spend Credits for Companion minutes, the Companion is governed by the philosophy, the Companion is explicit that it is not a signal generator. The Companion is a Future-tier stream because the Companion is not yet built.

**Professional Tools.** Professional Tools are a Future-tier product for serious traders: process journals, written-reflection tools, a long-form essay reader, a research-notes tool. The Tools are sold as a Credit-denominated subscription or as part of an Annual Membership upgrade. The Tools are a Future-tier stream because the Tools are not yet built; the Tools are a logical extension of the brand's editorial direction.

**Member Marketplace.** A Member Marketplace is a Future-tier platform for Members to buy and sell with other Members: a small publishing imprint, a curated set of services, a long-form essays collection. The Marketplace is governed by the philosophy, curated by the company, and priced to be a service to Members, not a revenue line in itself. The Marketplace is a Future-tier stream because the Marketplace requires a Member community large enough to support it.

**Business Partnerships.** Business Partnerships are a Future-tier stream: aligned, premium brands that the company partners with to provide Member benefits and to receive a small referral fee. The Partnerships are selective, are governed by the philosophy, and are reviewed annually. The Partnerships are a Future-tier stream because the Partnerships are not yet operational.

**Institutional Programs.** Institutional Programs are a Future-tier stream for institutions that want to learn from the company's philosophy: regulator briefings, university guest lectures, exchange-sponsored education. The Programs are a Future-tier stream because the Programs are not yet operational and because the Programs require the brand to be, in the public's view, the brand the Programs imply.

These seven opportunities are the company's long-term revenue position. None is committed. All are designed-for. The company is, in the long run, a company that has many small bets, each defensible, each compounding.

---

## 11. Revenue Risks

The revenue architecture is exposed to six categories of risk. Each is named, ranked, and mitigated.

**Risk 1 — Over-monetisation.** The most common failure mode of a successful membership business is to add so many revenue streams that the relationship becomes a series of transactions. The mitigation is the principle *Membership Before Transactions* (Section 6) and the explicit ceiling on the number of streams the company is willing to operate at any one time. A revenue stream that makes the relationship transactional is rejected.

**Risk 2 — Too many products.** A product line that grows faster than the philosophy can govern is a product line that has begun to dilute the brand. The mitigation is the *Quality Before Scale* principle (Section 6) and an annual review of the product line, with explicit removal of products that have fallen below the bar.

**Risk 3 — Confusing pricing.** A pricing structure that is hard to understand is a pricing structure that has begun to spend trust. The mitigation is the principle that the pricing is a filter, not a maximisation (Section 6), and a commitment to keeping the pricing structure simple enough that a new Member can understand the tiers in five minutes. A pricing change that adds complexity is rejected.

**Risk 4 — Brand dilution.** A revenue stream that is not aligned with the brand is, in effect, a tax on the brand. The mitigation is the explicit *Brand Fit* test for every new stream, the small number of Secondary-tier streams, and the annual review of the Strategic-tier streams. A stream that dilutes the brand is removed.

**Risk 5 — Low retention.** A revenue architecture that produces revenue in the first month and loses the Member in the second is an architecture that has produced a churn problem. The mitigation is the *Revenue Lifecycle* (Section 7), which optimises for tenure rather than for acquisition, and the *Reward Loyalty* principle (Section 6), which expresses revenue growth as a function of Member tenure.

**Risk 6 — Dependency on one revenue stream.** A company whose revenue depends on a single stream is a company that has, in effect, made a single bet with the entire business. The mitigation is the diversification of streams across the four tiers, with explicit attention to the size of any single stream in the portfolio. A stream that becomes too large is reviewed; a stream that becomes dominant is reduced.

The risks are not eliminable. The risks are managed by the operating system, by the cultural principles, and by the founders' commitment to the philosophy. The discipline of risk management is the discipline of staying honest about the risks, and the company is committed to that discipline.

---

## 12. Revenue Decision Framework

Every future revenue idea is run through the framework below. The framework is the operational expression of the principles in Section 6. A revenue idea that fails any question is rejected.

**Question 1 — Does this increase Member value?** A revenue idea that does not produce a Member outcome is, by definition, a revenue idea that is not yet ready. The product comes first; the revenue is the byproduct. A pricing change, a new stream, a partnership that produces revenue without producing value is rejected on net.

**Question 2 — Does this align with the philosophy?** A revenue idea that requires a contradiction with the philosophy in the Master Context, the Vision-Mission-Values, the Brand Philosophy, or the Business Model is rejected before any further analysis. The Master Context takes precedence in any conflict.

**Question 3 — Does this create dependency?** A revenue idea that produces a Member outcome the Member cannot live without is a revenue idea that has failed the brand's central test. The brand's success is measured by the *decline* in the Member's need for the product over time. A revenue idea that produces the opposite trend is rejected.

**Question 4 — Does this damage trust?** A revenue idea that the company would not want a regulator, a journalist, or a disappointed Member to read about is a revenue idea that is rejected. The trust account is the most important asset the company has, and the revenue function is its custodian.

**Question 5 — Can this scale internationally?** A revenue idea that works in India but cannot, in principle, work in Dubai is a revenue idea that has a ceiling. A revenue idea that works in both markets is a revenue idea that compounds. The international test is not a soft preference; the international test is a hard filter on the architecture.

A revenue idea that passes the five questions is a revenue idea the company is willing to consider. The consideration is then governed by the *Decision Framework* in the Vision-Mission-Values document (Section 7) and recorded in the Decision Log.

---

## 13. Conclusion

The revenue architecture exists to strengthen the ecosystem, not to exploit Members. The architecture is the operating expression of the philosophy; the philosophy is the test the architecture is held to; the test is the discipline the company is committed to.

The architecture is a four-tier system: Primary, Secondary, Strategic, Future. The Primary tier funds the company; the Secondary tier enriches the Member; the Strategic tier funds the next phase; the Future tier positions the company for the long run. Each tier has a role, a timescale, and a test. Each tier is replaceable. The architecture is, in the long run, a portfolio that compounds, and the compounding is what the company is, in the long run, selling.

The company is, in the long run, in the business of belief. The belief is that disciplined trading is a profession; the belief is that the most important product a company can offer a trader is a calm environment; the belief is that the relationship is the product, and the relationship is measured in years. The revenue architecture is the design by which the company is paid for holding the belief, and the design is the only thing the company is, in the long run, building.

Revenue exists to strengthen the ecosystem, not to exploit Members. The statement is the conclusion. The conclusion is the discipline. The discipline is the company.

---

*End of Revenue Architecture, Version 1.0.*
