import { createParamDecorator, ExecutionContext } from '@nestjs/common';
import { Request } from 'express';

export interface AuthedUser {
  sub: string;
  phone: string;
  role: 'listener' | 'host';
}

export const CurrentUser = createParamDecorator(
  (_data: unknown, ctx: ExecutionContext): AuthedUser => {
    const req = ctx.switchToHttp().getRequest<Request & { user: AuthedUser }>();
    return req.user;
  },
);
