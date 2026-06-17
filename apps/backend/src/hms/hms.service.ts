// 100ms.live JWT minting.
// 100ms uses HS256 JWTs signed with app_secret, and a static app_access_key claim.
// See: https://www.100ms.live/docs/server-side/v2/Authentication/token

import { Injectable } from '@nestjs/common';
import * as jwt from 'jsonwebtoken';
import { env } from '../env';
import { HmsTokenResponse } from '@fx-teller/shared-types';

@Injectable()
export class HmsService {
  // Stable room id for v1 — single room per app.
  // In a multi-host future, derive from session id.
  private readonly roomId = 'fxteller-main';

  mintToken(opts: {
    userId: string;
    role: 'listener' | 'host';
  }): HmsTokenResponse {
    const role = opts.role === 'host' ? env.hmsRoleHost : env.hmsRoleListener;
    const token = jwt.sign(
      {
        access_key: env.hmsAppAccessKey,
        room_id: this.roomId,
        user_id: opts.userId,
        role,
        type: 'app',
        version: 2,
      },
      env.hmsAppSecret,
      {
        algorithm: 'HS256',
        expiresIn: '24h',
        jwtid: `${opts.userId}-${Date.now()}`,
      },
    );
    return { token, roomId: this.roomId };
  }
}
