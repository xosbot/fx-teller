import { Inject, Injectable, NotFoundException } from '@nestjs/common';
import { Pool } from 'pg';
import { PG_POOL } from '../database/database.module';
import { Session } from '@fx-teller/shared-types';
import { v4 as uuid } from 'uuid';

interface SessionRow {
  id: string;
  title: string;
  host_name: string;
  host_id: string | null;
  starts_at: Date;
  status: 'UPCOMING' | 'LIVE' | 'ENDED';
  started_at: Date | null;
  ended_at: Date | null;
  created_at: Date;
}

@Injectable()
export class SessionsService {
  constructor(@Inject(PG_POOL) private readonly pool: Pool) {}

  async listUpcoming(limit = 10): Promise<Session[]> {
    const r = await this.pool.query<SessionRow>(
      `SELECT * FROM sessions WHERE status IN ('UPCOMING', 'LIVE')
       ORDER BY starts_at ASC LIMIT $1`,
      [limit],
    );
    return r.rows.map((row) => this.toSession(row));
  }

  async getCurrent(): Promise<Session | null> {
    const r = await this.pool.query<SessionRow>(
      `SELECT * FROM sessions WHERE status = 'LIVE' ORDER BY started_at DESC LIMIT 1`,
    );
    return r.rows[0] ? this.toSession(r.rows[0]) : null;
  }

  async getById(id: string): Promise<Session> {
    const r = await this.pool.query<SessionRow>(
      `SELECT * FROM sessions WHERE id = $1`,
      [id],
    );
    if (!r.rows[0]) throw new NotFoundException('Session not found');
    return this.toSession(r.rows[0]);
  }

  async create(input: {
    title: string;
    hostName: string;
    hostId: string;
    startsAt?: Date;
  }): Promise<Session> {
    const id = uuid();
    const startsAt = input.startsAt ?? new Date(Date.now() + 60 * 60 * 1000);
    const r = await this.pool.query<SessionRow>(
      `INSERT INTO sessions (id, title, host_name, host_id, starts_at, status)
       VALUES ($1, $2, $3, $4, $5, 'UPCOMING') RETURNING *`,
      [id, input.title, input.hostName, input.hostId, startsAt],
    );
    return this.toSession(r.rows[0]);
  }

  async start(id: string): Promise<Session> {
    const r = await this.pool.query<SessionRow>(
      `UPDATE sessions SET status = 'LIVE', started_at = now() WHERE id = $1 RETURNING *`,
      [id],
    );
    if (!r.rows[0]) throw new NotFoundException('Session not found');
    return this.toSession(r.rows[0]);
  }

  async end(id: string): Promise<Session> {
    const r = await this.pool.query<SessionRow>(
      `UPDATE sessions SET status = 'ENDED', ended_at = now() WHERE id = $1 RETURNING *`,
      [id],
    );
    if (!r.rows[0]) throw new NotFoundException('Session not found');
    return this.toSession(r.rows[0]);
  }

  private toSession(row: SessionRow): Session {
    return {
      id: row.id,
      title: row.title,
      hostName: row.host_name,
      startsAt: row.starts_at.toISOString(),
      status: row.status,
    };
  }
}
