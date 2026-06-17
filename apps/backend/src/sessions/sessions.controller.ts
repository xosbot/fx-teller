import {
  Body,
  Controller,
  Get,
  Param,
  Post,
  UseGuards,
} from '@nestjs/common';
import { IsString, MaxLength, MinLength } from 'class-validator';
import { SessionsService } from './sessions.service';
import { JwtAuthGuard } from '../auth/jwt.guard';
import { AuthedUser, CurrentUser } from '../auth/current-user.decorator';
import { Session, SessionStartRequest } from '@fx-teller/shared-types';

class StartSessionDto implements SessionStartRequest {
  @IsString()
  @MinLength(3)
  @MaxLength(120)
  title!: string;
}

@Controller('sessions')
export class SessionsController {
  constructor(private readonly sessions: SessionsService) {}

  @Get()
  async list(): Promise<Session[]> {
    return this.sessions.listUpcoming();
  }

  @Get('current')
  async current(): Promise<Session | null> {
    return this.sessions.getCurrent();
  }

  @Get(':id')
  async one(@Param('id') id: string): Promise<Session> {
    return this.sessions.getById(id);
  }

  @Post('start')
  @UseGuards(JwtAuthGuard)
  async start(
    @CurrentUser() u: AuthedUser,
    @Body() dto: StartSessionDto,
  ): Promise<Session> {
    return this.sessions.create({
      title: dto.title,
      hostName: 'Host',
      hostId: u.sub,
      startsAt: new Date(),
    }).then((s) => this.sessions.start(s.id));
  }

  @Post(':id/end')
  @UseGuards(JwtAuthGuard)
  async end(@Param('id') id: string): Promise<Session> {
    return this.sessions.end(id);
  }
}
