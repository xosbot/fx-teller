import { Controller, Get, UseGuards } from '@nestjs/common';
import { HmsService } from './hms.service';
import { JwtAuthGuard } from '../auth/jwt.guard';
import { AuthedUser, CurrentUser } from '../auth/current-user.decorator';
import { HmsTokenResponse } from '@fx-teller/shared-types';

@Controller('hms')
@UseGuards(JwtAuthGuard)
export class HmsController {
  constructor(private readonly hms: HmsService) {}

  @Get('token')
  token(@CurrentUser() u: AuthedUser): HmsTokenResponse {
    return this.hms.mintToken({ userId: u.sub, role: u.role });
  }
}
