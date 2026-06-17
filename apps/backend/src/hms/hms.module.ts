import { Module } from '@nestjs/common';
import { HmsService } from './hms.service';
import { HmsController } from './hms.controller';

@Module({
  providers: [HmsService],
  controllers: [HmsController],
  exports: [HmsService],
})
export class HmsModule {}
