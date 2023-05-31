## Useful commands
#  Be sure to adjust the path to the certificate folder
#  and the -H parameter with the IP address of the linux box running Docker
## LOCALHOST
docker --tlsverify --tlscacert=ca-public-key.pem --tlscert=client-cert.pem --tlskey=client-key.pem -H=127.0.0.1:2376 version
## REMOTE WITHOUT DOCKER_HOST ENV
docker --tlsverify --tlscacert=ca-public-key.pem --tlscert=client-cert.pem --tlskey=client-key.pem -H=192.168.1.226:2376 images
## CURL WITH DOCKER_HOST ENV
curl https://192.168.1.226:2376/images/json --cert ~/.docker/cert.pem --key ~/.docker/key.pem --cacert ~/.docker/ca.pem

## Docker secure by default 
cp ca-public-key.pem ~/.docker/ca.pem
cp client-cert.pem ~/.docker/cert.pem
cp client-key.pem ~/.docker/key.pem
export DOCKER_HOST=tcp://192.168.1.226:2376 DOCKER_TLS_VERIFY=1