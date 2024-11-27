from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import random

app = FastAPI()

# Global list to store metrics
metrics_data: List[Dict] = []

class Metrics(BaseModel):
    endpoint: str
    response_time: int
    status_code: int
    timestamp: str
    cpu_usage: float
    memory_usage: float
    queue_length: int
    success_ratio: float

@app.post("/api/metrics")
async def add_metrics(metrics: Metrics, x_api_key: str = Header(...)):
    # Simulate API key validation
    if x_api_key != "secure-api-key":
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Detect anomalies
    is_anomaly = (
        metrics.response_time > 300 or
        metrics.cpu_usage > 80.0 or
        metrics.memory_usage > 400.0 or
        metrics.success_ratio < 0.8
    )

    # Append metric with anomaly flag
    metrics_data.append({**metrics.dict(), "is_anomaly": is_anomaly})
    return {"status": "Metrics received"}

@app.get("/api/metrics")
async def get_metrics():
    # Group metrics by endpoint
    grouped_metrics = {}
    for metric in metrics_data:
        endpoint = metric["endpoint"]
        if endpoint not in grouped_metrics:
            grouped_metrics[endpoint] = []
        grouped_metrics[endpoint].append(metric)
    return {"metrics": grouped_metrics}

@app.post("/api/mock-metrics")
async def generate_mock_metrics():
    mock_metrics = {
        "endpoint": f"/api/mock-endpoint-{random.randint(1, 3)}",
        "response_time": random.randint(50, 500),
        "status_code": 200,
        "timestamp": "2024-11-03T22:10:00",
        "cpu_usage": round(random.uniform(10.0, 90.0), 2),
        "memory_usage": round(random.uniform(100.0, 500.0), 2),
        "queue_length": random.randint(0, 20),
        "success_ratio": round(random.uniform(0.5, 1.0), 2)
    }

    # Detect anomalies
    is_anomaly = (
        mock_metrics["response_time"] > 300 or
        mock_metrics["cpu_usage"] > 80.0 or
        mock_metrics["memory_usage"] > 400.0 or
        mock_metrics["success_ratio"] < 0.8
    )

    metrics_data.append({**mock_metrics, "is_anomaly": is_anomaly})
    return {"status": "Mock metrics generated", "metrics": mock_metrics}

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the PeakIQ Backend API",
        "endpoints": {
            "/api/metrics": {
                "GET": "Retrieve grouped metrics",
                "POST": "Add new metrics (with anomaly detection)"
            },
            "/api/recommendations": {
                "POST": "Get optimization recommendations for an API endpoint"
            },
            "/api/mock-metrics": {
                "POST": "Generate mock metrics for testing (with anomalies)"
            }
        }
    }