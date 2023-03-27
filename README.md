# metrics-a-must-have

A Prometheus ecosystem from a Python talk Perspective.
Talk from PyCon It 2022 - [Slides here](https://docs.google.com/presentation/d/1t9FYNmSoBcdmSYjmVqQi8PavuTZL8sgSiM_siiOhodw)


## Usage:

```bash docker-compose up```

This will expose the following services in the Following port:

```
docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED         STATUS         PORTS                              NAMES
08974bf26541   grafana/grafana:latest      "/run.sh"                5 seconds ago   Up 5 seconds   0.0.0.0:3000->3000/tcp             grafana
9d735b4f8ccc   prom/prometheus:latest      "/bin/prometheus --c…"   5 seconds ago   Up 5 seconds   0.0.0.0:9090->9090/tcp             prometheus
f63fcd7fbeea   prom/alertmanager:latest    "/bin/alertmanager -…"   6 seconds ago   Up 5 seconds   0.0.0.0:9093->9093/tcp             alertmanager
90c790b85ad1   prom/node-exporter:latest   "/bin/node_exporter …"   6 seconds ago   Up 5 seconds   0.0.0.0:9001->9001/tcp, 9100/tcp   node-exporter
```

To populate metrics run the Python app:

```bash
uvicorn sample_webapp:app --reload --host 0.0.0.0 --port 6000
```

and fire some requests:

```bash
for i in {1..1000}; do curl "http://localhost:6000/home"; done
```

Note that you can also fire some 500 errors hitting `/fail` endpoint;

