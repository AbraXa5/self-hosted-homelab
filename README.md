# Self-hosted HomeLab

-   Calibre-web
-   Cloudflare tunnel
-   Container Monitoring
    -   Prometheus
    -   Grafana
    -   cAdvisor
    -   node-exporter
-   Filebrowser
-   Homer
-   Jellyfin
-   Nextcloud
-   Ngnix Proxy Manager
-   Paperless-ngx
-   PhotoPrism
-   Pihole
-   Portainer
-   Samba Share
-   Syncthing
-   Tailscale VPN
-   Uptime Kuma
-   Minimal Vscode
-   Watchtower
-   Wireguard

## Setup

### Install docker and docker-compose

```bash
yay -S docker
yay -S docker-compose
```

```bash
sudo usermod -aG docker $USER
newgrp docker
_ systemctl enable docker --now
```

### Setting up services

`cd`into the directory and run

```bash
docker-compose up -d --force-recreate --remove-orphans
```

Some conatiners need a `.env` file, there's a `.env.example` file to refer to for that. Same goes for `config.yml` if required
