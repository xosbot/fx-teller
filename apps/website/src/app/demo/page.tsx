'use client';

import { useState } from 'react';
import PhoneFrame from '../components/PhoneFrame';

type Step = {
  id: string;
  name: string;
  caption: string;
  render: (go: (id: string) => void) => React.ReactNode;
};

function StatusBar() {
  return <div style={{ height: 36 }} />;
}

function AuthStep({ go }: { go: (id: string) => void }) {
  return (
    <div className="screen">
      <StatusBar />
      <div style={{ textAlign: 'center', marginTop: 32, marginBottom: 28 }}>
        <div style={{ fontSize: 26, fontWeight: 800, letterSpacing: '-0.02em' }}>
          FX<span style={{ color: 'var(--accent)' }}>-Teller</span>
        </div>
        <div className="screen-sub" style={{ marginTop: 4 }}>
          Live trading community
        </div>
      </div>

      <div className="field">
        <label>Phone number</label>
        <div style={{ display: 'flex', gap: 8 }}>
          <div
            style={{
              background: 'var(--bg-elev)',
              border: '1px solid var(--border)',
              borderRadius: 8,
              padding: '12px 14px',
              fontSize: 14,
              color: 'var(--text-muted)',
              minWidth: 70,
              textAlign: 'center',
            }}
          >
            🇮🇳 +91
          </div>
          <input defaultValue="98765 43210" />
        </div>
      </div>

      <button className="btn-block" style={{ marginTop: 8 }} onClick={() => go('otp')}>
        Send OTP
      </button>
      <div
        style={{
          textAlign: 'center',
          marginTop: 16,
          fontSize: 12,
          color: 'var(--text-muted)',
        }}
      >
        By continuing you accept the Terms of Service.
      </div>
    </div>
  );
}

function OtpStep({ go }: { go: (id: string) => void }) {
  return (
    <div className="screen">
      <StatusBar />
      <div className="screen-title" style={{ marginTop: 20 }}>
        Enter the code
      </div>
      <div className="screen-sub">We sent a 6-digit code to +91 ••••• 43210</div>

      <div style={{ display: 'flex', gap: 8, margin: '24px 0' }}>
        {[1, 2, 3, 4, 5, 6].map((n) => (
          <div
            key={n}
            style={{
              flex: 1,
              height: 52,
              borderRadius: 10,
              background: 'var(--bg-elev)',
              border: '1.5px solid var(--accent)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: 22,
              fontWeight: 700,
              color: 'var(--accent)',
            }}
          >
            4
          </div>
        ))}
      </div>

      <div style={{ textAlign: 'center', color: 'var(--text-muted)', fontSize: 13 }}>
        Resend in 0:42
      </div>

      <div style={{ flex: 1 }} />

      <button className="btn-block" onClick={() => go('home')}>
        Verify and continue
      </button>
    </div>
  );
}

function HomeStep({ go }: { go: (id: string) => void }) {
  return (
    <div className="screen">
      <StatusBar />
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          marginTop: 12,
        }}
      >
        <div style={{ fontWeight: 800, fontSize: 18 }}>
          FX<span style={{ color: 'var(--accent)' }}>-Teller</span>
        </div>
        <div
          style={{
            width: 32,
            height: 32,
            borderRadius: '50%',
            background: 'var(--bg-elev-2)',
            border: '1px solid var(--border)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: 14,
          }}
        >
          👤
        </div>
      </div>

      <div className="live-pill" style={{ marginTop: 20 }}>
        <span className="live-dot" />
        LIVE NOW · LONDON
      </div>
      <div className="screen-title" style={{ marginTop: 10 }}>
        Rijo · 412 listening
      </div>
      <div className="screen-sub">Live commentary on EUR, GBP, and Gold</div>

      <div className="audio-wave">
        <span /><span /><span /><span /><span /><span /><span /><span />
      </div>

      <button
        className="btn-block"
        style={{ marginTop: 0, marginBottom: 16 }}
        onClick={() => go('live')}
      >
        🎙 Join live audio
      </button>

      <div
        style={{
          fontSize: 11,
          textTransform: 'uppercase',
          letterSpacing: '0.08em',
          color: 'var(--text-muted)',
          margin: '8px 0 10px',
          fontWeight: 700,
        }}
      >
        Upcoming sessions
      </div>
      <div className="card-row">
        <div className="icon">🌏</div>
        <div className="meta">
          <b>Asia session</b>
          <span>Tonight · 11:30 PM</span>
        </div>
      </div>
      <div className="card-row">
        <div className="icon">🗽</div>
        <div className="meta">
          <b>New York session</b>
          <span>Tomorrow · 6:30 PM</span>
        </div>
      </div>

      <div
        style={{
          marginTop: 14,
          padding: 12,
          background: 'var(--accent-soft)',
          border: '1px solid rgba(245, 180, 0, 0.3)',
          borderRadius: 10,
          fontSize: 12,
          color: 'var(--accent)',
        }}
      >
        ✨ <b>Trial active</b> · 2 days, 14 hours left
      </div>
    </div>
  );
}

function LiveStep({ go }: { go: (id: string) => void }) {
  return (
    <div className="screen">
      <StatusBar />
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          marginTop: 12,
        }}
      >
        <div className="live-pill">
          <span className="live-dot" />
          LIVE
        </div>
        <div style={{ fontSize: 12, color: 'var(--text-muted)' }}>412 listening</div>
      </div>

      <div className="screen-title" style={{ marginTop: 14 }}>
        Rijo
      </div>
      <div className="audio-wave">
        <span /><span /><span /><span /><span /><span /><span /><span />
      </div>

      <div
        style={{
          fontSize: 12,
          color: 'var(--text-muted)',
          textAlign: 'center',
          margin: '4px 0 8px',
        }}
      >
        Tap below to simulate a trade call ↓
      </div>

      <button
        onClick={() => go('call')}
        style={{
          background: 'var(--bg-elev-2)',
          border: '1px dashed var(--accent)',
          color: 'var(--accent)',
          padding: 12,
          borderRadius: 10,
          fontSize: 13,
          fontWeight: 700,
          marginBottom: 12,
        }}
      >
        ⚡ Push trade call from host
      </button>

      <div className="card-row">
        <div className="icon">🎵</div>
        <div className="meta">
          <b>Sentiment · Alert</b>
          <span>Music switched</span>
        </div>
      </div>
      <div className="card-row">
        <div className="icon">📊</div>
        <div className="meta">
          <b>Recent calls</b>
          <span>5 in the last hour</span>
        </div>
      </div>

      <button className="btn-ghost" onClick={() => go('paywall')}>
        Leave room
      </button>
    </div>
  );
}

function CallStep({ go }: { go: (id: string) => void }) {
  return (
    <div className="screen" style={{ background: 'rgba(11, 18, 32, 0.95)' }}>
      <StatusBar />
      <div style={{ textAlign: 'center', marginTop: 12, fontSize: 11, color: 'var(--text-muted)' }}>
        Trade call received · 0.6s delivery
      </div>

      <div
        style={{
          marginTop: 20,
          padding: 18,
          background: 'linear-gradient(135deg, rgba(245, 180, 0, 0.25), rgba(245, 180, 0, 0.08))',
          border: '2px solid var(--accent)',
          borderRadius: 18,
          boxShadow: '0 0 60px rgba(245, 180, 0, 0.4)',
          animation: 'callGlow 1.2s ease-in-out infinite',
        }}
      >
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: 6,
          }}
        >
          <div style={{ fontSize: 22, fontWeight: 800, color: 'var(--accent)' }}>GBP/JPY</div>
          <span className="tag tag-live" style={{ fontSize: 10 }}>
            NEW
          </span>
        </div>
        <div style={{ fontSize: 16, fontWeight: 700, marginBottom: 4 }}>▼ SELL · 191.42</div>
        <div style={{ display: 'flex', gap: 12, fontSize: 12, color: 'var(--text-muted)' }}>
          <span>
            SL <b style={{ color: '#fff' }}>191.85</b>
          </span>
          <span>
            TP1 <b style={{ color: '#fff' }}>190.90</b>
          </span>
          <span>
            TP2 <b style={{ color: '#fff' }}>190.20</b>
          </span>
        </div>
        <div
          style={{
            marginTop: 12,
            paddingTop: 12,
            borderTop: '1px solid rgba(245, 180, 0, 0.2)',
            fontSize: 11,
            color: 'var(--text-muted)',
          }}
        >
          📳 Long vibration + floating widget (Android)
        </div>
      </div>

      <div className="card-row" style={{ marginTop: 20 }}>
        <div className="icon">🎵</div>
        <div className="meta">
          <b>Music switched to Alert</b>
          <span>Crossfaded over 1.2s</span>
        </div>
      </div>
      <div className="card-row">
        <div className="icon">⏱</div>
        <div className="meta">
          <b>Delivery time</b>
          <span>0.6s from host press</span>
        </div>
      </div>

      <button className="btn-block" onClick={() => go('live')} style={{ marginTop: 'auto' }}>
        Acknowledge &amp; continue
      </button>
    </div>
  );
}

function PaywallStep({ go }: { go: (id: string) => void }) {
  return (
    <div className="screen">
      <StatusBar />
      <div style={{ textAlign: 'center', marginTop: 20 }}>
        <div style={{ fontSize: 36, marginBottom: 8 }}>🔒</div>
        <div className="screen-title" style={{ fontSize: 20 }}>
          Your trial has ended
        </div>
        <div className="screen-sub" style={{ marginTop: 4 }}>
          Subscribe to keep listening to live calls.
        </div>
      </div>

      <div
        style={{
          marginTop: 20,
          padding: 16,
          background: 'var(--bg-elev)',
          border: '1.5px solid var(--accent)',
          borderRadius: 14,
          position: 'relative',
        }}
      >
        <span
          style={{
            position: 'absolute',
            top: -8,
            right: 12,
            background: 'var(--accent)',
            color: '#0b1220',
            fontSize: 10,
            fontWeight: 800,
            padding: '3px 8px',
            borderRadius: 999,
            textTransform: 'uppercase',
            letterSpacing: '0.06em',
          }}
        >
          Best value
        </span>
        <div style={{ fontSize: 12, color: 'var(--text-muted)' }}>Monthly</div>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 4, marginTop: 4 }}>
          <span style={{ fontSize: 28, fontWeight: 800 }}>₹499</span>
          <span style={{ color: 'var(--text-muted)', fontSize: 13 }}>/ month</span>
        </div>
        <ul
          style={{
            margin: '12px 0 0',
            padding: 0,
            listStyle: 'none',
            fontSize: 13,
            color: 'var(--text-muted)',
          }}
        >
          <li style={{ marginBottom: 6 }}>✓ Live audio + trade calls</li>
          <li style={{ marginBottom: 6 }}>✓ Sentiment music cues</li>
          <li>✓ Cancel anytime</li>
        </ul>
      </div>

      <button className="btn-block" style={{ marginTop: 16 }} onClick={() => go('profile')}>
        Pay with UPI / Card
      </button>
      <button className="btn-ghost" style={{ marginTop: 10 }}>
        Restore subscription
      </button>
    </div>
  );
}

function ProfileStep({ go }: { go: (id: string) => void }) {
  return (
    <div className="screen">
      <StatusBar />
      <div className="screen-title" style={{ marginTop: 16 }}>
        Profile
      </div>
      <div className="screen-sub">Manage your account</div>

      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: 14,
          margin: '20px 0',
          padding: 14,
          background: 'var(--bg-elev)',
          border: '1px solid var(--border)',
          borderRadius: 12,
        }}
      >
        <div
          style={{
            width: 48,
            height: 48,
            borderRadius: '50%',
            background: 'var(--accent-soft)',
            border: '1.5px solid var(--accent)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: 20,
            fontWeight: 800,
            color: 'var(--accent)',
          }}
        >
          A
        </div>
        <div>
          <div style={{ fontWeight: 700, fontSize: 15 }}>Arjun K.</div>
          <div style={{ color: 'var(--text-muted)', fontSize: 12 }}>+91 ••••• 43210</div>
        </div>
      </div>

      <div className="card-row">
        <div className="icon">⭐</div>
        <div className="meta">
          <b>Subscription</b>
          <span style={{ color: 'var(--success)' }}>Active · Pro</span>
        </div>
      </div>
      <div className="card-row">
        <div className="icon">🔔</div>
        <div className="meta">
          <b>Notifications</b>
          <span>All on</span>
        </div>
      </div>
      <div className="card-row">
        <div className="icon">📊</div>
        <div className="meta">
          <b>This month</b>
          <span>18 calls received</span>
        </div>
      </div>
      <div className="card-row">
        <div className="icon">🌐</div>
        <div className="meta">
          <b>Language</b>
          <span>English (India)</span>
        </div>
      </div>

      <button className="btn-ghost" style={{ marginTop: 'auto' }} onClick={() => go('auth')}>
        Restart demo
      </button>
    </div>
  );
}

const steps: Step[] = [
  {
    id: 'auth',
    name: 'Sign in',
    caption:
      'User enters their phone number. We send a 6-digit OTP via SMS. No password, no email, no friction.',
    render: (go) => <AuthStep go={go} />,
  },
  {
    id: 'otp',
    name: 'Verify OTP',
    caption:
      'The 6-digit code auto-fills on most Android devices. Verify creates a JWT session and starts the 3-day trial.',
    render: (go) => <OtpStep go={go} />,
  },
  {
    id: 'home',
    name: 'Home',
    caption:
      'The home screen shows the currently live session, upcoming schedule, and a trial banner with the time remaining.',
    render: (go) => <HomeStep go={go} />,
  },
  {
    id: 'live',
    name: 'Live audio',
    caption:
      'The user joins the 100ms audio room. They hear the host in under a second. The 412 listeners count is live.',
    render: (go) => <LiveStep go={go} />,
  },
  {
    id: 'call',
    name: 'Trade call',
    caption:
      'The host presses the trade-call button in the host console. Within 0.6s the user feels a long vibration and sees this card — with the floating widget on Android.',
    render: (go) => <CallStep go={go} />,
  },
  {
    id: 'paywall',
    name: 'Paywall',
    caption:
      'After the trial ends, the user is shown a single monthly plan (₹499). Razorpay handles UPI, cards, and netbanking. Webhook flips them to active.',
    render: (go) => <PaywallStep go={go} />,
  },
  {
    id: 'profile',
    name: 'Profile',
    caption:
      'A focused profile screen with subscription state, notification preferences, language, and sign out.',
    render: (go) => <ProfileStep go={go} />,
  },
];

export default function DemoPage() {
  const [activeId, setActiveId] = useState('auth');
  const active = steps.find((s) => s.id === activeId) ?? steps[0];

  return (
    <section className="section" style={{ paddingTop: 80 }}>
      <div className="container">
        <div className="section-head">
          <span className="eyebrow">Interactive demo</span>
          <h1 className="section-title">Walk through the user flow.</h1>
          <p className="section-sub">
            Step through the screens a trader will see. Click a step on the left to jump to it.
          </p>
        </div>

        <div className="demo-wrap">
          <div className="demo-controls">
            {steps.map((s, i) => (
              <button
                key={s.id}
                className={activeId === s.id ? 'active' : ''}
                onClick={() => setActiveId(s.id)}
              >
                <span className="step-num">{i + 1}</span>
                {s.name}
              </button>
            ))}
          </div>

          <div>
            <div className="demo-stage">
              <PhoneFrame>{active.render(setActiveId)}</PhoneFrame>
            </div>
            <p className="demo-caption">{active.caption}</p>
          </div>
        </div>

        <div className="banner" style={{ marginTop: 60 }}>
          <h3>That&apos;s the v1 user flow.</h3>
          <p>
            6 steps from install to paying subscriber, with the trade-call moment as the
            emotional peak.
          </p>
          <a href="/roadmap" className="btn btn-lg">
            See the development plan →
          </a>
        </div>
      </div>
    </section>
  );
}
