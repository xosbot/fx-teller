#!/usr/bin/env bash
# Deploy latest images. Trigger from CI: ssh deploy@vps '/srv/fxteller/deploy.sh'
set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> Pulling latest images"
docker compose pull

echo "==> Backing up DB before deploy"
./scripts/backup.sh pre-deploy || true

echo "==> Recreating containers"
docker compose up -d --remove-orphans

echo "==> Waiting for API healthcheck"
for i in {1..30}; do
  if docker compose ps api --format json 2>/dev/null | grep -q '"Health":"healthy"'; then
    echo "OK"; break
  fi
  if [ $i -eq 30 ]; then echo "API failed healthcheck"; docker compose logs --tail=100 api; exit 1; fi
  sleep 2
done

docker image prune -f
echo "==> Deploy complete"
