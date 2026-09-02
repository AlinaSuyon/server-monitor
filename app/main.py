from fastapi import FastAPI
from app.metrics import get_metrics


app = FastAPI(title="Server Monitor")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return get_metrics()