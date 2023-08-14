# AdGuard Home

## Config

Upstream DNS servers

```
https://dns10.quad9.net/dns-query
1.1.1.1
https://dns.adguard-dns.com/dns-query
https://dns.nextdns.io
https://security.cloudflare-dns.com/dns-query
```

Bootstrap DNS servers

```
9.9.9.10
149.112.112.10
2620:fe::10
2620:fe::fe:10
```

Private reverse DNS servers

```
192.168.1.6
```

DNS Blocklists

-   https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt -> AdGuard DNS filter
-   https://adguardteam.github.io/HostlistsRegistry/assets/filter_34.txt -> HaGeZi Personal Black & White
-   https://adguardteam.github.io/HostlistsRegistry/assets/filter_33.txt -> Steven Black's List
-   https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt -> Dan Pollock's List
-   https://adguardteam.github.io/HostlistsRegistry/assets/filter_27.txt -> OISD Blocklist Big

DNS rewrites (mostly for NGINX PROXY MANAGER and a couple other services)

-   adguard.home 192.168.1.6
-   niflheim.local 12.168.1.6
-   \*.lan.niflheim.online 192.168.1.6
-   \*.local.niflheim.online 192.168.1.6
-   dashboard.niflheim-local.duckdns.org 192.168.1.6

## Container issues

Healthcheck issue for ARM v0.107.34

> Docker users should note that the Docker HEALTHCHECK mechanism has been removed, since it was causing a lot of issues, especially when used with Podman and other popular Docker tools.

**Solution**
Delete and re pull the image
`docker compose up -d --force-recreate --remove-orphans --pull true`
