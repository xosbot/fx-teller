import Link from 'next/link';
import PhoneFrame from './components/PhoneFrame';

export default function HomePage() {
  return (
    <>
      <section className="hero">
        <div className="hero-bg" />
        <div className="container hero-grid">
          <div>
            <span className="eyebrow">v1 MVP · In build</span>
            <h1>
              A live trading room <br />
              that fits in your <span className="accent">pocket.</span>
            </h1>
            <p className="lead">
              FX-Teller is a live podcast trading community for forex traders in Kerala.
              Tune in to live audio commentary, get push trade calls with a long-vibration
              alert, and let the music switch itself when the market gets tense.
            </p>
            <div className="hero-ctas">
              <Link href="/demo" className="btn btn-lg">
                See live demo →
              </Link>
              <Link href="/features" className="btn btn-secondary btn-lg">
                View features
              </Link>
            </div>
            <div className="hero-meta">
              <span>
                <span className="check">✓</span> iOS + Android
              </span>
              <span>
                <span className="check">✓</span> Phone OTP, no password
              </span>
              <span>
                <span className="check">✓</span> UPI payments via Razorpay
              </span>
            </div>
          </div>
          <div>
            <PhoneFrame>
              <div className="screen">
                <div className="live-pill" style={{ marginTop: 24 }}>
                  <span className="live-dot" />
                  LIVE NOW
                </div>
                <div className="screen-title" style={{ marginTop: 14 }}>
                  London Session
                </div>
                <div className="screen-sub">with Rijo · 412 listening</div>

                <div className="audio-wave">
                  <span /><span /><span /><span /><span /><span /><span /><span />
                </div>

                <div className="card-row">
                  <div className="icon">🎙</div>
                  <div className="meta">
                    <b>Live audio</b>
                    <span>Tap to join the room</span>
                  </div>
                </div>
                <div className="card-row">
                  <div className="icon">📈</div>
                  <div className="meta">
                    <b>Next call window</b>
                    <span>EUR/USD · 10 min</span>
                  </div>
                </div>
                <div className="card-row">
                  <div className="icon">🎵</div>
                  <div className="meta">
                    <b>Market sentiment</b>
                    <span>Calm · Muted cues</span>
                  </div>
                </div>

                <button className="btn-block">Join live audio</button>
              </div>
            </PhoneFrame>
          </div>
        </div>
      </section>

      <div className="divider" />

      <section className="section">
        <div className="container">
          <div className="section-head">
            <span className="eyebrow">Why FX-Teller</span>
            <h2 className="section-title">Built for the way Kerala trades.</h2>
            <p className="section-sub">
              Forex moves in seconds. Telegram groups move in minutes. We built the missing
              middle — a real-time audio room with instant trade calls you can&apos;t miss.
            </p>
          </div>
          <div className="stats">
            <div className="stat">
              <div className="n">&lt; 1s</div>
              <div className="l">Trade-call delivery</div>
            </div>
            <div className="stat">
              <div className="n">3 day</div>
              <div className="l">Free trial, no card</div>
            </div>
            <div className="stat">
              <div className="n">2</div>
              <div className="l">Music states, curated</div>
            </div>
            <div className="stat">
              <div className="n">24/7</div>
              <div className="l">Session coverage</div>
            </div>
          </div>
        </div>
      </section>

      <div className="divider" />

      <section className="section">
        <div className="container">
          <div className="section-head">
            <span className="eyebrow">How it works</span>
            <h2 className="section-title">From sign-up to first call in 60 seconds.</h2>
          </div>
          <div className="grid grid-3">
            <div className="step">
              <div className="num">1</div>
              <h4>Verify your phone</h4>
              <p>Enter your mobile, get a 6-digit OTP, done. No passwords, no email.</p>
            </div>
            <div className="step">
              <div className="num">2</div>
              <h4>Start a 3-day trial</h4>
              <p>Full access to live audio and trade calls. No card required, cancel anytime.</p>
            </div>
            <div className="step">
              <div className="num">3</div>
              <h4>Tune in to a session</h4>
              <p>Join the live room, get calls on your lock screen with a long vibration.</p>
            </div>
          </div>
        </div>
      </section>

      <div className="divider" />

      <section className="section">
        <div className="container">
          <div className="section-head">
            <span className="eyebrow">Feature highlights</span>
            <h2 className="section-title">Everything a serious trader needs.</h2>
          </div>
          <div className="grid grid-3">
            <div className="card feature">
              <div className="ico">🎙</div>
              <h3>Live audio room</h3>
              <p>
                100ms-powered low-latency audio. Listen while you work, chat while you trade.
              </p>
            </div>
            <div className="card feature">
              <div className="ico">📳</div>
              <h3>Long-vibration calls</h3>
              <p>
                Trade calls land with a sustained vibration + floating widget. You will not miss
                a setup.
              </p>
            </div>
            <div className="card feature">
              <div className="ico">🎵</div>
              <h3>Sentiment music</h3>
              <p>
                Host switches the music to Alert mode when the market is hot. You feel it before
                you read it.
              </p>
            </div>
            <div className="card feature">
              <div className="ico">🔐</div>
              <h3>Phone OTP, no password</h3>
              <p>Login with a 6-digit code. No email, no password, no friction.</p>
            </div>
            <div className="card feature">
              <div className="ico">💳</div>
              <h3>UPI / Card payments</h3>
              <p>Razorpay handles GPay, PhonePe, Paytm, cards, and netbanking.</p>
            </div>
            <div className="card feature">
              <div className="ico">📱</div>
              <h3>System overlay (Android)</h3>
              <p>
                Trade-call widget floats over any app on Android. iOS gets a full-screen
                in-app modal.
              </p>
            </div>
          </div>
        </div>
      </section>

      <div className="container">
        <div className="banner">
          <h3>Ready to see it in action?</h3>
          <p>Walk through the user flow with our interactive demo. No install needed.</p>
          <Link href="/demo" className="btn btn-lg">
            Launch the live demo →
          </Link>
        </div>
      </div>
    </>
  );
}
