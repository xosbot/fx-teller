# Deployment guide (OVH VPS)

## 1. Provision the VPS

- Region: **Singapore** (`sgp`) — best latency to Kerala
- Plan: VPS-2 (4 vCPU / 8 GB RAM / 80 GB SSD) — ~€12/mo
- OS: Ubuntu 24.04 LTS
- Enable anti-DDoS (on by default)
- Set reverse DNS (PTR) for mail-friendly IP

## 2. Initial server setup

```bash
# SSH as root, then:
apt update && apt -y upgrade
apt -y install docker.io docker-compose-plugin ufw fail2ban curl git

# Create non-root user
useradd -m -s /bin/bash deploy
usermod -aG docker deploy
mkdir -p /home/deploy/.ssh
cp ~/.ssh/authorized_keys /home/deploy/.ssh/
chown -R deploy:deploy /home/deploy/.ssh
chmod 700 /home/deploy/.ssh
chmod 600 /home/deploy/.ssh/authorized_keys

# SSH hardening
sed -i 's/#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sed -i 's/#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart ssh

# Firewall
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable

# fail2ban
systemctl enable fail2ban
systemctl start fail2ban

# unattended upgrades
apt -y install unattended-upgrades
dpkg-reconfigure -plow unattended-upgrades
```

## 3. Clone and configure

```bash
sudo -iu deploy
git clone <repo-url> /srv/fxteller
cd /srv/fxteller

# Env
cp .env.example .env
nano .env   # fill in real values

# Secrets dir (for DB password file - optional, .env is enough for v1)
mkdir -p secrets
```

Generate strong random secrets:
```bash
openssl rand -hex 32  # JWT_SECRET
openssl rand -hex 16  # POSTGRES_PASSWORD
```

## 4. Point your domain

In your DNS provider:
- `A api.fxteller.app → <vps-ip>`
- `A app.fxteller.app → <vps-ip>`
- `A fxteller.app → <vps-ip>`

## 5. First deploy

```bash
# Build images locally on the VPS (faster than CI for v1)
./infra/scripts/deploy.sh

# Watch logs
docker compose -f infra/docker-compose.yml logs -f
```

The first boot will:
- Pull postgres, swag, node images
- Build api + web images
- Start all services
- SWAG will request a Let's Encrypt cert on first request — open `https://fxteller.app` to trigger

## 6. SWAG post-setup

After the first request, you'll get certs. Now:

```bash
# Edit SWAG config to enable nginx proxy for our domains
docker compose -f infra/docker-compose.yml exec swag bash

# Inside the container, add a site config:
cat > /config/nginx/site-confs/api.conf <<'EOF'
server {
    listen 443 ssl http2;
    server_name api.fxteller.app;
    include /config/nginx/ssl.conf;
    client_max_body_size 10M;
    location / {
        include /config/nginx/proxy.conf;
        resolver 127.0.0.11 valid=30s;
        set $upstream_api api;
        proxy_pass http://$upstream_api:3000;
    }
}
EOF

cat > /config/nginx/site-confs/app.conf <<'EOF'
server {
    listen 443 ssl http2;
    server_name app.fxteller.app;
    include /config/nginx/ssl.conf;
    location / {
        include /config/nginx/proxy.conf;
        proxy_pass http://web:3000;
    }
}
EOF

# Restart SWAG to apply
exit
docker compose -f infra/docker-compose.yml restart swag
```

## 7. Mobile build (EAS)

For v1, mobile builds happen in the cloud via Expo's EAS service:

```bash
cd apps/mobile
npm install -g eas-cli
eas login
eas build --platform android --profile production
eas build --platform ios --profile production
```

You'll need:
- `eas.json` (already created)
- Expo account (free tier OK for v1)
- Apple Developer account ($99/yr) for iOS builds
- Google Play Developer account ($25 one-time) for Android submissions

## 8. Backups

```bash
# Manual
./infra/scripts/backup.sh

# Cron (nightly at 3am)
crontab -e
# Add:
0 3 * * * /srv/fxteller/infra/scripts/backup.sh nightly >> /var/log/fxteller-backup.log 2>&1
```

Restores:
```bash
gunzip -c backups/fxteller-XXX.sql.gz | docker compose exec -T db pg_restore -U fxteller -d fxteller --clean --if-exists
```

OVH-level: configure weekly VPS snapshot via the OVH control panel as a second safety net.

## 9. Monitoring

v1 has no external monitoring. Watch:
- `docker compose ps` — should all be "healthy"
- `docker compose logs --tail=100 api` — for errors
- SWAG dashboard at `https://fxteller.app:9443` — fail2ban, cert status
- 100ms dashboard — for live session health, listener counts

Add Sentry + Uptime monitoring in v2.
