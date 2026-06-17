# FX-Teller

A live podcast trading community for forex traders in Kerala, India.

**Status:** v1 MVP (in build). Single host streams live audio commentary, pushes trade calls with a long vibration + floating widget, and switches background music to signal market sentiment.

## Repo layout

```
fx-teller/
├── apps/
│   ├── backend/        # NestJS API (auth, sessions, trade-calls, music-cues, subs)
│   ├── host-console/   # Next.js web app for the host
│   └── mobile/         # Expo React Native app (iOS + Android)
├── packages/
│   └── shared-types/   # TypeScript types shared across apps
├── infra/              # Docker compose, scripts, Dockerfile
└── docs/               # Architecture, runbooks
```

## Stack

| Layer | Choice |
|---|---|
| Mobile | Expo (React Native), EAS Build |
| Live audio | 100ms |
| Auth | Phone OTP (in-app), Firebase optional |
| Payments | Razorpay (UPI / Card / Netbanking) |
| Trade call UI | Android: floating overlay (custom Kotlin module) · iOS: in-app full-screen modal |
| Vibration | expo-haptics (long-vibrate via chained impacts) |
| Music | 2 states (Calm / Alert), pre-bundled audio assets |
| Backend | NestJS on OVH VPS, Docker Compose |
| DB | PostgreSQL 16 |
| Reverse proxy | SWAG (nginx + Let's Encrypt + fail2ban) |
| Payments webhook | Razorpay → /api/webhooks/razorpay |

## Quick start (local dev)

```bash
# Install deps
pnpm install

# Start postgres + api + web
docker compose -f infra/docker-compose.yml up -d db api web

# Run mobile (in another terminal)
cd apps/mobile
pnpm dev
```

## Production deploy (OVH VPS)

See `docs/DEPLOY.md`.

## Docs

- `docs/ARCHITECTURE.md` — system design
- `docs/DEPLOY.md` — OVH deployment guide
- `docs/RUNBOOK.md` — operations
