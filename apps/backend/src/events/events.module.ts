// Lightweight in-process pub/sub for broadcasting server events (trade calls, music cues)
// to mobile clients via SSE. In v1 we don't need Redis pub/sub; a single backend process
// is fine. When we scale horizontally, swap for Redis.

import { Global, Module } from '@nestjs/common';
import { Subject } from 'rxjs';
import { EventsController } from './events.controller';

export type AppEvent =
  | { type: 'trade_call'; payload: unknown }
  | { type: 'music_cue'; payload: unknown }
  | { type: 'session_state'; payload: unknown };

export const EVENT_BUS = 'EVENT_BUS';

@Global()
@Module({
  controllers: [EventsController],
  providers: [
    {
      provide: EVENT_BUS,
      useFactory: () => new Subject<AppEvent>(),
    },
  ],
  exports: [EVENT_BUS],
})
export class EventsModule {}
