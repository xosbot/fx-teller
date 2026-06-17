'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { Session, TradeCall } from '@fx-teller/shared-types';

const API = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3000/api';

type Sentiment = 'CALM' | 'ALERT';

export default function LiveConsole() {
  const router = useRouter();
  const [token, setToken] = useState<string | null>(null);
  const [session, setSession] = useState<Session | null>(null);
  const [sentiment, setSentiment] = useState<Sentiment>('CALM');
  const [recentCalls, setRecentCalls] = useState<TradeCall[]>([]);
  const [busy, setBusy] = useState(false);

  // Form state
  const [instrument, setInstrument] = useState('XAUUSD');
  const [side, setSide] = useState<'BUY' | 'SELL'>('BUY');
  const [entry, setEntry] = useState('');
  const [sl, setSl] = useState('');
  const [tp, setTp] = useState('');
  const [duration, setDuration] = useState(15000);

  useEffect(() => {
    const t = localStorage.getItem('fxteller_token');
    if (!t) {
      router.push('/');
      return;
    }
    setToken(t);
    refreshCurrent();
    loadRecent();
  }, [router]);

  async function refreshCurrent() {
    const t = localStorage.getItem('fxteller_token');
    const r = await fetch(`${API}/sessions/current`, {
      headers: { Authorization: `Bearer ${t}` },
    });
    if (r.ok) setSession(await r.json());
  }

  async function loadRecent() {
    const r = await fetch(`${API}/trade-calls/recent`);
    if (r.ok) setRecentCalls(await r.json());
  }

  async function startSession() {
    setBusy(true);
    try {
      const t = localStorage.getItem('fxteller_token');
      const r = await fetch(`${API}/sessions/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${t}` },
        body: JSON.stringify({ title: 'Live Session' }),
      });
      if (r.ok) setSession(await r.json());
    } finally {
      setBusy(false);
    }
  }

  async function endSession() {
    if (!session) return;
    setBusy(true);
    try {
      const t = localStorage.getItem('fxteller_token');
      const r = await fetch(`${API}/sessions/${session.id}/end`, {
        method: 'POST',
        headers: { Authorization: `Bearer ${t}` },
      });
      if (r.ok) setSession(await r.json());
    } finally {
      setBusy(false);
    }
  }

  async function pushTradeCall() {
    if (!session) return alert('Start a session first');
    if (!entry || !sl || !tp) return alert('Entry, SL, and TP are required');
    setBusy(true);
    try {
      const t = localStorage.getItem('fxteller_token');
      const r = await fetch(`${API}/trade-calls/push`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${t}` },
        body: JSON.stringify({
          sessionId: session.id,
          instrument,
          side,
          entry: parseFloat(entry),
          sl: parseFloat(sl),
          tp: tp.split(',').map((v) => parseFloat(v.trim())).filter((v) => !isNaN(v)),
          alertDurationMs: duration,
        }),
      });
      if (r.ok) {
        setEntry('');
        setSl('');
        setTp('');
        loadRecent();
      } else {
        alert(await r.text());
      }
    } finally {
      setBusy(false);
    }
  }

  async function setMusicCue(s: Sentiment) {
    if (!session) return alert('Start a session first');
    setBusy(true);
    try {
      const t = localStorage.getItem('fxteller_token');
      const r = await fetch(`${API}/music-cues/set`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${t}` },
        body: JSON.stringify({ sessionId: session.id, sentiment: s }),
      });
      if (r.ok) setSentiment(s);
    } finally {
      setBusy(false);
    }
  }

  function signOut() {
    localStorage.removeItem('fxteller_token');
    localStorage.removeItem('fxteller_user');
    router.push('/');
  }

  return (
    <main style={{ maxWidth: 1100, margin: '0 auto', padding: 24 }}>
      <header className="row" style={{ justifyContent: 'space-between', marginBottom: 24 }}>
        <h1 style={{ margin: 0, fontSize: 24 }}>
          FX<span style={{ color: 'var(--accent)' }}>-Teller</span>{' '}
          <span className="muted" style={{ fontSize: 14, fontWeight: 400 }}>
            Host Console
          </span>
        </h1>
        <button className="btn btn-secondary" onClick={signOut}>
          Sign Out
        </button>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
        {/* Session controls */}
        <div className="card">
          <h2 style={{ marginTop: 0, fontSize: 18 }}>Session</h2>
          {session && session.status === 'LIVE' ? (
            <>
              <p>
                <span className="live-dot" />
                <strong>LIVE</strong> · {session.title}
              </p>
              <p className="muted" style={{ fontSize: 12 }}>
                Session ID: {session.id}
              </p>
              <button className="btn btn-danger" onClick={endSession} disabled={busy}>
                End Session
              </button>
            </>
          ) : (
            <>
              <p className="muted">No active session.</p>
              <button className="btn" onClick={startSession} disabled={busy}>
                Start Live Session
              </button>
            </>
          )}
        </div>

        {/* Music cue */}
        <div className="card">
          <h2 style={{ marginTop: 0, fontSize: 18 }}>Background Music</h2>
          <p className="muted" style={{ fontSize: 13 }}>
            Listeners hear the matching track instantly.
          </p>
          <div className="row">
            <button
              className={`btn ${sentiment !== 'CALM' ? 'btn-secondary' : ''}`}
              onClick={() => setMusicCue('CALM')}
              disabled={busy}
              style={{ flex: 1 }}
            >
              🌊 CALM
            </button>
            <button
              className={`btn ${sentiment !== 'ALERT' ? 'btn-secondary' : ''}`}
              onClick={() => setMusicCue('ALERT')}
              disabled={busy}
              style={{ flex: 1, background: sentiment === 'ALERT' ? 'var(--danger)' : undefined, color: sentiment === 'ALERT' ? 'white' : undefined }}
            >
              ⚡ ALERT
            </button>
          </div>
        </div>

        {/* Trade call form */}
        <div className="card" style={{ gridColumn: 'span 2' }}>
          <h2 style={{ marginTop: 0, fontSize: 18 }}>Push Trade Call</h2>
          <div className="field-row">
            <div className="field" style={{ flex: 1 }}>
              <label className="label">Instrument</label>
              <input
                value={instrument}
                onChange={(e) => setInstrument(e.target.value.toUpperCase())}
                placeholder="XAUUSD"
              />
            </div>
            <div className="field" style={{ width: 120 }}>
              <label className="label">Side</label>
              <select value={side} onChange={(e) => setSide(e.target.value as 'BUY' | 'SELL')}>
                <option>BUY</option>
                <option>SELL</option>
              </select>
            </div>
          </div>
          <div className="field-row">
            <div className="field">
              <label className="label">Entry</label>
              <input
                value={entry}
                onChange={(e) => setEntry(e.target.value)}
                inputMode="decimal"
                placeholder="2340.50"
              />
            </div>
            <div className="field">
              <label className="label">Stop Loss</label>
              <input
                value={sl}
                onChange={(e) => setSl(e.target.value)}
                inputMode="decimal"
                placeholder="2335.00"
              />
            </div>
            <div className="field">
              <label className="label">Take Profit (comma-sep)</label>
              <input
                value={tp}
                onChange={(e) => setTp(e.target.value)}
                inputMode="decimal"
                placeholder="2350, 2355"
              />
            </div>
          </div>
          <div className="field">
            <label className="label">Alert Duration (ms)</label>
            <input
              type="number"
              step="1000"
              min="5000"
              max="60000"
              value={duration}
              onChange={(e) => setDuration(parseInt(e.target.value, 10))}
            />
          </div>
          <button
            className="btn"
            onClick={pushTradeCall}
            disabled={busy || !session || session.status !== 'LIVE'}
          >
            🔔 Push Trade Call
          </button>
        </div>

        {/* Recent calls */}
        <div className="card" style={{ gridColumn: 'span 2' }}>
          <h2 style={{ marginTop: 0, fontSize: 18 }}>Recent Trade Calls</h2>
          {recentCalls.length === 0 ? (
            <p className="muted">No calls yet.</p>
          ) : (
            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 14 }}>
              <thead>
                <tr style={{ textAlign: 'left', color: 'var(--text-muted)' }}>
                  <th style={{ padding: 8 }}>Time</th>
                  <th style={{ padding: 8 }}>Instrument</th>
                  <th style={{ padding: 8 }}>Side</th>
                  <th style={{ padding: 8 }}>Entry</th>
                  <th style={{ padding: 8 }}>SL</th>
                  <th style={{ padding: 8 }}>TP</th>
                </tr>
              </thead>
              <tbody>
                {recentCalls.map((c) => (
                  <tr key={c.id} style={{ borderTop: '1px solid var(--border)' }}>
                    <td style={{ padding: 8 }} className="muted">
                      {new Date(c.pushedAt).toLocaleTimeString()}
                    </td>
                    <td style={{ padding: 8, fontWeight: 600 }}>{c.instrument}</td>
                    <td
                      style={{
                        padding: 8,
                        color: c.side === 'BUY' ? 'var(--success)' : 'var(--danger)',
                      }}
                    >
                      {c.side}
                    </td>
                    <td style={{ padding: 8 }}>{c.entry}</td>
                    <td style={{ padding: 8 }}>{c.sl}</td>
                    <td style={{ padding: 8 }}>{c.tp.join(', ')}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </main>
  );
}
