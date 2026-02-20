# Deployment Guide - Vercel Deployment Steps

## ✅ Setup Complete
Your project is now ready for deployment to Vercel. All files have been configured:

- ✓ `api/index.py` - FastAPI application with CORS enabled
- ✓ `api/q-vercel-latency.json` - Sample data file (replace with your actual data)
- ✓ `requirements.txt` - Python dependencies configured
- ✓ `vercel.json` - Vercel build configuration
- ✓ `.gitignore` - Git ignore rules

## 📋 API Endpoints

### Root Endpoint (Health Check)
```
GET /
Response: {"message": "Vercel Latency Analytics API is running."}
```

### Analytics Endpoint
```
POST /api/
```

**Request Body:**
```json
{
  "regions": ["us-east-1", "us-west-2", "eu-west-1"],
  "threshold_ms": 200
}
```

**Response Format:**
```json
{
  "regions": [
    {
      "region": "us-east-1",
      "avg_latency": 47.6,
      "p95_latency": 54.4,
      "avg_uptime": 99.9,
      "breaches": 0
    },
    ...
  ]
}
```

## 🚀 Deployment Steps

### Option 1: Deploy via Vercel CLI (Recommended)

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm install -g vercel
   ```

2. **Initialize Git Repository**:
   ```bash
   cd "c:\Users\PRINCE PATEL\Desktop\e-shop latency"
   git init
   git add .
   git commit -m "Initial commit: Vercel latency analytics API"
   ```

3. **Login to Vercel**:
   ```bash
   vercel login
   ```

4. **Deploy**:
   ```bash
   vercel --prod
   ```
   - Accept the prompts to set up the project
   - Vercel will deploy automatically

5. **Get Your URL**:
   After deployment, you'll see your production URL similar to:
   ```
   https://e-shop-latency-xxx.vercel.app
   ```
   Your API endpoint will be: `https://e-shop-latency-xxx.vercel.app/api/`

### Option 2: Deploy via GitHub + Vercel Web Interface

1. **Initialize Git and Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Vercel latency analytics API"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/e-shop-latency.git
   git push -u origin main
   ```

2. **Deploy via Vercel Console**:
   - Go to https://vercel.com
   - Click "New Project"
   - Select "Import Git Repository"
   - Search for and select your repository
   - Click "Import"
   - Vercel will auto-detect the configuration from `vercel.json`
   - Click "Deploy"

## ⚠️ Important: Replace Sample Data

**The `api/q-vercel-latency.json` file currently contains sample data.**

Replace it with your actual telemetry data before deploying to production:
1. Download `q-vercel-latency.json` from your exam platform
2. Replace the contents of `api/q-vercel-latency.json` with the actual data
3. Commit and deploy again with `vercel --prod`

## 🧪 Testing Your Deployment

After deployment, test your endpoint:

```bash
curl -X POST https://YOUR-DEPLOYED-URL/api/ \
  -H "Content-Type: application/json" \
  -d '{"regions": ["us-east-1"], "threshold_ms": 200}'
```

## 🔍 Troubleshooting

### Common Issues:

1. **"q-vercel-latency.json not found"**
   - Ensure the data file is in the `api/` directory
   - Re-deploy after adding the file

2. **CORS Errors**
   - The API has CORS enabled for all origins
   - If issues persist, check Vercel logs

3. **Module Import Errors**
   - Ensure all packages in `requirements.txt` are correct
   - Vercel will install them automatically during build

4. **Check Vercel Logs**:
   ```bash
   vercel logs --prod
   ```

## 📝 Project Files Summary

```
e-shop latency/
├── api/
│   ├── index.py                 # FastAPI application
│   ├── q-vercel-latency.json   # Telemetry data (replace with actual)
│   └── __pycache__/
├── requirements.txt             # Python dependencies
├── vercel.json                  # Vercel configuration
├── .gitignore                   # Git ignore rules
├── test_endpoint.py            # Local testing script
├── README.md
├── DEPLOYMENT.md
└── deployment_guide.md         # This file
```

## 📞 Support

- Vercel Docs: https://vercel.com/docs/concepts/functions/serverless-functions/python
- FastAPI Docs: https://fastapi.tiangolo.com/
- For Vercel deployment issues: https://vercel.com/docs/deployments
