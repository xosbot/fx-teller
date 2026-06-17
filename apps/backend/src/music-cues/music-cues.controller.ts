import { Body, Controller, Get, Post, UseGuards } from '@nestjs/common';
import { IsEnum, IsString } from 'class-validator';
import { MusicCuesService } from './music-cues.service';
import { JwtAuthGuard } from '../auth/jwt.guard';
import { AuthedUser, CurrentUser } from '../auth/current-user.decorator';
import { MusicCue, MusicCueSetRequest, Sentiment } from '@fx-teller/shared-types';

class SetCueDto implements MusicCueSetRequest {
  @IsString()
  sessionId!: string;

  @IsEnum(['CALM', 'ALERT'])
  sentiment!: Sentiment;
}

@Controller('music-cues')
export class MusicCuesController {
  constructor(private readonly cues: MusicCuesService) {}

  @Get('current')
  async current(): Promise<MusicCue> {
    return this.cues.getCurrent();
  }

  @Post('set')
  @UseGuards(JwtAuthGuard)
  async set(
    @CurrentUser() u: AuthedUser,
    @Body() dto: SetCueDto,
  ): Promise<MusicCue> {
    return this.cues.set(u.sub, dto);
  }
}
