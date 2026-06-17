import { Module } from '@nestjs/common';
import { TradeCallsService } from './trade-calls.service';
import { TradeCallsController } from './trade-calls.controller';
import { SessionsModule } from '../sessions/sessions.module';
import { EventsModule } from '../events/events.module';

@Module({
  imports: [SessionsModule, EventsModule],
  controllers: [TradeCallsController],
  providers: [TradeCallsService],
  exports: [TradeCallsService],
})
export class TradeCallsModule {}
