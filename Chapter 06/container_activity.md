## As per reference to Chapter 3 - Network Security
## This lab requires Docker SWARM
Edit /etc/systemd/system/docker.service.d/override.conf, adding --metrics-addr to the unix socket
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H unix:///var/run/docker.sock --metrics-addr=127.0.0.1:9323
## Restart the docker daemon
sudo systemctl daemon-reload
sudo systemctl restart docker.service
## On the manager node
touch prometheus.yml
## add the following code (Linux system)
<---------------------------------->
# Prometheus config
global:
  scrape_interval:     15s
  evaluation_interval: 15s
  external_labels:
      monitor: 'prometheus-monitor-docker'
rule_files:
  # - "first.rules"         # No rules for this example
  # - "second.rules"        # No rules for this example
scrape_configs:
  - job_name: 'prometheus'  # Establish reachability for Prometheus system
    static_configs:
      - targets: ['192.168.1.226:9090']
  - job_name: 'docker'      # Connects the target to the dockerd daemon
    static_configs:
      - targets: ['192.168.1.226:9323']
<---------------------------------->
## Run Prometheus as a service on the manager node
sudo docker service create --replicas 1 --name my-prometheus --mount type=bind,source=/tmp/prometheus.yml,destination=/etc/prometheus/prometheus.yml --publish published=9090,target=9090,protocol=tcp prom/prometheus
## Pretty format
sudo docker service create \
--replicas 1 \
--name my-prometheus \
--mount type=bind,source=/home/luigi/prometheus.yml,destination=/etc/prometheus/prometheus.yml \
--publish published=9090,target=9090,protocol=tcp \
prom/prometheus

## Verify that Docker target is UP 
http://192.168.1.226:9090/targets
## In the Prometheus UI click the Graph link. Choose a metric from the search box and click Execute. 
http://192.168.1.226:9323/metrics

## Ping Service used to generate dummy traffic
docker service create \
  --replicas 5 \
  --name ping_service \
  alpine ping docker.com