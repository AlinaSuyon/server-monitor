from fastapi import FastAPI


app = FastAPI(title="Server Monitor")


@app.get("/health")
def health():
    return {"status": "ok"}