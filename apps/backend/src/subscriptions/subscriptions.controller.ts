import { Body, Controller, Post, UseGuards } from '@nestjs/common';
import { IsString } from 'class-validator';
import { SubscriptionsService } from './subscriptions.service';
import { JwtAuthGuard } from '../auth/jwt.guard';
import { AuthedUser, CurrentUser } from '../auth/current-user.decorator';
import { SubscriptionCreateRequest } from '@fx-teller/shared-types';

class CreateSubDto implements SubscriptionCreateRequest {
  @IsString()
  planId!: string;
}

@Controller('subscriptions')
@UseGuards(JwtAuthGuard)
export class SubscriptionsController {
  constructor(private readonly subs: SubscriptionsService) {}

  @Post('create')
  async create(@CurrentUser() u: AuthedUser, @Body() dto: CreateSubDto) {
    const result = await this.subs.createSubscription(u.sub, dto.planId);
    return {
      ...result,
      keyId: this.subs.getKeyId(),
    };
  }

  @Get('config')
  config() {
    return {
      keyId: this.subs.getKeyId(),
      planMonthly: this.subs.getPlanMonthly(),
      trialDays: 3,
    };
  }
}
