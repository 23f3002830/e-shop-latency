# E-Shop Latency Metrics API

FastAPI endpoint for analyzing eShopCo storefront latency data.

## Deployment to Vercel

1. **Initialize git repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push to GitHub**:
   - Create a new GitHub repository
   - Push this code to GitHub

3. **Deploy to Vercel**:
   - Visit [https://vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect the Python project
   - Click "Deploy"

## API Endpoint

**POST** `/api/metrics`

### Request Body
```json
{
  "regions": ["amer", "emea"],
  "threshold_ms": 179
}
```

### Response
```json
{
  "regions": {
    "amer": {
      "avg_latency": 156.59,
      "p95_latency": 212.51,
      "avg_uptime": 98.15,
      "breaches": 2
    },
    "emea": {
      "avg_latency": 176.52,
      "p95_latency": 229.21,
      "avg_uptime": 98.54,
      "breaches": 5
    }
  }
}
```

## Available Regions
- `apac`
- `emea`
- `amer`

## Health Check
**GET** `/api/health` - Returns `{"status": "healthy"}`
