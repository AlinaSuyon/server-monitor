from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.metrics import get_metrics
from app.database import init_db
from app.scheduler import start_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    start_scheduler()
    yield


app = FastAPI(title="Server Monitor", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return get_metrics()