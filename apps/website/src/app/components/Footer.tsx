import Link from 'next/link';

export default function Footer() {
  return (
    <footer className="site-footer">
      <div className="container">
        <div className="footer-grid">
          <div>
            <Link href="/" className="brand" style={{ marginBottom: 12 }}>
              <span className="dot" />
              FX<b>-Teller</b>
            </Link>
            <p style={{ marginTop: 12, fontSize: 14 }}>
              A live podcast trading community built for forex traders in Kerala, India. Real-time
              audio, push trade calls, and sentiment-driven cues — all in one app.
            </p>
          </div>
          <div>
            <h4>Product</h4>
            <Link href="/features">Features</Link>
            <Link href="/app-preview">App UI</Link>
            <Link href="/demo">Live Demo</Link>
            <Link href="/roadmap">Roadmap</Link>
          </div>
          <div>
            <h4>Company</h4>
            <Link href="/marketing">Marketing Plan</Link>
            <Link href="/roadmap">Development Plan</Link>
            <a href="mailto:ops@fxteller.app">Contact</a>
          </div>
          <div>
            <h4>Stack</h4>
            <span className="pill" style={{ marginBottom: 6, display: 'inline-block' }}>
              Expo RN
            </span>{' '}
            <span className="pill" style={{ marginBottom: 6, display: 'inline-block' }}>
              NestJS
            </span>{' '}
            <span className="pill" style={{ marginBottom: 6, display: 'inline-block' }}>
              100ms
            </span>{' '}
            <span className="pill" style={{ marginBottom: 6, display: 'inline-block' }}>
              Razorpay
            </span>
          </div>
        </div>
        <div className="footer-bottom">
          <span>© {new Date().getFullYear()} FX-Teller. All rights reserved.</span>
          <span className="dim">Built for traders. Crafted in Kerala.</span>
        </div>
      </div>
    </footer>
  );
}
