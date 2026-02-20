# Vercel Deployment Guide

## Quick Deployment Steps

### Step 1: Push to GitHub
```bash
# Create a new repository on GitHub (https://github.com/new)
# Then:

git remote add origin https://github.com/YOUR_USERNAME/e-shop-latency.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Vercel
1. Go to https://vercel.com and sign in (or create account)
2. Click "Add New" → "Project"
3. Click "Import Git Repository"
4. Paste your GitHub repo URL
5. Leave settings as default (Vercel auto-detects Python)
6. Click "Deploy"

### Step 3: Get Your Endpoint URL
After deployment, Vercel will show your project URL like:
```
https://e-shop-latency-XXXXXXXX.vercel.app
```

Your metrics endpoint will be:
```
https://e-shop-latency-XXXXXXXX.vercel.app/api/metrics
```

## Test Your Endpoint

Use curl or any HTTP client:
```bash
curl -X POST https://your-deployed-url.vercel.app/api/metrics \
  -H "Content-Type: application/json" \
  -d '{"regions":["amer","emea"],"threshold_ms":179}'
```

Expected response:
```json
{
  "regions": {
    "amer": {
      "avg_latency": 160.6,
      "p95_latency": 206.0,
      "avg_uptime": 98.13,
      "breaches": 3
    },
    "emea": {
      "avg_latency": 174.97,
      "p95_latency": 214.96,
      "avg_uptime": 98.54,
      "breaches": 6
    }
  }
}
```

## CORS Support
✅ POST requests from any origin are allowed
✅ Preflight OPTIONS requests are handled

## Available Test Data
- Regions: `apac`, `emea`, `amer`
- 36 telemetry records total (12 per region)
- Metrics: latency, uptime for various services
