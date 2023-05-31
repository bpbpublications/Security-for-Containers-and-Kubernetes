## Ubuntu snap conflict
$ sudo apt-mark hold snapd
snapd set on hold.

## Error
CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team
# Fix
sudo apt-get upgrade docker-compose

## cAdvisory 
docker-compose --tlsverify --tlscacert=ca-public-key.pem --tlscert=client-cert.pem --tlskey=client-key.pem -H=192.168.1.226:2376 up

## Ingest metrics into Prometheus
#  Needs SWARM
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2376 --tlsverify --tlscacert=/home/luigi/ca-public-key.pem --tlscert=/home/luigi/server-cert.pem --tlskey=/home/luigi/server-key.pem --metrics-addr=127.0.0.1:9323
# Reload dockerd
sudo systemctl daemon-reload
sudo systemctl restart docker.service
# Run Prometheus from Swarm
sudo docker service create --replicas 1 --name my-prometheus --mount type=bind,source=/tmp/prometheus.yml,destination=/etc/prometheus/prometheus.yaml --publish published=9090,target=9090,protocol=tcp prom/prometheus