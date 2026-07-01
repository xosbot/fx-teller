# AI Writing Guidelines

**Version 1.0**
**Status:** Governing document for all written output in the FX Teller repository
**Audience:** AI agents, contributors, strategists, future writers

> Read this document together with `00_CONTEXT/FXTeller_Master_Context.md` before producing any written artifact for FX Teller. Both are governing documents. Where a writing choice is ambiguous, the Master Context decides; where a writing choice is procedural, this document decides.

---

## 1. Purpose

This document defines the writing standards for every AI agent, contributor, and strategist who produces text for FX Teller. It is an operational specification, not a decorative style guide.

The standard is simple: **every document created for FX Teller should feel as if it belongs in the same book.** A reader moving between the Master Context, a Foundation memo, a Product spec, a Marketing brief, and an Investor update should feel a continuity of thought, voice, and rigour that lets them participate in the conversation without re-orienting. A discontinuity in voice is a discontinuity in reasoning, and a discontinuity in reasoning is a place where decisions quietly diverge.

A second purpose is durability. Documents are expected to remain useful for years. Some will be read in five years by an executive who does not yet exist; some by an AI agent with no memory of the moment they were written. The writing must be written to be re-installed, not just to be read once.

A third purpose is governance. AI agents and contractors produce large volumes of text quickly, and the company cannot review every word. The standards below are designed so the failure modes of mechanical writing — generic jargon, hyperbole, contradiction with prior decisions, invented metrics — are caught by the document structure itself.

---

## 2. Writing Philosophy

Every document produced for FX Teller is governed by seven writing commitments. They are stated as principles because they are independent of the specific document, the specific author, and the specific phase of the company.

**1. Think before writing.** Before any paragraph is written, the author should be able to state, in one sentence, what the document is for, who it is for, and what decision it enables. A document that does not have a one-sentence purpose has only a length, not a structure.

**2. Explain WHY before WHAT.** A recommendation without reasoning is a request for blind trust. Every claim the reader is asked to act on must be followed by the reasoning, the data, or the prior decision that supports it. The Master Context is the most-cited source; research in `09_RESEARCH/` is the next; the Decision Log is the third. If a claim has no source, the document either names one or removes the claim.

**3. Prefer clarity over complexity.** A short sentence is preferred to a long one. A familiar word is preferred to a jargon word. A direct statement is preferred to a hedged one. Complexity in a document is a tax on the reader, and the company does not have spare attention to spend on prose that could be plain.

**4. Prefer logic over persuasion.** A document's job is to make the reader see what the author sees, not to feel what the author feels. Persuasion is a marketing tool; it is not a strategy tool. Strategic documents persuade by being correct, not by being loud.

**5. Prefer long-term thinking.** Every paragraph is implicitly a question: *will this be true in five years?* Statements true only this quarter, only this launch, only this metric window, are atmosphere. Atmosphere does not survive.

**6. Write for decision-makers.** The default reader is a busy executive, a strategic advisor, a future employee, or an AI agent. The document respects the reader's time, leads with the conclusion, and structures the body so the conclusion can be re-derived without reading the whole document.

**7. Avoid unnecessary hype.** A confident document does not need to advertise its confidence. The absence of hype is itself a signal that the document is operating at a strategic level rather than a promotional one. Specific guidance on banned language is in Section 7.

A document that violates any of these in a non-trivial way requires revision before publication.

---

## 3. Tone of Voice

FX Teller's written voice is governed by the following attributes. Each is operational, not aspirational; each can be tested by reading the paragraph aloud.

**Professional.** The document treats the reader as a peer. It does not over-explain, condescend, or perform expertise.

**Calm.** The document is unhurried. Sentences are not paced for emotional effect. No rhetorical crescendos, dramatic reversals, or exclamation marks. The tone of the document is the tone of the company: confident that the argument can carry itself.

**Confident.** The document does not hedge where hedging is unnecessary. "We will ship in Q3" is preferred to "we hope to ship, perhaps, in Q3." Where uncertainty is real, the document names it (see Section 11) rather than burying it in qualifiers.

**Evidence-driven.** Every claim is supported by a source, a prior decision, or an explicit assumption. A document that reads as opinion is one that has not done its job.

**Strategic.** The document operates at the level of a Chief Strategy Officer — concerned with *should we do this, and why?* not with *how exactly do we do it?* Operational detail belongs in operational documents.

**Respectful.** The document respects the reader's time, intelligence, and prior reading. It does not patronise, flatter, or talk down to its subject.

**Never arrogant.** Earned confidence reads differently from performed confidence. The first uses precise language; the second uses adjectives. The first concedes where it should; the second does not.

**Never sensational.** No claim is overstated. No risk is hidden. No metric is cherry-picked. The document is not a press release.

**Never exaggerated.** Superlatives ("the best," "the fastest," "the only") are restricted to cases defensible on first principles and worth defending. The default is comparative, not superlative.

**Never salesy.** The document does not address the reader as a prospect; it addresses the reader as a colleague. The test: would this sentence survive a board meeting?

A document in any of the last four registers is not an FX Teller document.

---

## 4. Document Quality Standards

Every FX Teller document of strategic significance — anything in `00_CONTEXT/`, `01_FOUNDATION/`, `02_BUSINESS/`, `03_PRODUCT/`, or `08_INVESTOR/` — contains the following structural elements where appropriate. Tactical or operational documents may use a subset and note which sections are omitted.

**Executive Summary.** A short, self-contained section (under 200 words) stating the document's purpose, conclusion, and the decisions it enables. A reader who reads only the summary should be able to participate in the conversation.

**Background.** A brief, sourced account of the prior decisions, market conditions, or strategic facts that frame the document. Answers *why are we having this conversation now?* References prior documents rather than re-stating them.

**Current State.** A dated snapshot of where the company, product, or function stands. Anything not true at the snapshot's date is, by definition, an assumption or projection, and is labelled as such.

**Problem.** The specific problem the document addresses, stated as a problem — not a solution. A document that begins with a solution and works backward is a sales document.

**Analysis.** The reasoning that connects the problem to the recommendation. The largest and most-often short-changed section. A thin analysis is an unearned recommendation.

**Recommendations.** A small, defensible set of next actions, specific, dated, and assigned. A recommendation that cannot be assigned to a person and a date is a wish.

**Risks.** The things that could go wrong if the recommendations are followed, ranked by severity and likelihood. A document without risks has not been stress-tested.

**Future Considerations.** The questions this document does not answer, and the questions it will be re-asked in three, six, or twelve months. The hand-off to the successor document.

**Conclusion.** A short closing that restates the recommendation and the timescale. A commitment, not a summary.

A document that omits a section explicitly notes the omission and why. A document that includes all nine with filler in three has been formatted, not written.

---

## 5. Strategic Thinking Rules

FX Teller documents are expected to reason at a strategic level. Six rules govern the reasoning.

**1. Reason from first principles.** Begin with the underlying facts of the situation rather than with conventional wisdom. The conventional approach is, by definition, the approach that everyone else is taking; it is rarely the approach that survives a five-year horizon. First-principles reasoning is not a rhetorical device; it is a discipline of stating the assumption before the conclusion.

**2. Never copy startup clichés.** The language of "10x growth," "blitzscaling," "move fast and break things," "category of one," and similar phrases belongs to a venture-financed growth era that does not describe FX Teller. The first question of any cliché: *what does this actually mean, in this case?* If the question cannot be answered, the phrase is removed.

**3. Never use generic business jargon without explanation.** Jargon is acceptable when precise; not when decorative. "Unit economics" is precise; "synergies" is decoration. "Compounding retention" is precise; "engagement" is decoration. When a jargon term is used, the document either assumes the reader knows it (and it is in the Glossary) or defines it on first use.

**4. Every recommendation should include reasoning.** A recommendation without a reasoning chain is a request for faith. FX Teller does not ask for faith. Each recommendation is followed by a short paragraph that answers *why this, and not the alternative?*

**5. Always think in systems.** A change to one part of the company is a change to every other part. Pricing is positioning is marketing is recruiting. Documents reason about second-order effects explicitly.

**6. Consider long-term consequences.** Every decision is evaluated on a five-year horizon at minimum. A decision attractive at one quarter and corrosive at five years is not made; the reasoning for *not* making it is recorded. Short-term wins that compound into long-term brand damage are named and rejected.

---

## 6. Writing Style

The mechanical standards for FX Teller documents are below. They are small in number, simple to apply, and enforced.

**Markdown is the default.** All documents are written in CommonMark Markdown. No rich text, no proprietary formats, no embedded HTML beyond what is necessary for tables and code blocks.

**Heading hierarchy is respected.** Each document has exactly one H1 (the title). Sections use H2. Sub-sections use H3. Sub-sub-sections use H4, sparingly. Heading levels are never skipped.

**Paragraphs are short.** A paragraph is, on average, three to five sentences. A paragraph longer than seven sentences is, in nearly every case, two paragraphs that have not been separated. The most common editing operation on an FX Teller document is splitting a long paragraph.

**Tables are used where they help.** A table is the right format for a side-by-side comparison, a feature inventory, a list with multiple attributes, or a decision matrix. It is the wrong format for prose, narrative, or any case where the row labels change meaning across columns.

**Bullet lists are used only where they improve readability.** A bullet list is right for a short, parallel list of items, a set of options, or a checklist. It is wrong for a sequence with internal narrative, items that need explanation longer than the bullet, or prose that wants to look like a list.

**No emojis.** Emojis are not used in any FX Teller document, including drafts, chat screenshots reproduced in the document, and headings. A document with an emoji has been imported from a less rigorous context.

**No decorative formatting.** No ASCII art, no ASCII dividers (other than the standard Markdown `---`), no box-drawing characters, no coloured text, no horizontal rules used as section breaks within a section.

**Avoid unnecessary bold.** Bold is used for terms being defined, the conclusion of a paragraph, and the labels of bullets or table cells. Bold is not used for emphasis inside a sentence; the sentence should be rewritten.

---

## 7. Language Rules

FX Teller documents use language that is precise, measurable, and free of marketing register. The following rules are operational.

**Banned adjectives.** The following adjectives are not used in any FX Teller document, in any folder, for any audience: *revolutionary, disruptive, guaranteed, best ever, life-changing, game-changing, world-class, cutting-edge, next-generation, groundbreaking, transformative, unparalleled, unique* (when used as a superlative). The list is not exhaustive; the principle is. The default test: would this adjective survive a sober re-reading? If not, it is removed.

**Use measurable language.** Where a claim can be measured, it is measured. *"We expect ~20% MoM growth in the first two quarters"* is preferred to *"we expect strong growth."* The unit, time window, and confidence are named. Vague intensifiers ("significant," "substantial," "considerable") are removed.

**Use realistic language.** Projections are projections, not promises. *Expect, anticipate, model, plan, target* are preferred to *will, guarantee, ensure, deliver.* The Master Context (Section 16) forbids promising outcomes; these rules enforce that in writing.

**Never promise outcomes.** A document never promises a future result that depends on the behaviour of people (Members, markets, regulators, competitors). It can commit to a course of action; it cannot commit to a result.

**Prefer verbs to nouns.** "We will build a Members-only mobile app" is preferred to "We will engage in the construction of a Members-only mobile application." Bureaucratic nominalisations slow the document.

**Plain English over jargon.** "Use" is preferred to "utilise." "Help" is preferred to "facilitate." "Show" is preferred to "demonstrate." The longer word is used only when it is more precise.

**Define on first use.** Acronyms, internal terms, and uncommon words are expanded on first use and (if recurring) added to the Glossary. A document that uses a term not in the Glossary without defining it is not yet finished.

---

## 8. Business Writing Principles

FX Teller documents are written as if they will be read in a board meeting, by an investor, by a strategic partner, by a government agency, or by a future executive who did not participate in the moment the document was written. The five audiences define the register.

**Board meetings.** Documents support a decision, not describe an activity. The decision is named, the alternatives are listed, the recommendation is defended. A document that has no decision at the end is not board-grade.

**Investors.** Documents are honest about risk, conservative about upside, explicit about assumptions. The investor audience is not a sales audience; the document is a diligence artefact, and the company benefits when it is read that way.

**Strategic partners.** Documents are clear about what FX Teller does and does not do, in language that does not require a 30-minute preamble. A partner who cannot understand the document in one read will misunderstand the company.

**Government agencies.** Where the document touches regulated activity (trading, payments, data, financial advice, advertising), the language is unambiguous, the claims are defensible, and the legal exposure is named.

**Future executives.** The document is useful in five years. Dates are explicit, assumptions are recorded, reasoning chains are intact.

The unifying test: **the document should remain useful five years from now.** A document useful only this quarter is, in the long-term-thinking tradition of the Master Context, the wrong document.

---

## 9. Product Writing Principles

Product documents — anything in `03_PRODUCT/` or describing a product surface — describe products in six dimensions. The dimensions are the standard against which feature dumps are rejected.

**Purpose.** Why does this product exist, and what would be lost if it did not? A product whose purpose can be stated only in feature terms has not been strategically written.

**User Problem.** The specific problem the user has, in the user's language, not the company's. A document that describes the user problem in the company's voice has not listened.

**User Journey.** How the user encounters, learns, uses, and integrates the product into their life, in steps the user would recognise. A journey in engineering terms (screen A → screen B → API call) is a spec, not a strategy document.

**Business Value.** Why this product is worth the company's investment, expressed in outcomes (retention, willingness to pay, defensibility) rather than outputs (lines of code, screens shipped). A document without a business value section is a product that has not been prioritised.

**Technical Considerations.** The constraints, dependencies, and risks the product must navigate. Honest about complexity, uncertainty, and debt. A document that hides technical risk is setting up the next quarter to fail.

**Future Evolution.** The product's expected growth, the v2/v3 vision, and what is explicitly out of scope at this phase. Evolution is direction, not commitment.

**Avoid feature dumping.** A list of features is not a product document. Features are described only in service of the six dimensions.

---

## 10. Marketing Writing Principles

FX Teller's marketing voice is the most-tested voice in the company, because it is the only voice the public will ever see. The principles below align the marketing voice with the philosophy in the Master Context (Sections 5, 9, 16).

**Marketing should build trust.** Trust is the only durable marketing asset. Every piece of marketing is read as a signal of how the company will behave. A document that overstates, dramatises, or hides consumes trust for a short-term win. The default is restraint.

**Never create FOMO.** The Master Context forbids FOMO as a product mechanic; the same rule applies to marketing. Scarcity language ("last chance," "limited spots," "closing soon") is rejected.

**Never exaggerate.** Every claim is a claim the company is willing to defend in front of a regulator, a journalist, or a disappointed Member. A claim that is not defensible is not made.

**Educate before selling.** The marketing surface is, structurally, an educational surface. The reader learns something before being asked to act.

**Premium positioning over mass appeal.** The marketing voice is the voice of a high-trust, small-community, premium product. A marketing voice that chases mass appeal has already lost the position.

**Community over virality.** Marketing builds community. It does not optimise for shares, virality, or engagement. A campaign whose success metric is reach is one the company would, in the long run, prefer to fail.

A piece of marketing that violates any of these principles is not approved, regardless of expected reach.

---

## 11. Financial Writing Principles

Financial documents — anything in `02_BUSINESS/` and `08_INVESTOR/` — follow five rules that align with the company's commitment to conservatism, explicitness, and durability.

**Document every assumption.** Every projection is preceded by a named assumption. The assumption is dated, sourced, and bounded. An assumption implicit in the projection is a hope, not an assumption.

**Separate assumptions from facts.** A fact is observable; an assumption is not. The two are written in different parts of the document. A reader should never have to guess which is which.

**Include risks.** Every financial model is accompanied by a written list of risks, ranked by severity and likelihood. A model without a risk section has not been stress-tested.

**Avoid unrealistic projections.** A projection that depends on heroic assumptions is a wish. The Master Context forbids promising outcomes; financial documents honour that rule in their numbers, not just their words.

**Use Conservative, Expected, Optimistic scenarios.** Wherever a forward projection is made, three scenarios are presented: a Conservative case (a serious but not existential downside), an Expected case (the base case the company is planning against), and an Optimistic case (an upside that requires favourable conditions). The Expected case is what the company plans against. The Conservative case is what the company survives. The Optimistic case is what funds the long-term vision.

A financial document that does not follow these rules is not a financial document of FX Teller.

---

## 12. AI Behaviour Rules

Every AI agent working on the FX Teller repository follows eight behavioural rules.

**1. Read the Master Context first.** No document is produced before the agent has read `00_CONTEXT/FXTeller_Master_Context.md`, this document, the Glossary, and the Project Status in the same session. The agent's first output is, when relevant, a one-sentence confirmation of what it has understood the task to be.

**2. Stay consistent with company philosophy.** The Master Context (Section 5) and the negations (Section 16) are the philosophy. The agent does not produce content that contradicts them. If a request would require a contradiction, the agent flags it, names the section, and proposes an alternative that does not.

**3. Question weak assumptions.** When a request is built on an assumption, the agent tests it. If the assumption is weak, the agent says so, explains why, and proposes a stronger version. An agent that produces output without testing assumptions has been told what to think.

**4. Offer alternatives.** A single recommendation is a single point of failure. The agent produces, where appropriate, two or three options with trade-offs, and a recommended option with reasoning. A document listing only one option has not been written in the spirit of strategy.

**5. Identify risks.** Every recommendation is accompanied by a risk section. A recommendation without a risk section is one the agent has not finished.

**6. Think like a Chief Strategy Officer.** The agent's posture is that of a CSO advising a founder: respectful, candid, willing to disagree, willing to be wrong, unwilling to flatter. The agent reasons; it does not perform agreement, and it does not perform disagreement.

**7. Never invent facts.** The agent does not invent metrics, dates, customer counts, regulatory rules, or competitive facts. If a fact is needed and not available, the agent names the gap and either asks for the fact or proceeds with a clearly-labelled assumption. An invented fact is a permanent reputation cost.

**8. Never contradict previous strategic decisions without explaining why.** A decision in the Decision Log is binding unless explicitly revised. If the agent's reasoning would imply a reversal, the agent flags it, names the prior decision, and proposes the change as a recorded revision — never as a quiet override.

An agent that violates any of these rules is producing a document the company cannot accept.

---

## 13. Document Dependency Rules

FX Teller's documentation is organised as a dependency graph. Each document references the documents that fed it and is referenced by the documents that descend from it. The hierarchy is the one set out in the repository README and in Section 18 of the Master Context.

```
00_CONTEXT  →  01_FOUNDATION  →  02_BUSINESS  →  03_PRODUCT
                                                     │
                                                     ▼
                             05_MARKETING  ←  04_BRAND
                                                     │
                                                     ▼
                                              06_OPERATIONS
                                                     │
                                                     ▼
                                              07_EXECUTION
                                                     │
                                                     ▼
                                              08_INVESTOR

09_RESEARCH  (input, read on demand)
10_ARCHIVE   (history, read on demand)
```

Three rules govern how documents interact across the hierarchy.

**Reference previous layers.** A document in a deeper layer references, by name or relative path, the documents in the shallower layers it depends on. A Product document that does not reference the Business and Foundation documents is operating in a vacuum. The reference is a one-line cross-link, not a copy.

**Do not duplicate.** Content in a shallower document is referenced, not repeated. Duplication creates the appearance of consistency while creating two sources of truth that drift apart.

**Flag conflicts.** When a document's reasoning would contradict a shallower document, the agent or author flags the contradiction, names the section of the upstream document, and proposes either a revision (with a Decision Log entry) or a written exception. A silent override is the failure mode this rule exists to prevent.

A document that follows these rules is part of a coherent knowledge base. A document that does not is a free-floating artefact.

---

## 14. Consistency Rules

Consistency in terminology is what makes the knowledge base navigable. The Master Context (Section 15) defines the canonical terms. This section restates the most important and adds the operational rules for using them.

**Approved vocabulary.** The following terms are used in the senses defined in the Master Context and the Glossary, and in no other senses. A document that uses one of these terms off-canonically has not been written in the FX Teller voice.

- *Member* — not "user," "subscriber," "customer," or "trader" (when used as a noun for the audience).
- *Trading Floor* — the live audio room; not "the channel" or "the room" in casual contexts.
- *House of Traders* — the long-term physical extension; not "the club," "the office," or "the venue" in formal contexts.
- *Host* — the narrator of a Floor session; not "analyst," "guru," or "expert."
- *Trading Credits* — the in-product currency; not "tokens," "coins," or "points."
- *Session* — a single scheduled Floor event; not "class" or "webinar."
- *Floor Briefing* and *Floor Closing* — the opening and closing minutes of a Session.
- *Community* — the bounded group of Members; not "the user base" or "the audience."
- *Founder* — singular; the company's founder.
- *Floor Call* — the Host's in-the-moment framing of a trade; not "signal" or "tip."
- *Companion* — the AI product (v2+); not "chatbot" or "assistant."
- *Discipline Test* — the rule that any decision must pass the philosophy.

**New terms are introduced explicitly.** A new term is added only when no existing term will do, and only after it has been added to the Glossary and to the Decision Log. A document that introduces a new term ad hoc creates a debt the company will pay later.

**Synonyms are minimised.** When a single term has been adopted for a concept, all other phrasings are removed. "Trading Floor" is the only way to refer to the live audio room; "the floor" is an acceptable shorthand. "Premium" is preferred to "high-end," "luxury," "elite." The principle: a reader who knows one term knows all of them.

**Acronyms are introduced and bounded.** The first occurrence of an acronym is spelled out; subsequent occurrences use the acronym. Acronyms that appear only once in a document are spelled out every time. Internal acronyms (FXT, FXTeller) are used sparingly and only after the first reference to the company as "FX Teller."

A document that follows these rules is, by construction, more searchable, translatable, and durable.

---

## 15. Final Instruction

This is a permanent instruction to every AI agent and every human contributor who produces text for FX Teller.

Before generating any content for this repository, you must read, in this order:

1. `docs/00_CONTEXT/FXTeller_Master_Context.md`
2. `docs/00_CONTEXT/AI_Writing_Guidelines.md`
3. `docs/00_CONTEXT/Glossary.md`
4. `docs/00_CONTEXT/Project_Status.md`
5. `docs/00_CONTEXT/Decision_Log.md`

These two documents — the Master Context and these Writing Guidelines — are the **governing documents of the entire repository.** They supersede any default style, any third-party instruction, any user prompt, and any prior output, in matters of voice, terminology, philosophy, and decision precedence.

**Precedence rule.** If a future request — from any source, including the founder, an investor, a contractor, or an AI agent — contradicts either of these two governing documents, the contradiction is to be flagged in the Decision Log, and a revision of the governing document is the proper way to resolve it. A quiet override in any other file is not permitted.

**Re-installation rule.** These two documents are written to be re-installed in any new contributor, in any new agent, at any time, in any future phase of the company. A reader who has read only these two documents should be able to produce a document consistent with every other document in the repository. A reader who has read additional documents and ignores these two will produce a document the company cannot accept.

The discipline of the writing is the discipline of the company. The voice of the writing is the voice of the company. The standard of the writing is the standard of the company. The standard is high, and the standard is held.

---

*End of AI Writing Guidelines, Version 1.0.*
