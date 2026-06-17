import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { ScheduleModule } from '@nestjs/schedule';
import { DatabaseModule } from './database/database.module';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';
import { SessionsModule } from './sessions/sessions.module';
import { TradeCallsModule } from './trade-calls/trade-calls.module';
import { MusicCuesModule } from './music-cues/music-cues.module';
import { SubscriptionsModule } from './subscriptions/subscriptions.module';
import { HmsModule } from './hms/hms.module';
import { HealthController } from './health/health.controller';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    ScheduleModule.forRoot(),
    DatabaseModule,
    AuthModule,
    UsersModule,
    SessionsModule,
    HmsModule,
    TradeCallsModule,
    MusicCuesModule,
    SubscriptionsModule,
  ],
  controllers: [HealthController],
})
export class AppModule {}
