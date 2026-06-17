import { Inject, Injectable, NotFoundException } from '@nestjs/common';
import { Pool } from 'pg';
import { PG_POOL } from '../database/database.module';
import { User, SubscriptionStatus } from '@fx-teller/shared-types';
import { v4 as uuid } from 'uuid';
import { env } from '../env';

interface UserRow {
  id: string;
  phone: string;
  name: string | null;
  role: 'listener' | 'host';
  trial_ends_at: Date | null;
  subscription: SubscriptionStatus;
  sub_ends_at: Date | null;
  rzp_customer_id: string | null;
  rzp_subscription_id: string | null;
  created_at: Date;
}

@Injectable()
export class UsersService {
  constructor(@Inject(PG_POOL) private readonly pool: Pool) {}

  async findOrCreateByPhone(phone: string): Promise<User> {
    const existing = await this.pool.query<UserRow>(
      `SELECT * FROM users WHERE phone = $1`,
      [phone],
    );
    if (existing.rows[0]) {
      await this.refreshSubscriptionState(existing.rows[0]);
      const fresh = await this.pool.query<UserRow>(
        `SELECT * FROM users WHERE id = $1`,
        [existing.rows[0].id],
      );
      return this.toUser(fresh.rows[0]);
    }
    const id = uuid();
    const trialEnds = new Date(Date.now() + env.trialDays * 24 * 60 * 60 * 1000);
    const inserted = await this.pool.query<UserRow>(
      `INSERT INTO users (id, phone, role, trial_ends_at, subscription)
       VALUES ($1, $2, 'listener', $3, 'trialing')
       RETURNING *`,
      [id, phone, trialEnds],
    );
    return this.toUser(inserted.rows[0]);
  }

  async findById(id: string): Promise<User | null> {
    const r = await this.pool.query<UserRow>(`SELECT * FROM users WHERE id = $1`, [id]);
    return r.rows[0] ? this.toUser(r.rows[0]) : null;
  }

  async findByPhone(phone: string): Promise<User | null> {
    const r = await this.pool.query<UserRow>(
      `SELECT * FROM users WHERE phone = $1`,
      [phone],
    );
    return r.rows[0] ? this.toUser(r.rows[0]) : null;
  }

  async updateName(id: string, name: string): Promise<User> {
    const r = await this.pool.query<UserRow>(
      `UPDATE users SET name = $2, updated_at = now() WHERE id = $1 RETURNING *`,
      [id, name],
    );
    if (!r.rows[0]) throw new NotFoundException('User not found');
    return this.toUser(r.rows[0]);
  }

  async setRole(id: string, role: 'listener' | 'host'): Promise<void> {
    await this.pool.query(
      `UPDATE users SET role = $2, updated_at = now() WHERE id = $1`,
      [id, role],
    );
  }

  async setRazorpayCustomer(id: string, customerId: string): Promise<void> {
    await this.pool.query(
      `UPDATE users SET rzp_customer_id = $2, updated_at = now() WHERE id = $1`,
      [id, customerId],
    );
  }

  async updateSubscription(
    id: string,
    status: SubscriptionStatus,
    subEndsAt: Date | null,
    rzpSubscriptionId: string | null,
  ): Promise<void> {
    await this.pool.query(
      `UPDATE users SET subscription = $2, sub_ends_at = $3, rzp_subscription_id = COALESCE($4, rzp_subscription_id), updated_at = now() WHERE id = $1`,
      [id, status, subEndsAt, rzpSubscriptionId],
    );
  }

  private async refreshSubscriptionState(row: UserRow): Promise<void> {
    if (row.subscription === 'trialing' && row.trial_ends_at) {
      if (new Date(row.trial_ends_at).getTime() < Date.now()) {
        await this.pool.query(
          `UPDATE users SET subscription = 'expired', updated_at = now() WHERE id = $1`,
          [row.id],
        );
      }
    }
  }

  private toUser(row: UserRow): User {
    return {
      id: row.id,
      phone: row.phone,
      name: row.name ?? '',
      role: row.role,
      trialEndsAt: row.trial_ends_at ? row.trial_ends_at.toISOString() : null,
      subscription: row.subscription,
      subscriptionEndsAt: row.sub_ends_at ? row.sub_ends_at.toISOString() : null,
      createdAt: row.created_at.toISOString(),
    };
  }
}
