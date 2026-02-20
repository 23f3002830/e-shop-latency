import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

# Enable CORS for POST requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

# Load telemetry data
TELEMETRY_DATA = [
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 161.13,
    "uptime_pct": 98.885,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 136.44,
    "uptime_pct": 97.932,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 112.87,
    "uptime_pct": 99.392,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 200.6,
    "uptime_pct": 98.691,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 229.45,
    "uptime_pct": 98.264,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 109.71,
    "uptime_pct": 99.056,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 153.96,
    "uptime_pct": 97.782,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 228.25,
    "uptime_pct": 97.629,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 157.65,
    "uptime_pct": 97.504,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 216.55,
    "uptime_pct": 98.928,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 147.5,
    "uptime_pct": 98.562,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 151.94,
    "uptime_pct": 98.874,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 165.78,
    "uptime_pct": 99.03,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 129.11,
    "uptime_pct": 99.094,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 179.75,
    "uptime_pct": 98.017,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 120.95,
    "uptime_pct": 97.56,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 155.19,
    "uptime_pct": 99.207,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 158.42,
    "uptime_pct": 99.358,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 199.99,
    "uptime_pct": 98.323,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 188.9,
    "uptime_pct": 97.884,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 192.04,
    "uptime_pct": 97.962,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 203.31,
    "uptime_pct": 98.636,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 229.21,
    "uptime_pct": 99.184,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 177.04,
    "uptime_pct": 98.199,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 168.36,
    "uptime_pct": 97.641,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 131.6,
    "uptime_pct": 98.915,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 200.68,
    "uptime_pct": 98.611,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 117.33,
    "uptime_pct": 98.436,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 142.77,
    "uptime_pct": 98.358,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 153.5,
    "uptime_pct": 97.491,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 175.81,
    "uptime_pct": 98.549,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 142.15,
    "uptime_pct": 98.006,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 130.64,
    "uptime_pct": 98.317,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 190.65,
    "uptime_pct": 97.873,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 161.23,
    "uptime_pct": 97.904,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 212.51,
    "uptime_pct": 97.404,
    "timestamp": 20250312
  }
]


@app.post("/api/metrics")
async def get_metrics(request: dict):
    """
    Calculate per-region metrics for latency and uptime.
    
    Request body: {"regions": [...], "threshold_ms": 180}
    Response: {"regions": {region: {metrics}}}
    """
    regions = request.get("regions", [])
    threshold_ms = request.get("threshold_ms", 180)
    
    result = {"regions": {}}
    
    for region in regions:
        # Filter data for this region
        region_data = [r for r in TELEMETRY_DATA if r["region"] == region]
        
        if not region_data:
            continue
        
        latencies = [r["latency_ms"] for r in region_data]
        uptimes = [r["uptime_pct"] for r in region_data]
        
        # Calculate metrics
        avg_latency = float(np.mean(latencies))
        p95_latency = float(np.percentile(latencies, 95))
        avg_uptime = float(np.mean(uptimes))
        breaches = sum(1 for l in latencies if l > threshold_ms)
        
        result["regions"][region] = {
            "avg_latency": round(avg_latency, 2),
            "p95_latency": round(p95_latency, 2),
            "avg_uptime": round(avg_uptime, 2),
            "breaches": breaches
        }
    
    return JSONResponse(result)


# Health check endpoint
@app.get("/api/health")
async def health():
    return {"status": "healthy"}
