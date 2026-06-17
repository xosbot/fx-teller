import Link from 'next/link';
import PhoneFrame from '../components/PhoneFrame';

type Feature = {
  icon: string;
  title: string;
  body: string;
  bullets: string[];
};

const sections: { eyebrow: string; title: string; subtitle: string; features: Feature[] }[] = [
  {
    eyebrow: 'For traders',
    title: 'Live room + calls that you actually feel',
    subtitle:
      'A purpose-built experience for following a single host through a market session, in real time.',
    features: [
      {
        icon: '🎙',
        title: 'Live audio room (100ms)',
        body: 'Low-latency audio powered by 100ms.live. The host streams commentary, the listeners hear it in under a second.',
        bullets: [
          'Auto-reconnect on flaky mobile networks',
          'Background-friendly listener role',
          'Optional data channel for trade calls (sub-second)',
        ],
      },
      {
        icon: '📳',
        title: 'Long-vibration trade calls',
        body: 'When a call lands, your phone vibrates in a sustained burst you can feel through a pocket. Followed by the floating widget with pair, action, entry, SL, and TP.',
        bullets: [
          'Chained expo-haptics impacts (Android + iOS)',
          'Floating overlay survives app switching (Android)',
          'In-app full-screen modal (iOS)',
        ],
      },
      {
        icon: '🎵',
        title: 'Sentiment music cues',
        body: 'The host switches between Calm and Alert states. The app crossfades the background music so the mood of the room is felt, not read.',
        bullets: [
          'Two curated, pre-bundled audio assets',
          'Smooth crossfade (no jarring cuts)',
          'Opt-in: respects OS media volume',
        ],
      },
      {
        icon: '📅',
        title: 'Session schedule',
        body: 'A simple, scrollable list of upcoming sessions. Tap to set a local reminder so you never miss a London or New York open.',
        bullets: [
          'Asia, London, and New York sessions pre-scheduled',
          'Local time + Asia/Kolkata by default',
          'One-tap calendar add (v2)',
        ],
      },
    ],
  },
  {
    eyebrow: 'For the business',
    title: 'Auth, payments, and growth built in',
    subtitle:
      'No credit-card friction for new users, real UPI payments for subscribers, and analytics-ready events.',
    features: [
      {
        icon: '🔐',
        title: 'Phone OTP authentication',
        body: 'A 6-digit code, no password, no email. We use a JWT session for the host console and the app alike.',
        bullets: [
          'Twilio-compatible SMS provider',
          'Rate-limited OTP request endpoint',
          'Bcrypt-hashed OTPs, 5-minute TTL',
        ],
      },
      {
        icon: '💳',
        title: 'Razorpay subscriptions',
        body: 'Monthly plan at ₹499. UPI, cards, netbanking, and wallets. Webhook flips the user from trialing to active.',
        bullets: [
          'Signed webhook verification',
          'Idempotent webhook handler',
          'Auto-retry on payment failure (v2)',
        ],
      },
      {
        icon: '🎁',
        title: '3-day free trial (no card)',
        body: 'Every verified user gets 3 full days of access. No card required, no surprise charges, easy conversion to the paywall.',
        bullets: [
          'Trial banner with countdown on home + live screens',
          'Paywall triggered when trial_ends_at < now',
          'Server-enforced, not just client-side',
        ],
      },
      {
        icon: '🛡',
        title: 'Hardened backend',
        body: 'NestJS on a Dockerized OVH VPS behind SWAG (nginx + Let&apos;s Encrypt + fail2ban). Postgres 16 with daily offsite backups.',
        bullets: [
          'JWT + role-based access (host, listener)',
          'Server-Sent Events for live trade-call broadcast',
          'Health endpoint + structured logs',
        ],
      },
    ],
  },
];

export default function FeaturesPage() {
  return (
    <>
      <section className="section" style={{ paddingTop: 80 }}>
        <div className="container">
          <div className="section-head">
            <span className="eyebrow">Features</span>
            <h1 className="section-title">Every detail, built for traders.</h1>
            <p className="section-sub">
              A focused look at what ships in v1 — and what is intentionally out of scope to keep
              the team shipping fast.
            </p>
          </div>

          {sections.map((sec) => (
            <div key={sec.title} style={{ marginBottom: 80 }}>
              <div style={{ textAlign: 'center', marginBottom: 36 }}>
                <span className="eyebrow">{sec.eyebrow}</span>
                <h2 className="section-title" style={{ fontSize: 32, marginTop: 12 }}>
                  {sec.title}
                </h2>
                <p className="section-sub">{sec.subtitle}</p>
              </div>
              <div className="grid grid-2">
                {sec.features.map((f) => (
                  <div key={f.title} className="card">
                    <div className="feature">
                      <div className="ico">{f.icon}</div>
                      <h3>{f.title}</h3>
                      <p>{f.body}</p>
                      <ul style={{ margin: '8px 0 0', paddingLeft: 18, color: 'var(--text-muted)' }}>
                        {f.bullets.map((b) => (
                          <li key={b} style={{ marginBottom: 4 }}>
                            {b}
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}

          <div className="section-head" style={{ marginTop: 80 }}>
            <span className="eyebrow">In the live experience</span>
            <h2 className="section-title">A peek at the live screen.</h2>
          </div>

          <div className="grid grid-2" style={{ alignItems: 'center' }}>
            <div>
              <h3 style={{ fontSize: 24, marginBottom: 12 }}>
                Everything you need on one screen.
              </h3>
              <p style={{ color: 'var(--text-muted)' }}>
                The live screen is the heart of the app. It shows the host&apos;s audio, the
                current sentiment, and — most importantly — incoming trade calls. A trader can
                keep this in their pocket and react without unlocking the phone.
              </p>
              <ul style={{ marginTop: 20, paddingLeft: 20, color: 'var(--text-muted)' }}>
                <li>Persistent audio with status indicator</li>
                <li>Live listener count</li>
                <li>Last 5 trade calls (collapsible)</li>
                <li>Sentiment state and music cue</li>
                <li>Quick leave / mute controls</li>
              </ul>
              <div style={{ marginTop: 28 }}>
                <Link href="/app-preview" className="btn">
                  See all app screens →
                </Link>
              </div>
            </div>
            <div>
              <PhoneFrame>
                <div className="screen">
                  <div className="live-pill">
                    <span className="live-dot" />
                    LIVE · LONDON
                  </div>
                  <div className="screen-title" style={{ marginTop: 14 }}>
                    Rijo · 412 listening
                  </div>
                  <div className="audio-wave">
                    <span /><span /><span /><span /><span /><span /><span /><span />
                  </div>

                  <div className="trade-call">
                    <div className="pair">EUR/USD</div>
                    <div className="action">▲ BUY · 1.0842</div>
                    <div className="row-mini">
                      <span>SL <b>1.0820</b></span>
                      <span>TP1 <b>1.0870</b></span>
                      <span>TP2 <b>1.0900</b></span>
                    </div>
                  </div>

                  <div className="card-row">
                    <div className="icon">🎵</div>
                    <div className="meta">
                      <b>Sentiment · Alert</b>
                      <span>Music switched</span>
                    </div>
                  </div>
                  <div className="card-row">
                    <div className="icon">💬</div>
                    <div className="meta">
                      <b>Reactions</b>
                      <span>🔥 × 24 · 👀 × 11</span>
                    </div>
                  </div>

                  <button className="btn-ghost">Leave room</button>
                </div>
              </PhoneFrame>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
