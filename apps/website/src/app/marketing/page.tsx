type Channel = {
  ch: string;
  title: string;
  body: string;
  kpi: string;
};

const channels: Channel[] = [
  {
    ch: '01 · Organic social',
    title: 'YouTube Shorts + Instagram Reels',
    body:
      'Daily 30–60s recaps of the day\'s calls with the host on camera. Each short ends with "Download FX-Teller, free for 3 days" + a link. We post in English first, then dub the top 10% into Malayalam.',
    kpi: 'KPI: 1M views / month in 90 days',
  },
  {
    ch: '02 · Community seeding',
    title: 'WhatsApp + Telegram invite funnel',
    body:
      'Partner with 8–10 small Kerala-based trading groups (1k–10k members each). Offer the host a free 2-week "office hours" appearance, in exchange for the group admin pinning a join link.',
    kpi: 'KPI: 20 partner groups by month 3',
  },
  {
    ch: '03 · Influencer collabs',
    title: 'Kerala finance YouTubers',
    body:
      'Pay 3 mid-tier (50k–200k subs) Malayalam finance creators for a single sponsored live. Offer them a 6-month free Pro code for their audience. Track sign-ups via unique code.',
    kpi: 'KPI: ₹30 cost per trial activation',
  },
  {
    ch: '04 · Paid performance',
    title: 'Meta + Google UAC',
    body:
      'Tight geo-fence on Kerala + Kochi + Calicut + Trivandrum. Creative variants: trade-call clip with "Get calls like this on your phone" overlay. Day-7 ROAS target of 1.5×.',
    kpi: 'KPI: <₹200 cost per paying subscriber',
  },
  {
    ch: '05 · SEO & content',
    title: 'Blog: "EUR/USD weekly outlook"',
    body:
      'Two long-form posts per week targeting high-intent Kerala + India forex queries. Each post has an in-line CTA and a host-attributed take. Slow build, durable traffic.',
    kpi: 'KPI: 50k organic sessions / month by month 6',
  },
  {
    ch: '06 · Referral loop',
    title: 'In-app "invite a friend"',
    body:
      'Every paying user gets a unique link. Friend gets 7 extra trial days, user gets ₹100 off next month. Caps at 3 successful referrals / month to control margin.',
    kpi: 'KPI: 30% of new trials from referral by month 4',
  },
];

const persona = {
  name: 'Primary persona — Arjun, 26, Kochi',
  bio: 'Day-trader working a 9–5 in IT. Trades XAU/USD and EUR/USD in the London and New York sessions. Currently uses TradingView + a Telegram group of 200 strangers. Pain points: misses entries, signal spam, no audio context.',
  hook:
    '"I just need someone I trust, talking to me, telling me what they are seeing — while I work."',
  cta: 'Trade-call delivery under 1 second, with vibration. Trial in 60 seconds. ₹499/month after.',
};

const pricingTiers = [
  {
    name: 'Free trial',
    price: '₹0',
    period: '3 days',
    tagline: 'No card. Full access.',
    features: ['Live audio + calls', 'Sentiment music', 'Cancel anytime'],
    cta: 'Default for new users',
    highlight: false,
  },
  {
    name: 'Monthly',
    price: '₹499',
    period: '/ month',
    tagline: 'Most popular',
    features: [
      'Everything in trial',
      'Unlimited sessions',
      'Priority audio quality',
      'In-app reactions',
    ],
    cta: 'Default plan after trial',
    highlight: true,
  },
  {
    name: 'Yearly (Phase 3)',
    price: '₹4,999',
    period: '/ year',
    tagline: 'Coming soon',
    features: ['Save 17%', 'Early access to Phase 3 features', 'Priority support'],
    cta: 'Notify me',
    highlight: false,
  },
];

export default function MarketingPage() {
  return (
    <>
      <section className="section" style={{ paddingTop: 80 }}>
        <div className="container">
          <div className="section-head">
            <span className="eyebrow">Marketing plan</span>
            <h1 className="section-title">A go-to-market built for Kerala.</h1>
            <p className="section-sub">
              Forex communities in India live on Telegram and YouTube. Our plan meets traders
              where they already are, then earns the right to bring them into the app.
            </p>
          </div>

          <div className="grid grid-3 stats" style={{ marginTop: 8 }}>
            <div className="stat">
              <div className="n">TAM</div>
              <div className="l" style={{ fontSize: 14, color: 'var(--text)' }}>
                ~3.4M active Indian FX traders
              </div>
            </div>
            <div className="stat">
              <div className="n">SAM</div>
              <div className="l" style={{ fontSize: 14, color: 'var(--text)' }}>
                ~180k Kerala-based part-time traders
              </div>
            </div>
            <div className="stat">
              <div className="n">SOM (Y1)</div>
              <div className="l" style={{ fontSize: 14, color: 'var(--text)' }}>
                5,000 paying subscribers
              </div>
            </div>
          </div>
        </div>
      </section>

      <div className="divider" />

      <section className="section">
        <div className="container">
          <div className="section-head">
            <span className="eyebrow">Persona</span>
            <h2 className="section-title">Who we are selling to.</h2>
          </div>

          <div className="card" style={{ padding: 36 }}>
            <div className="grid grid-2" style={{ gap: 40, alignItems: 'center' }}>
              <div>
                <h3 style={{ fontSize: 24, marginBottom: 8 }}>{persona.name}</h3>
                <p className="muted" style={{ fontSize: 15 }}>
                  {persona.bio}
                </p>
                <div
                  style={{
                    marginTop: 20,
                    padding: 16,
                    background: 'var(--bg-elev)',
                    borderLeft: '3px solid var(--accent)',
                    borderRadius: 6,
                    fontStyle: 'italic',
                    color: 'var(--text)',
                  }}
                >
                  {persona.hook}
                </div>
              </div>
              <div>
                <div className="eyebrow" style={{ marginBottom: 12 }}>
                  Our value, in his words
                </div>
                <h3 style={{ fontSize: 20, lineHeight: 1.4 }}>{persona.cta}</h3>
                <div className="pill-row" style={{ marginTop: 20 }}>
                  <span className="pill">Phone OTP</span>
                  <span className="pill">Sub-second calls</span>
                  <span className="pill">Vibration</span>
                  <span className="pill">UPI</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div className="divider" />

      <section className="section">
        <div className="container">
          <div className="section-head">
            <span className="eyebrow">Channels</span>
            <h2 className="section-title">Six channels, ranked by ROI.</h2>
            <p className="section-sub">
              We start with the cheapest, highest-trust channels (organic + community) and only
              turn on paid once the funnel is measured end-to-end.
            </p>
          </div>

          <div className="mkt-grid">
            {channels.map((c) => (
              <div key={c.title} className="mkt-card">
                <div className="ch">{c.ch}</div>
                <h3>{c.title}</h3>
                <p>{c.body}</p>
                <div
                  style={{
                    marginTop: 14,
                    paddingTop: 12,
                    borderTop: '1px solid var(--border)',
                    fontSize: 12,
                    color: 'var(--accent)',
                    fontWeight: 600,
                  }}
                >
                  {c.kpi}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <div className="divider" />

      <section className="section">
        <div className="container">
          <div className="section-head">
            <span className="eyebrow">Pricing</span>
            <h2 className="section-title">A single monthly plan, with a year tease.</h2>
            <p className="section-sub">
              One plan keeps the funnel simple. We will add a yearly tier in Phase 3 once retention
              is measured.
            </p>
          </div>

          <div className="grid grid-3">
            {pricingTiers.map((t) => (
              <div
                key={t.name}
                className="card"
                style={{
                  borderColor: t.highlight ? 'var(--accent)' : 'var(--border)',
                  boxShadow: t.highlight ? '0 0 40px rgba(245, 180, 0, 0.15)' : 'none',
                  position: 'relative',
                }}
              >
                {t.highlight && (
                  <span
                    style={{
                      position: 'absolute',
                      top: -10,
                      right: 20,
                      background: 'var(--accent)',
                      color: '#0b1220',
                      fontSize: 10,
                      fontWeight: 800,
                      padding: '4px 10px',
                      borderRadius: 999,
                      textTransform: 'uppercase',
                      letterSpacing: '0.06em',
                    }}
                  >
                    Primary
                  </span>
                )}
                <h3 style={{ fontSize: 18, marginBottom: 4 }}>{t.name}</h3>
                <div className="muted" style={{ fontSize: 13, marginBottom: 16 }}>
                  {t.tagline}
                </div>
                <div style={{ display: 'flex', alignItems: 'baseline', gap: 4 }}>
                  <span style={{ fontSize: 36, fontWeight: 800, letterSpacing: '-0.02em' }}>
                    {t.price}
                  </span>
                  <span className="muted" style={{ fontSize: 14 }}>
                    {t.period}
                  </span>
                </div>
                <ul
                  style={{
                    margin: '16px 0',
                    padding: 0,
                    listStyle: 'none',
                    fontSize: 14,
                    color: 'var(--text-muted)',
                  }}
                >
                  {t.features.map((f) => (
                    <li key={f} style={{ marginBottom: 8, paddingLeft: 22, position: 'relative' }}>
                      <span
                        style={{
                          position: 'absolute',
                          left: 0,
                          color: 'var(--success)',
                          fontWeight: 700,
                        }}
                      >
                        ✓
                      </span>
                      {f}
                    </li>
                  ))}
                </ul>
                <button
                  className={t.highlight ? 'btn' : 'btn btn-secondary'}
                  style={{ width: '100%' }}
                >
                  {t.cta}
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      <div className="divider" />

      <section className="section">
        <div className="container">
          <div className="section-head">
            <span className="eyebrow">90-day launch plan</span>
            <h2 className="section-title">From closed beta to public launch.</h2>
          </div>

          <div className="grid grid-3">
            <div className="card">
              <div className="eyebrow" style={{ marginBottom: 8 }}>
                Days 1–30
              </div>
              <h3 style={{ fontSize: 20, marginBottom: 8 }}>Closed beta</h3>
              <p className="muted">
                50 hand-picked traders from partner groups. Daily feedback loop. Ship fixes
                weekly. Set up the analytics + payment funnel end-to-end.
              </p>
            </div>
            <div className="card">
              <div className="eyebrow" style={{ marginBottom: 8 }}>
                Days 31–60
              </div>
              <h3 style={{ fontSize: 20, marginBottom: 8 }}>Soft launch</h3>
              <p className="muted">
                Open the funnel to 500 traders. Influencer collabs go live. Reels cadence
                ramps to 5/week. Aim for 100 paying users.
              </p>
            </div>
            <div className="card">
              <div className="eyebrow" style={{ marginBottom: 8 }}>
                Days 61–90
              </div>
              <h3 style={{ fontSize: 20, marginBottom: 8 }}>Public launch</h3>
              <p className="muted">
                Meta + Google UAC turn on. SEO posts compound. Referral program in app.
                Target: 1,000 paying subscribers and a 70% trial-to-paid rate.
              </p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
