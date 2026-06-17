import PhoneFrame from '../components/PhoneFrame';

type Screen = {
  name: string;
  tag: string;
  tagClass?: string;
  body: React.ReactNode;
};

function StatusBar() {
  return <div style={{ height: 36 }} />;
}

function AuthScreen() {
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
          <input placeholder="98765 43210" defaultValue="98765 43210" />
        </div>
      </div>

      <button className="btn-block" style={{ marginTop: 8 }}>
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

function OtpScreen() {
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
              border: '1.5px solid var(--border)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: 22,
              fontWeight: 700,
              color: n <= 4 ? 'var(--accent)' : 'var(--text-dim)',
            }}
          >
            {n <= 4 ? '4' : ''}
          </div>
        ))}
      </div>

      <div style={{ textAlign: 'center', color: 'var(--text-muted)', fontSize: 13 }}>
        Resend in 0:42
      </div>

      <div style={{ flex: 1 }} />

      <button className="btn-block">Verify and continue</button>
    </div>
  );
}

function HomeScreen() {
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

      <button className="btn-block" style={{ marginTop: 0, marginBottom: 16 }}>
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

function LiveScreen() {
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

      <div className="trade-call">
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <div className="pair">GBP/JPY</div>
          <span className="tag tag-live" style={{ fontSize: 10 }}>
            NEW
          </span>
        </div>
        <div className="action">▼ SELL · 191.42</div>
        <div className="row-mini">
          <span>SL <b>191.85</b></span>
          <span>TP1 <b>190.90</b></span>
          <span>TP2 <b>190.20</b></span>
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
        <div className="icon">📊</div>
        <div className="meta">
          <b>Recent calls</b>
          <span>5 in the last hour</span>
        </div>
      </div>

      <button className="btn-ghost">Leave room</button>
    </div>
  );
}

function PaywallScreen() {
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

      <button className="btn-block" style={{ marginTop: 16 }}>
        Pay with UPI / Card
      </button>
      <button className="btn-ghost" style={{ marginTop: 10 }}>
        Restore subscription
      </button>
    </div>
  );
}

function ProfileScreen() {
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
          <span>Trialing · 2d 14h left</span>
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
        <div className="icon">🌐</div>
        <div className="meta">
          <b>Language</b>
          <span>English (India)</span>
        </div>
      </div>
      <div className="card-row">
        <div className="icon">❓</div>
        <div className="meta">
          <b>Help &amp; support</b>
          <span>support@fxteller.app</span>
        </div>
      </div>

      <button className="btn-ghost" style={{ marginTop: 'auto' }}>Sign out</button>
    </div>
  );
}

function OverlayScreen() {
  return (
    <div className="screen" style={{ background: '#1f2937', position: 'relative' }}>
      <StatusBar />
      <div
        style={{
          marginTop: 16,
          padding: 12,
          background: 'rgba(0,0,0,0.4)',
          borderRadius: 10,
          color: '#9ca3af',
          fontSize: 11,
          textAlign: 'center',
        }}
      >
        User is in another app
      </div>

      <div style={{ marginTop: 60, textAlign: 'center', color: '#6b7280', fontSize: 12 }}>
        Chrome browser · 9:41 AM
      </div>

      <div
        style={{
          position: 'absolute',
          top: 110,
          left: 16,
          right: 16,
          background: 'linear-gradient(135deg, #f5b400, #ffa500)',
          borderRadius: 16,
          padding: 14,
          color: '#0b1220',
          boxShadow: '0 0 40px rgba(245, 180, 0, 0.6)',
          animation: 'callGlow 1.5s ease-in-out infinite',
        }}
      >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ fontSize: 16, fontWeight: 800 }}>USD/JPY · BUY</div>
          <div
            style={{
              background: 'rgba(0,0,0,0.2)',
              padding: '2px 8px',
              borderRadius: 999,
              fontSize: 10,
              fontWeight: 700,
            }}
          >
            FX-Teller
          </div>
        </div>
        <div style={{ fontSize: 12, fontWeight: 600, marginTop: 2 }}>Entry 149.20</div>
        <div style={{ display: 'flex', gap: 10, fontSize: 10, marginTop: 8 }}>
          <span>SL <b>148.80</b></span>
          <span>TP1 <b>149.80</b></span>
          <span>TP2 <b>150.40</b></span>
        </div>
        <div
          style={{
            marginTop: 10,
            display: 'flex',
            gap: 6,
          }}
        >
          <button
            style={{
              flex: 1,
              background: '#0b1220',
              color: '#fff',
              border: 'none',
              padding: '6px',
              borderRadius: 6,
              fontSize: 11,
              fontWeight: 700,
            }}
          >
            Open app
          </button>
          <button
            style={{
              flex: 1,
              background: 'rgba(11, 18, 32, 0.2)',
              color: '#0b1220',
              border: 'none',
              padding: '6px',
              borderRadius: 6,
              fontSize: 11,
              fontWeight: 700,
            }}
          >
            Dismiss
          </button>
        </div>
      </div>

      <div
        style={{
          position: 'absolute',
          bottom: 12,
          left: 16,
          right: 16,
          textAlign: 'center',
          color: '#6b7280',
          fontSize: 10,
        }}
      >
        Android system overlay · tap to drag
      </div>
    </div>
  );
}

const screens: Screen[] = [
  { name: 'Auth', tag: 'sign in', tagClass: 'tag-done', body: <AuthScreen /> },
  { name: 'OTP', tag: 'verify', tagClass: 'tag-done', body: <OtpScreen /> },
  { name: 'Home', tag: 'main', tagClass: 'tag-done', body: <HomeScreen /> },
  { name: 'Live', tag: 'audio', tagClass: 'tag-done', body: <LiveScreen /> },
  { name: 'Trade call', tag: 'in-app', tagClass: 'tag-done', body: <LiveScreen /> },
  { name: 'Overlay', tag: 'android', tagClass: 'tag-done', body: <OverlayScreen /> },
  { name: 'Paywall', tag: 'razorpay', tagClass: 'tag-done', body: <PaywallScreen /> },
  { name: 'Profile', tag: 'account', tagClass: 'tag-done', body: <ProfileScreen /> },
];

export default function AppPreviewPage() {
  return (
    <section className="section" style={{ paddingTop: 80 }}>
      <div className="container">
        <div className="section-head">
          <span className="eyebrow">App UI</span>
          <h1 className="section-title">Eight screens. One focused flow.</h1>
          <p className="section-sub">
            Every screen a trader will see in v1 — from phone-number entry to the Android
            floating overlay that surfaces a trade call over any other app.
          </p>
        </div>

        <div className="mockup-grid">
          {screens.map((s) => (
            <div key={s.name} style={{ textAlign: 'center' }}>
              <PhoneFrame>
                {s.body}
              </PhoneFrame>
              <div style={{ marginTop: 14, fontWeight: 700 }}>{s.name}</div>
              <div style={{ marginTop: 4 }}>
                <span className={`tag ${s.tagClass ?? ''}`}>{s.tag}</span>
              </div>
            </div>
          ))}
        </div>

        <div className="banner" style={{ marginTop: 80 }}>
          <h3>Want to feel the flow?</h3>
          <p>Step through the screens with the interactive demo.</p>
          <a href="/demo" className="btn btn-lg">
            Open interactive demo →
          </a>
        </div>
      </div>
    </section>
  );
}
