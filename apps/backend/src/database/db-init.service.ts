import { Inject, Injectable, Logger, OnModuleInit } from '@nestjs/common';
import { Pool } from 'pg';
import { readFileSync } from 'fs';
import { join } from 'path';
import { PG_POOL } from './database.module';

@Injectable()
export class DbInitService implements OnModuleInit {
  private readonly logger = new Logger(DbInitService.name);

  constructor(@Inject(PG_POOL) private readonly pool: Pool) {}

  async onModuleInit() {
    try {
      const sql = readFileSync(join(__dirname, 'schema.sql'), 'utf8');
      await this.pool.query(sql);
      this.logger.log('Database schema initialized');
    } catch (err) {
      this.logger.error('Failed to initialize schema', err as Error);
    }
  }
}
