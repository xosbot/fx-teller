-- FX-Teller initial schema. Idempotent: safe to run on every boot.
CREATE TABLE IF NOT EXISTS users (
  id            UUID PRIMARY KEY,
  phone         TEXT UNIQUE NOT NULL,
  name          TEXT,
  role          TEXT NOT NULL DEFAULT 'listener',
  trial_ends_at TIMESTAMPTZ,
  subscription  TEXT NOT NULL DEFAULT 'none',
  sub_ends_at   TIMESTAMPTZ,
  rzp_customer_id TEXT,
  rzp_subscription_id TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS otp_codes (
  phone       TEXT PRIMARY KEY,
  code        TEXT NOT NULL,
  expires_at  TIMESTAMPTZ NOT NULL,
  attempts    INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS sessions (
  id          UUID PRIMARY KEY,
  title       TEXT NOT NULL,
  host_name   TEXT NOT NULL,
  host_id     TEXT,
  starts_at   TIMESTAMPTZ NOT NULL,
  status      TEXT NOT NULL DEFAULT 'UPCOMING',
  started_at  TIMESTAMPTZ,
  ended_at    TIMESTAMPTZ,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS trade_calls (
  id           UUID PRIMARY KEY,
  session_id   UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
  host_id      TEXT NOT NULL,
  instrument   TEXT NOT NULL,
  side         TEXT NOT NULL,
  entry        NUMERIC NOT NULL,
  sl           NUMERIC NOT NULL,
  tp           NUMERIC[] NOT NULL,
  pushed_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  expires_at   TIMESTAMPTZ NOT NULL,
  alert_ms     INT NOT NULL DEFAULT 15000
);

CREATE TABLE IF NOT EXISTS music_cues (
  id          UUID PRIMARY KEY,
  session_id  UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
  sentiment   TEXT NOT NULL,
  track_name  TEXT NOT NULL,
  set_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS webhook_events (
  event_id   TEXT PRIMARY KEY,
  source     TEXT NOT NULL,
  received_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
