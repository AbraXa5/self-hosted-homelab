# Tailscale Mesh VPN

Authenticate and connect to the tailscale network

```bash
docker-compose exec tailscale tailscale up
```

Get status all clients

```bash
docker exec tailscale tailscale status
```

## Access PiHole over tailscale

```bash
docker-compose exec tailscale tailscale up --accept-dns=false
```

Set DNS servers on [tailscale's console](https://login.tailscale.com/admin/dns)
Under Global nameservers, add a custom IP, which would be the Pi's local IP

Enable the `Override local DNS` to override any local DNS settings
Also disable key expiry to prevent DNS interruptions when tailscale re-authenticates

https://tailscale.com/kb/1114/pi-hole/

The same can be done with [NextDNS](https://nextdns.io/)
https://tailscale.com/kb/1218/nextdns/

## Sharing machines

Go to the [tailscale console](https://login.tailscale.com/admin/machines)

Select the machine to share and click on share, which will create a link which can be shared with other users
![](https://i.imgur.com/R6Yzm7N.png)

https://tailscale.com/kb/1084/sharing/#sharing--magicdns
