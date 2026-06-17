import { Inject, Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { Pool } from 'pg';
import { PG_POOL } from '../database/database.module';
import { UsersService } from '../users/users.service';
import { AuthResponse, User } from '@fx-teller/shared-types';
import { env } from '../env';

interface OtpRow {
  code: string;
  expires_at: Date;
  attempts: number;
}

interface JwtPayload {
  sub: string;
  phone: string;
  role: 'listener' | 'host';
}

@Injectable()
export class AuthService {
  constructor(
    @Inject(PG_POOL) private readonly pool: Pool,
    private readonly users: UsersService,
    private readonly jwt: JwtService,
  ) {}

  async requestOtp(phone: string): Promise<{ devCode?: string }> {
    const normalized = this.normalizePhone(phone);
    const code = this.generateOtp();
    const expires = new Date(Date.now() + 5 * 60 * 1000);
    await this.pool.query(
      `INSERT INTO otp_codes (phone, code, expires_at, attempts)
       VALUES ($1, $2, $3, 0)
       ON CONFLICT (phone) DO UPDATE SET code = EXCLUDED.code, expires_at = EXCLUDED.expires_at, attempts = 0`,
      [normalized, code, expires],
    );
    // In production: send via SMS provider (MSG91, Textlocal, Twilio).
    // For dev, we return the code so the client can display it.
    return env.nodeEnv === 'production' ? {} : { devCode: code };
  }

  async verifyOtp(phone: string, code: string): Promise<AuthResponse> {
    const normalized = this.normalizePhone(phone);
    const row = await this.pool.query<OtpRow>(
      `SELECT code, expires_at, attempts FROM otp_codes WHERE phone = $1`,
      [normalized],
    );
    const otp = row.rows[0];
    if (!otp) throw new UnauthorizedException('No OTP requested');
    if (otp.attempts >= 5) throw new UnauthorizedException('Too many attempts');
    if (new Date(otp.expires_at).getTime() < Date.now())
      throw new UnauthorizedException('OTP expired');
    if (otp.code !== code) {
      await this.pool.query(
        `UPDATE otp_codes SET attempts = attempts + 1 WHERE phone = $1`,
        [normalized],
      );
      throw new UnauthorizedException('Invalid OTP');
    }
    await this.pool.query(`DELETE FROM otp_codes WHERE phone = $1`, [normalized]);

    const user = await this.users.findOrCreateByPhone(normalized);
    const token = this.signToken(user);
    return { token, user };
  }

  signToken(user: User): string {
    const payload: JwtPayload = {
      sub: user.id,
      phone: user.phone,
      role: user.role,
    };
    return this.jwt.sign(payload);
  }

  verifyToken(token: string): JwtPayload {
    return this.jwt.verify<JwtPayload>(token);
  }

  private normalizePhone(phone: string): string {
    const trimmed = phone.replace(/[\s-]/g, '');
    if (trimmed.startsWith('+')) return trimmed;
    if (trimmed.length === 10) return `+91${trimmed}`;
    if (trimmed.length === 12 && trimmed.startsWith('91')) return `+${trimmed}`;
    return trimmed;
  }

  private generateOtp(): string {
    return Math.floor(100000 + Math.random() * 900000).toString();
  }
}
