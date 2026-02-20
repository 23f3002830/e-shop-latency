"""Test script to verify the metrics endpoint"""
import sys
sys.path.insert(0, r"c:\Users\PRINCE PATEL\Desktop\e-shop latency")

from api.index import TELEMETRY_DATA
import numpy as np

# Test with the requested regions
regions = ["amer", "emea"]
threshold_ms = 179

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

print("Test Request: POST /api/metrics")
print(f"Body: {{'regions': {regions}, 'threshold_ms': {threshold_ms}}}")
print("\nResponse:")
import json
print(json.dumps(result, indent=2))
