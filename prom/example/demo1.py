import time
import random
from prometheus_client import start_http_server
from prometheus_client import Counter, Gauge, Histogram, Summary
from prometheus_client import Info, Enum

cc = Counter('cc', 'A counter')
gg = Gauge('gg', 'A gauge')
hh = Histogram('hh', 'A histogram', buckets=(-5, 0, 5), labelnames=['a', 'b'])
ss = Summary('ss', 'A summary', labelnames=['a', 'b'])

i = Info('my_build_version', 'Description of info')
e = Enum('my_task_state', 'Description of enum',states=['starting', 'running', 'stopped'])

i.info({'version': '1.2.3', 'buildhost': 'foo@bar'})

if __name__ == '__main__':
    start_http_server(8000)

    while True:
        cc.inc()
        gg.set(random.random())
        hh.labels('c', 'd').observe(random.randint(-10, 10))
        ss.labels(a='c', b='d').observe(17)

        e.state('running')
        time.sleep(2)
