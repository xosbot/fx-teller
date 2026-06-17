#!/usr/bin/env bash
# Backup Postgres to ./backups. Run on the VPS via cron.
set -euo pipefail
cd "$(dirname "$0")/.."

LABEL="${1:-manual}"
TS=$(date -u +%Y%m%dT%H%M%SZ)
FILE="./backups/fxteller-$TS-$LABEL.sql.gz"
KEEP_DAYS=14

docker compose exec -T db \
  pg_dump -U fxteller -d fxteller --format=custom --no-owner --clean --if-exists \
  | gzip -9 > "$FILE"

[ -s "$FILE" ] || { echo "Backup empty"; rm -f "$FILE"; exit 1; }
gzip -t "$FILE"

find ./backups -name 'fxteller-*.sql.gz' -mtime +$KEEP_DAYS -delete
echo "OK: $FILE ($(du -h "$FILE" | cut -f1))"
