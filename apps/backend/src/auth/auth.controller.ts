import { Body, Controller, Post } from '@nestjs/common';
import { IsString, Matches, MinLength } from 'class-validator';
import { AuthService } from './auth.service';
import { AuthOtpRequest, AuthOtpVerify, AuthResponse } from '@fx-teller/shared-types';

class OtpRequestDto implements AuthOtpRequest {
  @IsString()
  @Matches(/^(\+?\d{10,12})$/, { message: 'Invalid phone number' })
  phone!: string;
}

class OtpVerifyDto implements AuthOtpVerify {
  @IsString()
  @Matches(/^(\+?\d{10,12})$/, { message: 'Invalid phone number' })
  phone!: string;

  @IsString()
  @MinLength(6)
  code!: string;
}

@Controller('auth')
export class AuthController {
  constructor(private readonly auth: AuthService) {}

  @Post('otp/request')
  async requestOtp(@Body() dto: OtpRequestDto) {
    return this.auth.requestOtp(dto.phone);
  }

  @Post('otp/verify')
  async verifyOtp(@Body() dto: OtpVerifyDto): Promise<AuthResponse> {
    return this.auth.verifyOtp(dto.phone, dto.code);
  }
}
