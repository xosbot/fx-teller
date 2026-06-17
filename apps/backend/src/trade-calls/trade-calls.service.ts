import { Inject, Injectable, NotFoundException } from '@nestjs/common';
import { Pool } from 'pg';
import { Subject } from 'rxjs';
import { PG_POOL } from '../database/database.module';
import { EVENT_BUS, AppEvent } from '../events/events.module';
import { TradeCall, TradeCallPushRequest } from '@fx-teller/shared-types';
import { v4 as uuid } from 'uuid';
import { SessionsService } from '../sessions/sessions.service';

interface TradeCallRow {
  id: string;
  session_id: string;
  host_id: string;
  instrument: string;
  side: 'BUY' | 'SELL';
  entry: string; // pg NUMERIC returns string
  sl: string;
  tp: string[];
  pushed_at: Date;
  expires_at: Date;
  alert_ms: number;
}

@Injectable()
export class TradeCallsService {
  constructor(
    @Inject(PG_POOL) private readonly pool: Pool,
    @Inject(EVENT_BUS) private readonly bus: Subject<AppEvent>,
    private readonly sessions: SessionsService,
  ) {}

  async push(
    hostId: string,
    dto: TradeCallPushRequest,
  ): Promise<TradeCall> {
    const session = await this.sessions.getById(dto.sessionId);
    if (session.status === 'ENDED')
      throw new NotFoundException('Session has ended');

    const id = uuid();
    const expiresAt = new Date(
      Date.now() + (dto.alertDurationMs ?? 15000) + 60 * 1000,
    );
    const r = await this.pool.query<TradeCallRow>(
      `INSERT INTO trade_calls (id, session_id, host_id, instrument, side, entry, sl, tp, expires_at, alert_ms)
       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
       RETURNING *`,
      [
        id,
        dto.sessionId,
        hostId,
        dto.instrument.toUpperCase(),
        dto.side,
        dto.entry,
        dto.sl,
        dto.tp,
        expiresAt,
        dto.alertDurationMs ?? 15000,
      ],
    );
    const tc = this.toTradeCall(r.rows[0]);
    this.bus.next({ type: 'trade_call', payload: tc });
    return tc;
  }

  async listRecent(limit = 20): Promise<TradeCall[]> {
    const r = await this.pool.query<TradeCallRow>(
      `SELECT * FROM trade_calls ORDER BY pushed_at DESC LIMIT $1`,
      [limit],
    );
    return r.rows.map((row) => this.toTradeCall(row));
  }

  async listForSession(sessionId: string, limit = 50): Promise<TradeCall[]> {
    const r = await this.pool.query<TradeCallRow>(
      `SELECT * FROM trade_calls WHERE session_id = $1 ORDER BY pushed_at DESC LIMIT $2`,
      [sessionId, limit],
    );
    return r.rows.map((row) => this.toTradeCall(row));
  }

  private toTradeCall(row: TradeCallRow): TradeCall {
    return {
      id: row.id,
      sessionId: row.session_id,
      hostId: row.host_id,
      instrument: row.instrument,
      side: row.side,
      entry: parseFloat(row.entry),
      sl: parseFloat(row.sl),
      tp: row.tp.map((v) => parseFloat(v)),
      pushedAt: row.pushed_at.toISOString(),
      expiresAt: row.expires_at.toISOString(),
    };
  }
}
