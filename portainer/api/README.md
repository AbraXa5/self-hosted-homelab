# Flask application for Portainer API Container Management

A simple flask application to start/ stop/ restart container using the portainer API (which inturn uses the docker api). This can be done using the portainer UI too, this does that without any authentication

1. Generate a API token
    1. Account -> Access tokens
    2. Populate the `.env` file
2. Add container names and ids to the `containers.json` file in `/opt/portainer_api`
3. Run `docker-compose -d up` to get it up and running
4. `http://hostname:5000/container_name/[start|stop]
