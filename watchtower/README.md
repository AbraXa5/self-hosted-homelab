# Watchtower

Ideally updating a container would involve

```bash
> docker stop <CONTAINER_ID></CONTAINER_ID>
> docker rm <CONTAINER_ID>
> docker rmi <IMAGE_NAME:TAG>
> docker pull <IMAGE_NAME:TAG>
> docker run <COMMAND>
```

Or using docker compose

```bash
> docker-compose pull
> docker-compose down
> docker-compose up -d --force-recreate
> docker rmi $(docker images -f "dangling=true" -q) -f
```

Watchtower like the name says, _watches_ the containers and periodically checks for a newer version of the deployed image using the Docker API
If a newer image is found, Watchtower sends a `SIGTERM` signal to the containers and stop it, and using the new image runs it again

It also supports a bunch of configurations

-   `WATCHTOWER_CLEANUP` -> Clean old images after updating
-   `WATCHTOWER_INCLUDE_RESTARTING` -> Restart the container
-   `WATCHTOWER_SCHEDULE` -> Run watchtower on a schedule
    -   This needs a 6 set cron job

Run watchtower once against all containers and cleanup

```sh
> docker run --rm \
  --name watchtower_once \
  -v /var/run/docker.sock:/var/run/docker.sock \
  containrrr/watchtower --run-once --cleanup
```

# Creating a discord webhook, https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
