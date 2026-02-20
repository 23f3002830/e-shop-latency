from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import statistics
import numpy as np

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Load telemetry data
with open("q-vercel-latency.json") as f:
    data = json.load(f)

@app.post("/api/metrics")
async def metrics(req: Request):
    body = await req.json()
    regions = body["regions"]
    threshold = body["threshold_ms"]

    result = {}

    for r in regions:
        records = [d for d in data if d["region"] == r]

        latencies = [d["latency_ms"] for d in records]
        uptimes = [d["uptime_pct"] for d in records]

        result[r] = {
            "avg_latency": round(statistics.mean(latencies), 2),
            "p95_latency": round(np.percentile(latencies, 95), 2),
            "avg_uptime": round(statistics.mean(uptimes), 2),
            "breaches": sum(1 for l in latencies if l > threshold)
        }

    return result
