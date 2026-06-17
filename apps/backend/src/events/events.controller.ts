import { Controller, Sse, MessageEvent } from '@nestjs/common';
import { Observable, Subject, filter, map, merge } from 'rxjs';
import { Inject } from '@nestjs/common';
import { EVENT_BUS, AppEvent } from '../events/events.module';
import { SessionsService } from '../sessions/sessions.service';

@Controller('events')
export class EventsController {
  private readonly clientStreams = new Subject<MessageEvent>();

  constructor(
    @Inject(EVENT_BUS) private readonly bus: Subject<AppEvent>,
    private readonly sessions: SessionsService,
  ) {}

  @Sse('stream')
  stream(): Observable<MessageEvent> {
    // Per-connection: tap into the shared bus, transform to SSE.
    // We use a per-client Subject so we can also close cleanly.
    const local = new Subject<MessageEvent>();
    const sub = this.bus.subscribe((e: AppEvent) => {
      local.next({ data: e, type: e.type } as MessageEvent);
    });
    // Push session state on connect
    this.sessions.getCurrent().then((s) => {
      local.next({
        data: { type: 'session_state', payload: s },
        type: 'session_state',
      } as MessageEvent);
    });
    // Cleanup on disconnect
    // (NestJS SSE handles this when the observable is unsubscribed; we
    // approximate by completing after 1h and letting the client reconnect.)
    setTimeout(() => {
      sub.unsubscribe();
      local.complete();
    }, 60 * 60 * 1000);
    return local.asObservable();
  }
}
