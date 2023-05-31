from prometheus_client import start_http_server, Summary
import random
import time
# Metric initialization to track time and requests.
REQUEST_TIME = Summary('request_processing_seconds', 'Requests processing time')
# Populate function with metrics.
@REQUEST_TIME.time()
def process_request(t):
    """Prometheus Python Client Library example function."""
    time.sleep(t)
if __name__ == '__main__':
    start_http_server(9191)     # HTTP Endpoint exposed on port 9191
    while True:                 # Requests generation
        process_request(random.random())