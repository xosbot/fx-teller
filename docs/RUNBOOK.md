# Runbook

## Common tasks

### View logs
```bash
docker compose -f infra/docker-compose.yml logs -f api
docker compose -f infra/docker-compose.yml logs -f web
docker compose -f infra/docker-compose.yml logs -f db
```

### Restart a service
```bash
docker compose -f infra/docker-compose.yml restart api
```

### Tail DB queries
```bash
docker compose -f infra/docker-compose.yml exec db psql -U fxteller -d fxteller
# Then:
# \dt              -- list tables
# \d users         -- describe users table
# SELECT * FROM users LIMIT 5;
```

### Make a user a host (via DB)
```bash
docker compose -f infra/docker-compose.yml exec db psql -U fxteller -d fxteller \
  -c "UPDATE users SET role = 'host' WHERE phone = '+91XXXXXXXXXX';"
```

### Manually create an upcoming session
```bash
docker compose -f infra/docker-compose.yml exec db psql -U fxteller -d fxteller <<'SQL'
INSERT INTO sessions (id, title, host_name, host_id, starts_at, status)
VALUES (
  gen_random_uuid(),
  'Live Trading Session',
  'Host',
  '<host-user-uuid>',
  now() + interval '1 hour',
  'UPCOMING'
);
SQL
```

### Force-end a stuck live session
```bash
docker compose -f infra/docker-compose.yml exec db psql -U fxteller -d fxteller \
  -c "UPDATE sessions SET status = 'ENDED', ended_at = now() WHERE id = '<session-uuid>';"
```

### Reset someone's trial
```bash
docker compose -f infra/docker-compose.yml exec db psql -U fxteller -d fxteller \
  -c "UPDATE users SET subscription = 'trialing', trial_ends_at = now() + interval '3 days' WHERE phone = '+91XXXXXXXXXX';"
```

## Troubleshooting

### API won't start / DB connection refused
- Check `docker compose ps` — is `db` healthy?
- Check `docker compose logs db` — any startup errors?
- If password mismatch, recreate: `docker compose down -v && docker compose up -d db`

### SWAG won't get a Let's Encrypt cert
- Make sure port 80 is open in OVH firewall
- Make sure `DOMAIN` in `.env` resolves to this VPS
- Check `docker compose logs swag | grep -i cert`

### 100ms audio not connecting
- Verify `HMS_APP_ACCESS_KEY` and `HMS_APP_SECRET` are correct in `.env`
- Check the mobile app's `/api/hms/token` returns a valid token
- Verify in 100ms dashboard that the template has the `listener` role with `canSubscribe: true`

### Razorpay webhook failing
- Webhook URL: `https://api.fxteller.app/api/webhooks/razorpay`
- Active events to subscribe: `subscription.authenticated`, `subscription.activated`, `subscription.charged`, `subscription.cancelled`, `subscription.completed`, `subscription.halted`
- Webhook secret in `.env` must match the one Razorpay shows after webhook creation
- Check `docker compose logs api | grep webhook` for signature errors

### Floating overlay not appearing on Android
- Xiaomi/Oppo/Vivo: user must enable "Display pop-up windows" + "Autostart" manually
- Lock the app in recents to prevent the system from killing it
- On first use, the app must call `requestOverlayPermission()` — check logs

### Trial not expiring
- `trial_ends_at` is checked on every `GET /api/users/me` call
- If a user keeps getting fresh trials, check their phone number hasn't changed (we key by phone)
