# FX Teller

**A members' club for serious retail traders in India.** Live audio trading floors, expert-hosted sessions, and a community built for traders who treat the markets as a craft — not a casino.

## Repository Overview

This is a monorepo housing two distinct but connected bodies of work:

| Area | Description |
|------|-------------|
| **Product** (`apps/`, `packages/`, `infra/`) | The live product platform — NestJS backend, host console (Next.js), mobile app (React Native + Expo), marketing website |
| **Strategy** (`docs/`) | The complete strategic knowledge base — 30+ documents defining the company's philosophy, business model, product, brand, operations, and execution plans |

## Quick Start

```bash
pnpm install

# Start backend + web locally
docker compose -f infra/docker-compose.yml up -d db api web

# Run mobile (separate terminal)
cd apps/mobile && pnpm dev
```

## Product Stack

| Layer | Choice |
|-------|--------|
| Mobile | Expo (React Native), EAS Build |
| Live audio | 100ms |
| Auth | Phone OTP (in-app), Firebase optional |
| Payments | Razorpay (UPI / Card / Netbanking) |
| Trade call UI | Android: floating overlay (custom Kotlin module) · iOS: in-app full-screen modal |
| Backend | NestJS on OVH VPS, Docker Compose |
| Database | PostgreSQL 16 |
| Reverse proxy | SWAG (nginx + Let's Encrypt + fail2ban) |

## Strategic Knowledge Base (`docs/`)

The `docs/` folder contains the full strategic architecture of FX Teller. It is organised as a numbered pipeline — the lower the number, the more foundational the document.

```
docs/
├── 00_CONTEXT/          Master context, glossary, writing guidelines
├── 01_FOUNDATION/       Vision, mission, values, brand philosophy
├── 02_BUSINESS/         Business model, revenue, pricing, unit economics
├── 03_PRODUCT/          Product ecosystem, member experience, service catalogue
├── 04_BRAND/            Brand voice, visual identity (in progress)
├── 05_MARKETING/        Customer personas, go-to-market playbook
├── 06_OPERATIONS/       Operating model, delivery blueprint
├── 07_EXECUTION/        6-month plan, 24-month strategic roadmap
├── 08_INVESTOR/         Pitch deck, financial model (in progress)
├── 09_RESEARCH/         Architecture docs, market sizing, runbooks
├── 10_ARCHIVE/          Historical documents (phase 1 proposal)
├── 98_STRATEGY_OFFICE/  10 specialist roles + 4 collaboration frameworks
│   └── 99_GOVERNANCE/   Strategic decision register (24 closed + 10 open decisions)
└── README.md            Knowledge base entry point
```

### Key Documents

- **Strategic Blueprint** — [`STRATEGIC_BLUEPRINT.md`](STRATEGIC_BLUEPRINT.md). The master synthesis of all strategy documents. Start here.
- **Master Context** — [`docs/00_CONTEXT/FXTeller_Master_Context.md`](docs/00_CONTEXT/FXTeller_Master_Context.md). The company's core philosophy. The governing document.
- **6-Month Execution Plan** — [`docs/07_EXECUTION/6_Month_Execution_Plan.md`](docs/07_EXECUTION/6_Month_Execution_Plan.md). Week-by-week plan for the first 6 months.
- **Strategic Decision Register** — [`docs/99_GOVERNANCE/Strategic_Decision_Register.md`](docs/99_GOVERNANCE/Strategic_Decision_Register.md). Every material decision, recorded and maintained.
- **Pricing & Commercial Strategy** — [`docs/02_BUSINESS/Commercial_Strategy_&_Pricing_Psychology.md`](docs/02_BUSINESS/Commercial_Strategy_&_Pricing_Psychology.md).
- **Go-To-Market Playbook** — [`docs/05_MARKETING/Go_To_Market_&_Brand_Launch_Playbook.md`](docs/05_MARKETING/Go_To_Market_&_Brand_Launch_Playbook.md).
- **Product Ecosystem** — [`docs/03_PRODUCT/Product_Ecosystem.md`](docs/03_PRODUCT/Product_Ecosystem.md).

### Reading Order

New contributors should read in this order:
1. `STRATEGIC_BLUEPRINT.md` — the one-page strategic synthesis
2. `docs/00_CONTEXT/FXTeller_Master_Context.md` — core philosophy
3. `docs/00_CONTEXT/AI_Writing_Guidelines.md` — writing standards
4. `docs/01_FOUNDATION/Vision_Mission_Values.md` — why we exist
5. `docs/02_BUSINESS/Business_Model.md` — how we make money
6. `docs/03_PRODUCT/Member_Experience_Blueprint.md` — what we ship
7. `docs/06_OPERATIONS/Operating_Model.md` — how we operate
8. `docs/07_EXECUTION/6_Month_Execution_Plan.md` — what we are doing this week

## Deployment

Production is deployed on OVH VPS. See:
- [`docs/09_RESEARCH/DEPLOY.md`](docs/09_RESEARCH/DEPLOY.md) — OVH deployment guide
- [`docs/09_RESEARCH/RUNBOOK.md`](docs/09_RESEARCH/RUNBOOK.md) — operations runbook

## License

Proprietary. All rights reserved.
