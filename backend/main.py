from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
import random

app = FastAPI()

# In-memory storage for registered endpoints and metrics
registered_endpoints: Dict[str, Dict] = {}
metrics_data: Dict[str, List[Dict]] = {}

# Models
class RegisterAPI(BaseModel):
    name: str
    url: str
    threshold_response_time: Optional[int] = None  # Optional threshold for alerting
    threshold_error_rate: Optional[float] = None  # Optional error rate threshold

class Metrics(BaseModel):
    endpoint: str
    response_time: int
    status_code: int
    timestamp: str
    cpu_usage: float
    memory_usage: float
    queue_length: int
    success_ratio: float

@app.post("/api/register")
async def register_api(api: RegisterAPI):
    if api.name in registered_endpoints:
        raise HTTPException(status_code=400, detail="API already registered")
    registered_endpoints[api.name] = api.dict()
    metrics_data[api.name] = []  # Initialize metrics list for this endpoint
    return {"status": "API registered successfully", "api": api.dict()}

@app.get("/api/register")
async def get_registered_apis():
    return {"registered_endpoints": registered_endpoints}

@app.post("/api/metrics")
async def add_metrics(metrics: Metrics):
    if metrics.endpoint not in registered_endpoints:
        raise HTTPException(status_code=400, detail="Endpoint not registered")
    # Check for anomalies (e.g., thresholds exceeded)
    anomaly = False
    api_config = registered_endpoints[metrics.endpoint]
    if api_config.get("threshold_response_time") and metrics.response_time > api_config["threshold_response_time"]:
        anomaly = True
    metrics_dict = metrics.dict()
    metrics_dict["is_anomaly"] = anomaly
    metrics_data[metrics.endpoint].append(metrics_dict)
    return {"status": "Metrics received", "is_anomaly": anomaly}

@app.get("/api/metrics")
async def get_metrics():
    return {"metrics": metrics_data}

@app.post("/api/mock-metrics")
async def generate_mock_metrics():
    if not registered_endpoints:
        raise HTTPException(status_code=400, detail="No registered endpoints to generate metrics")
    endpoint = random.choice(list(registered_endpoints.keys()))
    mock_metrics = {
        "endpoint": endpoint,
        "response_time": random.randint(50, 300),
        "status_code": 200,
        "timestamp": "2024-11-03T22:10:00",
        "cpu_usage": round(random.uniform(10.0, 90.0), 2),
        "memory_usage": round(random.uniform(100.0, 500.0), 2),
        "queue_length": random.randint(0, 10),
        "success_ratio": round(random.uniform(0.5, 1.0), 2),
    }
    metrics_data[endpoint].append(mock_metrics)
    return {"status": "Mock metrics generated", "metrics": mock_metrics}

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the PeakIQ Backend API",
        "endpoints": {
            "/api/register": {
                "GET": "Retrieve registered APIs",
                "POST": "Register a new API for monitoring"
            },
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