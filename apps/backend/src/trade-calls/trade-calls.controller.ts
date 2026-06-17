import {
  ArrayMinSize,
  IsArray,
  IsEnum,
  IsNumber,
  IsOptional,
  IsString,
  Min,
  MinLength,
} from 'class-validator';
import { Body, Controller, Get, Post, UseGuards } from '@nestjs/common';
import { TradeCallsService } from './trade-calls.service';
import { JwtAuthGuard } from '../auth/jwt.guard';
import { AuthedUser, CurrentUser } from '../auth/current-user.decorator';
import { TradeCall, TradeCallPushRequest } from '@fx-teller/shared-types';

class PushTradeCallDto implements TradeCallPushRequest {
  @IsString()
  sessionId!: string;

  @IsString()
  @MinLength(1)
  instrument!: string;

  @IsEnum(['BUY', 'SELL'])
  side!: 'BUY' | 'SELL';

  @IsNumber()
  @Min(0)
  entry!: number;

  @IsNumber()
  @Min(0)
  sl!: number;

  @IsArray()
  @ArrayMinSize(1)
  @IsNumber({}, { each: true })
  tp!: number[];

  @IsOptional()
  @IsNumber()
  @Min(1000)
  alertDurationMs?: number;
}

@Controller('trade-calls')
export class TradeCallsController {
  constructor(private readonly tradeCalls: TradeCallsService) {}

  @Get('recent')
  async recent(): Promise<TradeCall[]> {
    return this.tradeCalls.listRecent();
  }

  @Post('push')
  @UseGuards(JwtAuthGuard)
  async push(
    @CurrentUser() u: AuthedUser,
    @Body() dto: PushTradeCallDto,
  ): Promise<TradeCall> {
    return this.tradeCalls.push(u.sub, dto);
  }
}
