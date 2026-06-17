import { Body, Controller, Get, Patch, UseGuards } from '@nestjs/common';
import { IsOptional, IsString, MaxLength } from 'class-validator';
import { UsersService } from './users.service';
import { JwtAuthGuard } from '../auth/jwt.guard';
import { AuthedUser, CurrentUser } from '../auth/current-user.decorator';
import { User } from '@fx-teller/shared-types';

class UpdateProfileDto {
  @IsOptional()
  @IsString()
  @MaxLength(60)
  name?: string;
}

@Controller('users')
@UseGuards(JwtAuthGuard)
export class UsersController {
  constructor(private readonly users: UsersService) {}

  @Get('me')
  async me(@CurrentUser() u: AuthedUser): Promise<User> {
    const user = await this.users.findById(u.sub);
    if (!user) throw new Error('User not found');
    return user;
  }

  @Patch('me')
  async update(
    @CurrentUser() u: AuthedUser,
    @Body() dto: UpdateProfileDto,
  ): Promise<User> {
    if (dto.name !== undefined) {
      return this.users.updateName(u.sub, dto.name);
    }
    const me = await this.users.findById(u.sub);
    if (!me) throw new Error('User not found');
    return me;
  }
}
