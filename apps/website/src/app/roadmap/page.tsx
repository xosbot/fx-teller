type Phase = {
  status: 'done' | 'now' | 'next' | 'later';
  label: string;
  title: string;
  body: string;
  bullets: string[];
};

const phases: Phase[] = [
  {
    status: 'done',
    label: 'Phase 0',
    title: 'Foundation & design',
    body: 'Architecture, design tokens, infra, and the monorepo skeleton. The boring work that makes shipping fast.',
    bullets: [
      'Turbo + pnpm monorepo (apps/backend, host-console, mobile, shared-types, website)',
      'NestJS modules: auth, users, sessions, hms, trade-calls, music-cues, events, subscriptions, health',
      'Postgres 16 schema + migrations',
      'Docker Compose with SWAG reverse proxy',
      'Brand identity, color tokens, phone-frame design system',
    ],
  },
  {
    status: 'now',
    label: 'Phase 1',
    title: 'v1 MVP — live audio + trade calls',
    body: 'A single host streams live audio commentary and pushes trade calls. Listeners hear commentary and feel calls on their phone.',
    bullets: [
      'Phone OTP auth (in-app) + JWT session',
      '100ms token minting (host / listener roles)',
      'Live audio room (mobile + host console)',
      'Trade-call push with long-vibration + floating widget (Android) / in-app modal (iOS)',
      'Music cue switching: Calm ↔ Alert with crossfade',
      'Server-Sent Events broadcast bus',
      'Razorpay monthly subscription (₹499) + webhook',
      '3-day trial, no card',
      'EAS Build pipeline for iOS + Android',
      'OVH VPS deploy script + daily backups',
    ],
  },
  {
    status: 'next',
    label: 'Phase 2',
    title: 'Retention & community',
    body: 'Once the v1 loop works, deepen retention. Add lightweight community features and personalisation.',
    bullets: [
      'In-app chat over the 100ms data channel',
      'Pinned-message system from the host',
      'Reactions on live calls (🔥 👀 💯)',
      'Personal call history + per-pair performance stats',
      'Push notifications when a session is about to start',
      'Referral program (₹100 off for both parties)',
    ],
  },
  {
    status: 'later',
    label: 'Phase 3',
    title: 'Scale & monetisation',
    body: 'Wider distribution, multi-host support, and the platform features that make this a real business.',
    bullets: [
      'Multi-host marketplace (apply + approval flow)',
      'Revenue split with hosts (Razorpay Route)',
      'Yearly plan + team / family plans',
      'iOS Live Activity + Android persistent notification',
      'Live translation (English ↔ Malayalam) over 100ms',
      'Public landing pages per host (SEO)',
      'Analytics dashboard (Mixpanel / PostHog)',
      'Public API + webhooks for partner brokers',
    ],
  },
];

const statusToTag: Record<Phase['status'], string> = {
  done: 'tag-done',
  now: 'tag-live',
  next: 'tag-soon',
  later: 'tag',
};

const statusToLabel: Record<Phase['status'], string> = {
  done: 'Complete',
  now: 'In build',
  next: 'Next up',
  later: 'Later',
};

export default function RoadmapPage() {
  return (
    <section className="section" style={{ paddingTop: 80 }}>
      <div className="container">
        <div className="section-head">
          <span className="eyebrow">Development plan</span>
          <h1 className="section-title">A focused 4-phase build.</h1>
          <p className="section-sub">
            We deliberately cut the original scope to ship a tight v1, then layer on community
            and monetisation once the core loop is validated.
          </p>
        </div>

        <div className="timeline" style={{ marginTop: 40 }}>
          {phases.map((p) => (
            <div className="timeline-item" key={p.label}>
              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 12,
                  marginBottom: 6,
                }}
              >
                <span className="when">{p.label}</span>
                <span className={`tag ${statusToTag[p.status]}`}>
                  {statusToLabel[p.status]}
                </span>
              </div>
              <h4>{p.title}</h4>
              <p>{p.body}</p>
              <ul style={{ margin: '12px 0 0', paddingLeft: 20, color: 'var(--text-muted)' }}>
                {p.bullets.map((b) => (
                  <li key={b} style={{ marginBottom: 4 }}>
                    {b}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="section-head" style={{ marginTop: 80 }}>
          <span className="eyebrow">v1 scope</span>
          <h2 className="section-title">What we cut to ship fast.</h2>
          <p className="section-sub">
            Every cut below is a deliberate trade-off. We document them so the client knows what
            to expect from v1 and what comes later.
          </p>
        </div>

        <div className="compare">
          <div className="h">Capability</div>
          <div className="h">Original plan</div>
          <div className="h ours">v1 choice</div>

          <div>In-app chat</div>
          <div>WebSocket, full chat</div>
          <div>Deferred to Phase 2</div>

          <div>Music states</div>
          <div>5 curated states</div>
          <div>2 states (Calm / Alert)</div>

          <div>iOS delivery</div>
          <div>Live Activity</div>
          <div>In-app full-screen modal</div>

          <div>Trial</div>
          <div>With card, prorated</div>
          <div>3 days, no card</div>

          <div>Plans</div>
          <div>Monthly + Yearly</div>
          <div>Monthly only (₹499)</div>

          <div>Design system</div>
          <div>Full tokens + components</div>
          <div>Wordmark + 1 accent</div>

          <div>Roles</div>
          <div>Listener + Host + Moderator</div>
          <div>Listener + Host only</div>
        </div>

        <div className="section-head" style={{ marginTop: 80 }}>
          <span className="eyebrow">Engineering principles</span>
          <h2 className="section-title">How we are building it.</h2>
        </div>

        <div className="grid grid-3">
          <div className="card">
            <h3>Ship the loop first</h3>
            <p className="muted">
              Auth → join room → hear call → take trade. Everything else is a multiplier on this
              loop, not a replacement for it.
            </p>
          </div>
          <div className="card">
            <h3>Server-enforced access</h3>
            <p className="muted">
              Subscriptions, trial windows, and host-only endpoints are all checked on the
              NestJS server. The client is a thin view.
            </p>
          </div>
          <div className="card">
            <h3>Boring infra, sharp UX</h3>
            <p className="muted">
              SWAG + Postgres + Docker + a single VPS. The budget goes into the audio pipeline and
              the Android overlay, not into k8s.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
