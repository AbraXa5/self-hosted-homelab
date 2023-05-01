# Container and Raspi Monitoring

Containers used in the stack

-   [Prometheus](https://prometheus.io/)
-   [Grafana](https://grafana.com/)
-   [cAdvisor](https://github.com/google/cadvisor)
-   [NodeExporter](https://github.com/prometheus/node_exporter)

cAdvisor extracts conatiners metrics and node-exporter collects host hardware and os metrics
Prometheus monitors these collects as a data source

Grafana visualizes the data from prometheus

Ports for any container except Grafana are not exposed, they can be used internally using the hostname because the conatiners are part of the same stack. This means all of them are on the same network

## Promethes

The data received will be saved at `/opt/prometheus/data`. Another option is to use a database like redis to store it

Add jobs you want to monitor, and good to go.

## Docker Monitoring

Docker conatiners can be monitored using cAdvisor or a [docker daemon that docker exposes on the host](https://docs.docker.com/config/daemon/prometheus/)

## Grafana

-   Add prometheus as the data source using `prometheus:9090` as the URL
-   Used the [RaspberryPiMonitoring](./Dashboard/RaspberryPiMonitoring.json) Dashboard
