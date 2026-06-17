import { Injectable, Logger } from '@nestjs/common';
import Razorpay from 'razorpay';
import { env } from '../env';
import { UsersService } from '../users/users.service';

@Injectable()
export class SubscriptionsService {
  private readonly logger = new Logger(SubscriptionsService.name);
  private readonly rzp: Razorpay;

  constructor(private readonly users: UsersService) {
    this.rzp = new Razorpay({
      key_id: env.rzpKeyId,
      key_secret: env.rzpKeySecret,
    });
  }

  /**
   * Create a Razorpay subscription. v1 trial is enforced at app-level (3 days),
   * so we create the subscription in "created" state with no `start_at` offset
   * — the user is charged immediately upon authentication. To make it a real
   * trial, set `start_at` to now + 3 days.
   *
   * For the simplest path, we tie the auth to trial behaviour: we create the
   * subscription with start_at = now + trial, and the webhook flips the user
   * to "active" when `subscription.activated` fires (post-trial first charge).
   */
  async createSubscription(userId: string, planId: string) {
    let user = await this.users.findById(userId);
    if (!user) throw new Error('User not found');

    // Reuse customer if we already created one
    let customerId = (user as unknown as { rzp_customer_id?: string }).rzp_customer_id;
    if (!customerId) {
      const customer = await this.rzp.customers.create({
        name: user.name || 'FX-Teller User',
        contact: user.phone,
      });
      customerId = customer.id;
      await this.users.setRazorpayCustomer(userId, customerId);
    }

    const startAt = Math.floor(Date.now() / 1000) + env.trialDays * 24 * 3600;
    const sub = await this.rzp.subscriptions.create({
      plan_id: planId,
      customer_notify: 1,
      start_at: startAt,
      total_count: 12,
      notes: { user_id: userId },
    });

    return { subscriptionId: sub.id, customerId, planId, startAt };
  }

  getKeyId(): string {
    return env.rzpKeyId;
  }

  getPlanMonthly(): string {
    return env.rzpPlanMonthly;
  }
}
