# Backing up docker data using Kopia

Why Kopia? It supports

-   Encryption out of the box
-   Decent WebUI
-   Incremental backups
-   Deduplication
-   Compression, which can save quite a bit of space
-   Snapshots taken can be mounted and the files can be inspected

Initially I started with a docker setup, but since kopia required root access, it would be simpler to use install it on the host
Download the binary on the host system using yay, else download a pre built binary from [kopia releases](https://github.com/kopia/kopia/releases)

```shell
yay -S kopia-bin
```

## Setup Kopia

Create a password file for kopia to use with its config using `htpasswd`

```bash
> _ htpasswd -c /root/kopiap.txt kopia
New password:
Re-type new password:
Adding password for user kopia
> _ cat /root/kopiap.txt
kopia:$apr1$gpVct.4W$Koq0PYwvRTsxx1I36M6o30
```

Start a kopia server, which will expose port 51515

```bash
_ kopia server start --tls-generate-cert --htpasswd-file /root/kopiap.txt --address https://0.0.0.0:51515 --enable-actions
```

```bash
> _ kopia server start --tls-generate-cert --htpasswd-file /root/kopiap.txt --address https://0.0.0.0:51515 --enable-actions

Server will allow connections from users whose accounts are stored in the repository.
User accounts can be added using 'kopia server user add'.

SERVER CERT SHA256: 5f4294cfa1689fe9603cc8d26f67ff12f6ec64c4875d10bf4b5ee34fe29f9f8e
SERVER ADDRESS: https://[::]:51515
Open the address above in a web browser to use the UI.
```

The `--tls-generate-cert` is used to generate SSl certs

Visiting `https://hostname:51515` gives a password prompt. Use kopia as the username and password setup earlier

## Setup BackBlaze for storage

Currently going with BackBlaze B2 buckets as the storage type since they have a decent free tier

Navigate to Account -> Application Keys and create a new key

Now, navigate to repositories in the Kopia WebUI and select BackBlaze B2 to setup a new one
![]()

Add the necessary details like bucket name, bucket ID, application key and the storage for the repository is set up

## Set snapshot policies

Navigate to `/snapshots` to setup a new snapshot and corresponding policy

![]()

Add the path to directory to backup, then define necessary policies

-   retention policy
-   file ignore list
-   compression algorithm
-   scheduling
-   Pre and post snapshot actions

For some reason the pre and post snapshot script config doesn't work with the WebUI, so set that manually via CLI

```bash
> _ kopia --config-file=/root/.config/kopia/repository.config policy list
[sudo] password for abraxas:
c8f2e632bdace7072c9682ddd38b51d3 (global)
d67a0394619e3a8b14662e656ecadc72 root@niflheim:/opt

> _ kopia --config-file=/root/.config/kopia/repository.config policy set "root@niflheim:/opt" --before-snapshot-root-action /root/.config/kopia/pre-snapshot.sh --after-snapshot-root-action /root/.config/kopia/post-snapshot.sh
Setting policy for root@niflheim:/opt
 - setting before-snapshot-root (essential) action command to "/root/.config/kopia/pre-snapshot.sh" and timeout 5m0s
 - setting after-snapshot-root (essential) action command to "/root/.config/kopia/post-snapshot.sh" and timeout 5m0s
```

Since I am backing up docker bind volumes, I need to stop the containers in order to avoid any corruption.

This script gets a list of all running docker container's ID and pauses all of them.
TO manage them better, using docker labels
`pre-snapshot.sh`

```bash
#! /usr/bin/env bash

backup_label=kopia_backup
containers_to_backup=( $(docker ps --filter "label=$backup_label" -q) )

for container in "${containers_to_backup[@]}"
do
    docker unpause "$container"
done

```

A similar script unpauses the containers once the snapshot is done

## ToDo

-   [ ] Add notifications for snapshot events
-   [ ] Add Images
-   [ ] Add cronjob to start the server automatically at 0400 everyday
