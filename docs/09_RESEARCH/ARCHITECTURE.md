# Architecture (v1)

## High-level

```
+-------------------+        +--------------------+
| Host (mic input)  | ─────> |  100ms.live room   |
+-------------------+        |  (audio SFU)       |
                             +---------+----------+
                                       |
                          data channel (trade_call, music_cue)
                                       |
+--------------------------+    +-------v--------------+    +------------------+
| Mobile app (Expo RN)     | <─ |  Backend (NestJS)    | <─ | Host Console     |
|  - 100ms listener        |    |  - auth (OTP)        |    |  (Next.js)       |
|  - floating overlay      |    |  - 100ms token mint  |    |  - push calls    |
|  - SSE for events        |    |  - SSE event bus     |    |  - switch music  |
|  - Razorpay checkout     |    |  - Razorpay          |    +------------------+
|  - trial logic           |    |  - Postgres          |
+--------------+-----------+    +----------------------+
               │                          ^
               v                          |
+-----------------------------+   +-------+
|  Trade-call (vibration +    |   | Webhooks
|  floating widget/modal)     |   | (Razorpay)
+-----------------------------+   +-------+
```

## Backend modules

- `auth/` — phone OTP request + verify, JWT issue
- `users/` — profile, role, subscription state
- `sessions/` — upcoming + currently live session
- `hms/` — 100ms token minting (signed JWT with role)
- `trade-calls/` — push (host), list recent, broadcast via in-process event bus
- `music-cues/` — set sentiment (host), get current, broadcast
- `subscriptions/` — create Razorpay subscription, verify checkout
- `events/` — in-process pub/sub + SSE controller for clients
- `health/` — `/api/health` for liveness

## Mobile app

- `app/_layout.tsx` — root stack + auth context
- `app/index.tsx` — splash router
- `app/auth.tsx` — phone OTP flow
- `app/home.tsx` — live CTA + schedule + trial banner
- `app/live.tsx` — 100ms join, music cue, trade-call modal w/ vibration
- `app/paywall.tsx` — Razorpay checkout
- `app/profile.tsx` — name, phone, subscription state, sign out
- `modules/floating-overlay/` — Android native module for true system overlay

## Trade-call delivery

Two parallel paths (clients can use either):
1. **100ms data channel** — host sends `sendBroadcastMessage` via 100ms SDK; listeners receive via `ON_MESSAGE`. Lowest latency, requires being in the room.
2. **SSE** — `GET /api/events/stream` streams `{ type, payload }` events. Works without 100ms in case of disconnect.

v1: SSE is the primary path; 100ms data channel is wired but optional.

## Music switching

Host console → `POST /api/music-cues/set` → backend persists in DB → broadcasts via SSE + 100ms data → client switches local audio asset.

## Floating overlay (Android)

`modules/floating-overlay` is a custom Expo Module that exposes:
- `hasOverlayPermission()` / `requestOverlayPermission()` — manage `SYSTEM_ALERT_WINDOW`
- `showOverlay(payload, autoDismissMs)` — display a draggable trade-call card over any app
- `hideOverlay()` — dismiss

iOS does not support system overlays; v1 uses a full-screen React Native modal triggered when a trade call arrives.

## Trial logic

- On first verify, user gets `subscription = 'trialing'`, `trial_ends_at = now + 3 days`
- Client checks `trial_ends_at` for the countdown banner
- When `trial_ends_at < now`, the user hits the paywall (no audio / no calls)
- Subscribing creates a Razorpay subscription; webhook flips `subscription = 'active'`

## Why these simplifications (vs. original plan)

| Original plan | v1 choice | Why |
|---|---|---|
| In-app chat (WebSocket) | Deferred to v2 | Single biggest simplification |
| 5 music states | 2 (Calm / Alert) | Half the music licensing, half the UI |
| iOS Live Activity | In-app modal | Removes native module work |
| Trial with card | No card | Lower friction, simpler Razorpay flow |
| Yearly tier | Monthly only | One plan, one paywall |
| Full design system | Text wordmark + 1 accent | Ship in 1 day |
| Chat moderation + roles | Listener + Host only | Removes moderator tooling |
