# FX Teller — Knowledge Base

This directory is the **single source of truth** for the FX Teller Strategy Office. Every strategic, business, product, brand, and operational document in this repository lives here.

The workspace is organised as a numbered pipeline. The number prefix is a **dependency hint**: lower numbers feed higher numbers. Read top-down on first contact, then jump straight to the folder you need.

---

## Documentation hierarchy

| # | Folder | Purpose | Stage |
|---|--------|---------|-------|
| 00 | `00_CONTEXT/` | Master context, writing rules, project status, glossary, decision log. **Read first.** | Meta |
| 01 | `01_FOUNDATION/` | Mission, vision, values, long-term thesis. The "why we exist" layer. | Strategy |
| 02 | `02_BUSINESS/` | Business model, pricing, unit economics, revenue streams, moat. | Strategy |
| 03 | `03_PRODUCT/` | Product strategy, feature spec, roadmap, technical architecture notes. | Strategy → Build |
| 04 | `04_BRAND/` | Brand identity, voice, tone, visual system, naming. | Identity |
| 05 | `05_MARKETING/` | Positioning, messaging, channels, content strategy, growth loops. | Go-to-market |
| 06 | `06_OPERATIONS/` | Customer support, success, legal/compliance, internal processes. | Run |
| 07 | `07_EXECUTION/` | Sprint plans, weekly OKRs, task backlogs, decision records in motion. | Build |
| 08 | `08_INVESTOR/` | Pitch deck, financial model, cap table narrative, investor updates. | External |
| 09 | `09_RESEARCH/` | Active research material, references, technical specs, market studies. | Input |
| 10 | `10_ARCHIVE/` | Superseded or historical documents. Frozen, do not edit. | History |

---

## Purpose of every folder

### `00_CONTEXT/`
The control room. Five files every contributor and AI agent must consult before writing anything else:
- `FXTeller_Master_Context.md` — one-page brief of who we are, what we ship, who it is for.
- `AI_Writing_Guidelines.md` — voice, tone, formatting, banned phrases, length rules.
- `Project_Status.md` — current phase, last milestone, next milestone, blockers.
- `Glossary.md` — canonical definitions of every internal term.
- `Decision_Log.md` — append-only log of strategic decisions with date and rationale.

### `01_FOUNDATION/`
Strategic bedrock. Mission, vision, values, north-star thesis, founding story. Changes here ripple through everything else and should be rare and deliberate.

### `02_BUSINESS/`
The commercial engine. Business model canvas, pricing tiers, unit economics, LTV/CAC assumptions, revenue mix, competitive moat. This is what the investor folder summarises and what the product folder builds toward.

### `03_PRODUCT/`
What we ship. Product principles, feature inventory, roadmap, v1/v2/v3 scope, user journeys, technical architecture references. Lives alongside, not inside, the application source code.

### `04_BRAND/`
How we look and sound. Brand identity, voice and tone guide, visual tokens, naming conventions, logo usage. Feeds `05_MARKETING/`.

### `05_MARKETING/`
How we reach people. Positioning, messaging matrix, channel strategy, content calendar, SEO/GEO plan, growth loops, launch playbooks.

### `06_OPERATIONS/`
How the company runs day-to-day. Support playbook, customer success flows, legal posture, compliance (SEBI/RBI considerations, Razorpay, data handling), internal rituals.

### `07_EXECUTION/`
The moving parts. Sprint plans, weekly OKRs, current-quarter scorecard, in-flight decisions, task breakdowns. Highest churn rate; refreshed often.

### `08_INVESTOR/`
External-facing strategy. Pitch deck, executive summary, financial model assumptions, cap table narrative, investor update template.

### `09_RESEARCH/`
Live reference material. The pre-existing technical documents (`ARCHITECTURE.md`, `DEPLOY.md`, `RUNBOOK.md`) live here, alongside market research, competitor teardowns, user interviews, regulatory notes.

### `10_ARCHIVE/`
Frozen history. The phase-1 proposal (`proposal-phase1.html`, `proposal-phase1.pdf`) lives here. Documents in this folder are read-only references; do not edit or delete.

---

## Naming convention

- **Folders** are zero-padded two-digit numbers followed by a SCREAMING_SNAKE_CASE label: `00_CONTEXT`, `01_FOUNDATION`, …
- **Files** use `PascalCase_With_Underscores.md` and carry a descriptive name, not a version number in the filename (versioning lives in git).
- **One concept, one file.** If a file grows past ~500 lines, split it.
- **Dates** in filenames (e.g. `2026-07-01_investor-update.md`) are allowed only for time-bound artefacts: investor updates, sprint reviews, decision log entries.
- **Prefixes** are reserved: `TODO_` (planned but unwritten), `DRAFT_` (in review), `ARCHIVED_` (deprecated mirror of an active file).

---

## Writing convention

1. **Lead with the conclusion.** First paragraph states the takeaway; supporting detail follows.
2. **One audience per file.** Specify it at the top: `> Audience: founders / engineering / investors / marketing / customer support`.
3. **Plain English.** Short sentences, active voice, no marketing fluff.
4. **No invented numbers.** Every metric, date, or claim links to a source in `09_RESEARCH/` or a decision in `Decision_Log.md`.
5. **Link, don't duplicate.** Reference other docs by relative path; never copy their content.
6. **Update the decision log.** Any change to strategy, pricing, or scope must be reflected in `00_CONTEXT/Decision_Log.md`.
7. **No application source code in this folder.** Engineering artefacts belong in `apps/`, `packages/`, `infra/`. This folder is prose, diagrams, and references.

For tone, voice, and formatting specifics, see `00_CONTEXT/AI_Writing_Guidelines.md`.

---

## Document dependency order

Read in this order on first contact. Each step builds on the previous.

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

**In one sentence:** *Context → Why we exist → How we make money → What we ship → How it looks → How we market it → How we run it → What we are doing this week → What we tell investors.*

---

## Maintenance rules

- Every new strategy document lands in the lowest-numbered folder that matches its purpose.
- Cross-link aggressively; never duplicate.
- When a document is superseded, move it to `10_ARCHIVE/` with a `ARCHIVED_` prefix and a one-line note in `00_CONTEXT/Decision_Log.md`.
- When in doubt, ask: *would a new contributor need this to understand the company on day one?* If yes, it belongs in `00_CONTEXT` or `01_FOUNDATION`. If no, it belongs deeper in the tree.
