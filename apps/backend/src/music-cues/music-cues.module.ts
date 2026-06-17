import { Module } from '@nestjs/common';
import { MusicCuesService } from './music-cues.service';
import { MusicCuesController } from './music-cues.controller';
import { EventsModule } from '../events/events.module';

@Module({
  imports: [EventsModule],
  controllers: [MusicCuesController],
  providers: [MusicCuesService],
  exports: [MusicCuesService],
})
export class MusicCuesModule {}
