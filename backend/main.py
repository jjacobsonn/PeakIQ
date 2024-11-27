from fastapi import FastAPI
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
    cpu_usage: float  # New field
    memory_usage: float  # New field

@app.post("/api/metrics")
async def add_metrics(metrics: Metrics):
    global metrics_data
    metrics_data.append(metrics.dict())
    return {"status": "Metrics received"}

@app.get("/api/metrics")
async def get_metrics():
    global metrics_data
    return {"metrics": metrics_data}

@app.post("/api/recommendations")
async def get_recommendation(data: Dict[str, str]):
    endpoint = data.get("endpoint", "unknown")
    return {"recommendation": f"Consider caching the endpoint '{endpoint}' for optimization."}

@app.post("/api/mock-metrics")
async def generate_mock_metrics():
    mock_metrics = {
        "endpoint": "/api/mock-endpoint",
        "response_time": random.randint(50, 300),
        "status_code": 200,
        "timestamp": "2024-11-03T22:10:00",
        "cpu_usage": round(random.uniform(10.0, 90.0), 2),
        "memory_usage": round(random.uniform(100.0, 500.0), 2)
    }
    metrics_data.append(mock_metrics)
    return {"status": "Mock metrics generated", "metrics": mock_metrics}

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the PeakIQ Backend API",
        "endpoints": {
            "/api/metrics": {
                "GET": "Retrieve collected metrics",
                "POST": "Add new metrics"
            },
            "/api/recommendations": {
                "POST": "Get optimization recommendations for an API endpoint"
            },
            "/api/mock-metrics": {
                "POST": "Generate mock metrics for testing"
            }
        }
    }