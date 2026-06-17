// Razorpay webhook handler. Verifies HMAC signature, then processes events.
// We use the raw body parser (configured in main.ts) to verify the signature.

import {
  BadRequestException,
  Controller,
  Headers,
  Inject,
  Logger,
  Post,
  Req,
} from '@nestjs/common';
import { Request } from 'express';
import { createHmac, timingSafeEqual } from 'crypto';
import { Pool } from 'pg';
import { PG_POOL } from '../database/database.module';
import { UsersService } from '../users/users.service';
import { env } from '../env';
import { SubscriptionStatus } from '@fx-teller/shared-types';

interface RazorpaySubscriptionEntity {
  id: string;
  status: string;
  notes: { user_id: string };
  current_end?: number;
}

@Controller('webhooks')
export class RazorpayWebhookController {
  private readonly logger = new Logger(RazorpayWebhookController.name);

  constructor(
    @Inject(PG_POOL) private readonly pool: Pool,
    private readonly users: UsersService,
  ) {}

  @Post('razorpay')
  async handle(
    @Req() req: Request,
    @Headers('x-razorpay-signature') signature: string,
    @Headers('x-razorpay-event-id') eventId: string,
  ) {
    const raw = (req as Request & { rawBody?: Buffer }).rawBody;
    if (!raw) throw new BadRequestException('Missing raw body');

    const expected = createHmac('sha256', env.rzpWebhookSecret)
      .update(raw)
      .digest('hex');
    if (
      !signature ||
      signature.length !== expected.length ||
      !timingSafeEqual(Buffer.from(signature), Buffer.from(expected))
    ) {
      throw new BadRequestException('Invalid signature');
    }

    if (!eventId) throw new BadRequestException('Missing event id');

    // Idempotency: ignore if we've already processed this event.
    const seen = await this.pool.query(
      `SELECT 1 FROM webhook_events WHERE event_id = $1`,
      [eventId],
    );
    if (seen.rows.length) return { ok: true, dedup: true };

    const event = JSON.parse(raw.toString('utf8')) as {
      event: string;
      payload: { subscription: { entity: RazorpaySubscriptionEntity } };
    };
    const sub = event.payload?.subscription?.entity;
    if (!sub?.notes?.user_id) {
      this.logger.warn(`Webhook missing user_id: ${event.event}`);
      return { ok: true };
    }

    const userId = sub.notes.user_id;
    const subEndsAt = sub.current_end ? new Date(sub.current_end * 1000) : null;

    let newStatus: SubscriptionStatus | null = null;
    switch (event.event) {
      case 'subscription.authenticated':
      case 'subscription.created':
        // Subscription mandate is in place; trial still active.
        break;
      case 'subscription.activated':
        newStatus = 'active';
        break;
      case 'subscription.charged':
        newStatus = 'active';
        break;
      case 'subscription.cancelled':
      case 'subscription.completed':
        newStatus = 'expired';
        break;
      case 'subscription.halted':
        newStatus = 'expired';
        break;
      default:
        this.logger.log(`Unhandled razorpay event: ${event.event}`);
    }

    if (newStatus) {
      await this.users.updateSubscription(userId, newStatus, subEndsAt, sub.id);
    }

    await this.pool.query(
      `INSERT INTO webhook_events (event_id, source) VALUES ($1, 'razorpay')`,
      [eventId],
    );

    return { ok: true };
  }
}
