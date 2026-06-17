import { TradeCall, MusicCue, Session, Sentiment } from '@fx-teller/shared-types';
import { API_URL } from '../config';
import { authedFetch } from './auth';

export async function fetchCurrentSession(): Promise<Session | null> {
  const r = await fetch(`${API_URL}/sessions/current`);
  if (!r.ok) return null;
  return r.json();
}

export async function fetchUpcomingSessions(): Promise<Session[]> {
  return authedFetch('/sessions');
}

export async function fetchRecentTradeCalls(limit = 10): Promise<TradeCall[]> {
  const r = await fetch(`${API_URL}/trade-calls/recent?limit=${limit}`);
  if (!r.ok) return [];
  return r.json();
}

export async function fetchCurrentMusicCue(): Promise<MusicCue> {
  const r = await fetch(`${API_URL}/music-cues/current`);
  if (!r.ok) return { sentiment: 'CALM' as Sentiment, trackName: 'Still Water', setAt: new Date().toISOString() };
  return r.json();
}

export async function getHmsToken(): Promise<{ token: string; roomId: string }> {
  return authedFetch('/hms/token');
}
