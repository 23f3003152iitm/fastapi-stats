from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
import time
import uuid


app = FastAPI()

ALLOWED_ORIGIN = "https://dash-zw43c8.example.com"


app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOWED_ORIGIN],
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_headers(request: Request, call_next):

    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    response.headers["X-Request-ID"] = str(uuid.uuid4())
    response.headers["X-Process-Time"] = str(duration)

    return response



@app.get("/stats")
def stats(values: str = Query(...)):

    numbers = [int(x) for x in values.split(",")]

    return {
        "email": "23f3003151@ds.study.iitm.ac.in",
        "count": len(numbers),
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "mean": round(sum(numbers) / len(numbers), 2)
    }