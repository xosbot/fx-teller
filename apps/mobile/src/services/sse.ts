// Server-Sent Events client. Subscribes to /api/events/stream and exposes
// typed callbacks for trade_call, music_cue, and session_state events.

import { API_URL } from '../config';
import { TradeCall, MusicCue, Session } from '@fx-teller/shared-types';

type Listener = (data: any) => void;

export class SseClient {
  private es: EventSource | null = null;

  start(handlers: {
    onTradeCall?: (c: TradeCall) => void;
    onMusicCue?: (c: MusicCue) => void;
    onSessionState?: (s: Session | null) => void;
  }) {
    if (this.es) return;
    // Note: EventSource is a browser API. RN doesn't ship it natively.
    // For the real implementation, swap to react-native-sse or a manual
    // fetch stream. We provide the wiring here and call it out clearly.
    // In v1 mobile build, server-pushed events arrive via 100ms data
    // channel (preferred) OR a manual streaming fetch.
    // For now this is a stub that will be replaced at integration time.
    if (typeof EventSource !== 'undefined') {
      this.es = new EventSource(`${API_URL}/events/stream`);
      this.es.addEventListener('trade_call', (e: MessageEvent) => {
        handlers.onTradeCall?.(JSON.parse(e.data));
      });
      this.es.addEventListener('music_cue', (e: MessageEvent) => {
        handlers.onMusicCue?.(JSON.parse(e.data));
      });
      this.es.addEventListener('session_state', (e: MessageEvent) => {
        handlers.onSessionState?.(JSON.parse(e.data));
      });
    } else {
      // eslint-disable-next-line no-console
      console.warn('EventSource not available; use 100ms data channel instead');
    }
  }

  stop() {
    this.es?.close();
    this.es = null;
  }
}

export const sse = new SseClient();
