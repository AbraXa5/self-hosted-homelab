# Self-hosted HomeLab

![Dashboard Image](images/dashboard.png)

-   [Calibre-web](./calibre-web/)
-   [Cloudflare tunnel](./cloudflare-tunnel/)
-   [Container Monitoring](./container-monitoring/)
    -   Prometheus
    -   Grafana
    -   cAdvisor
    -   node-exporter
-   [Filebrowser](./filebrowser/)
-   [Homer](./homer/)
-   [Jellyfin](./jellyfin/)
-   [Nextcloud](./nextcloud/)
-   [Ngnix Proxy Manager](./ngnix-proxy-manager/)
-   [Paperless-ngx](./paperless-ngx/)
-   [PhotoPrism](./PhotoPrism/)
-   [Pihole](./pihole/)
-   [Portainer](./portainer/)
-   [Samba Share](./samba/)
-   [Syncthing](./syncthing/)
-   [Tailscale VPN](./tailscale/)
-   [Uptime Kuma](./uptime-kuma/)
-   [Minimal Vscode](./vscode/)
-   [Wireguard](./wireguard/)

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

### Docker cgroup mnemory issue fix

On arm devices, enabling cgroud memory doesn't take effect.
Adding this to `/boot/cmdline.txt` and rebooting should help fix the issue, [src](https://github.com/docker/for-linux/issues/1112)

```txt
cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1
```

Verify by running.
```bash
docker stats
```

## Contributing

Install pre-commit

```bash
pipx install pre-commit
pre-commit install
```

Update tags for the pre-commit hooks and dry run

```bash
pre-commit autoupdate
pre-commit run --all-files --verbose
```

## ToDo

-   [x] Switch pihole to AdGuard Home
-   [x] Add watchdog to automatically update docker containers
-   [ ] Setup Sonarr, Radarr and Jackett
-   [ ] Switch to Traefik as the reverse proxy
-   [ ] ~~Add wireguard configs~~
-   [x] Setup tailscale for remote access
-   [ ] Setup VaultWarden
