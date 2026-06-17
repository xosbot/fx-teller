import LoginForm from './LoginForm';

export default function LoginPage() {
  return (
    <main style={{ maxWidth: 420, margin: '10vh auto', padding: 24 }}>
      <div style={{ textAlign: 'center', marginBottom: 32 }}>
        <h1 style={{ margin: 0, fontSize: 32, letterSpacing: '-0.02em' }}>
          FX<span style={{ color: 'var(--accent)' }}>-Teller</span>
        </h1>
        <p className="muted" style={{ marginTop: 8 }}>
          Host Console
        </p>
      </div>
      <div className="card">
        <LoginForm />
      </div>
    </main>
  );
}
