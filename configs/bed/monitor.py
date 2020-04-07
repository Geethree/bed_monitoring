import prometheus_client as prom
import random
import time

COUNTER = prom.Counter('device_read', 'Device was read')

HEART_RATE = prom.Gauge('heart_rate_bpm', 'Heart rate BPM')
O2_LVL = prom.Gauge('o2_mmHg', 'Millimeters of mercury')

def read_values():
    HEART_RATE.set(random.uniform(60,64))
    O2_LVL.set(random.uniform(70,78))


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    prom.start_http_server(8000)
    # Generate some requests.
    while True:
        read_values()
        time.sleep(1)
