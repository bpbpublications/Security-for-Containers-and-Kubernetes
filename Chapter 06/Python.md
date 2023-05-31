## Install PIP on ubuntu
# Check pyhon is installed
$ python3 --version
Python 3.10.6
$ sudo apt install python3-pip      # PIP Installation on Ubuntu
$ pip3 --version
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
$ pip3 install prometheus-client
Collecting prometheus-client
  Downloading prometheus_client-0.16.0-py3-none-any.whl (122 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 122.5/122.5 KB 1.1 MB/s eta 0:00:00
Installing collected packages: prometheus-client
Successfully installed prometheus-client-0.16.0

## Example code
<-------------------------------------------------------------------->
from prometheus_client import start_http_server, Summary
import random
import time
# Metric initialization to track time and requests.
REQUEST_TIME = Summary('request_processing_seconds', ''Requests processing time')
# Populate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """Prometheus Python Client Library example function."""
    time.sleep(t)
if __name__ == '__main__':
    start_http_server(9191)     # HTTP Endpoint
    while True:                 # Requests generation
        process_request(random.random())
<-------------------------------------------------------------------->
