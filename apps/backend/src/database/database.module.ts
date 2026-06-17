import { Global, Module } from '@nestjs/common';
import { Pool } from 'pg';
import { env } from '../env';
import { DbInitService } from './db-init.service';

export const PG_POOL = 'PG_POOL';

@Global()
@Module({
  providers: [
    {
      provide: PG_POOL,
      useFactory: () => {
        const pool = new Pool({ connectionString: env.databaseUrl });
        pool.on('error', (err) => {
          // eslint-disable-next-line no-console
          console.error('Unexpected pg pool error', err);
        });
        return pool;
      },
    },
    DbInitService,
  ],
  exports: [PG_POOL],
})
export class DatabaseModule {}
