import { Inject, Injectable } from '@nestjs/common';
import { Pool } from 'pg';
import { Subject } from 'rxjs';
import { PG_POOL } from '../database/database.module';
import { EVENT_BUS, AppEvent } from '../events/events.module';
import {
  MusicCue,
  MusicCueSetRequest,
  Sentiment,
} from '@fx-teller/shared-types';
import { v4 as uuid } from 'uuid';

const TRACKS: Record<Sentiment, string> = {
  CALM: 'Still Water',
  ALERT: 'Sharp Edge',
};

@Injectable()
export class MusicCuesService {
  constructor(
    @Inject(PG_POOL) private readonly pool: Pool,
    @Inject(EVENT_BUS) private readonly bus: Subject<AppEvent>,
  ) {}

  async set(hostId: string, dto: MusicCueSetRequest): Promise<MusicCue> {
    const id = uuid();
    const trackName = TRACKS[dto.sentiment];
    const r = await this.pool.query<{ id: string; sentiment: Sentiment; track_name: string; set_at: Date }>(
      `INSERT INTO music_cues (id, session_id, sentiment, track_name)
       VALUES ($1, $2, $3, $4)
       RETURNING id, sentiment, track_name, set_at`,
      [id, dto.sessionId, dto.sentiment, trackName],
    );
    const row = r.rows[0];
    const cue: MusicCue = {
      sentiment: row.sentiment,
      trackName: row.track_name,
      setAt: row.set_at.toISOString(),
    };
    this.bus.next({ type: 'music_cue', payload: cue });
    return cue;
  }

  async getCurrent(): Promise<MusicCue> {
    const r = await this.pool.query<{ sentiment: Sentiment; track_name: string; set_at: Date }>(
      `SELECT sentiment, track_name, set_at FROM music_cues
       ORDER BY set_at DESC LIMIT 1`,
    );
    const row = r.rows[0];
    if (!row) {
      return { sentiment: 'CALM', trackName: TRACKS.CALM, setAt: new Date().toISOString() };
    }
    return {
      sentiment: row.sentiment,
      trackName: row.track_name,
      setAt: row.set_at.toISOString(),
    };
  }
}
