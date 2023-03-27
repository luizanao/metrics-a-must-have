import asyncio
import random
import time

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, Histogram, generate_latest

app = FastAPI()


histogram = Histogram(
    "http_request_duration_seconds",
    "Request duration",
    labelnames=["method", "path", "http_status"],
)


async def middleware_handler(request, handler):
    tic = time.time()
    response = await handler(request)
    # Warning: request.url.path needs to be low cardinality
    # you might want to remove any uuid/id/slug from the path
    # and replace with something literal. e.g: /abc/<uuid>
    labels = [request.method, request.url.path, response.status_code]
    tac = time.time()
    histogram.labels(*labels).observe(tac - tic)
    return response


app.middleware("http")(middleware_handler)


@app.get("/home")
async def home():
    ms = random.uniform(0.1, 2)
    print(f"sleeping {ms}")
    await asyncio.sleep(ms)
    return {"message": "Hello World"}


@app.get("/fail")
async def home():
    raise Exception()


@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
