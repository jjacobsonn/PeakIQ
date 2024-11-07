from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Global list to retain metrics data
metrics_data: List[Dict] = []

class Metrics(BaseModel):
    endpoint: str
    response_time: int
    status_code: int
    timestamp: str

class RecommendationRequest(BaseModel):
    endpoint: str

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
async def get_recommendation(data: RecommendationRequest):
    # Filter metrics data for the specified endpoint
    endpoint_data = [metric for metric in metrics_data if metric["endpoint"] == data.endpoint]
    
    # Initialize response
    recommendation = "No recommendation at this time."
    
    # Example logic for recommendations based on metrics
    if endpoint_data:
        avg_response_time = sum(d["response_time"] for d in endpoint_data) / len(endpoint_data)
        error_rate = sum(1 for d in endpoint_data if d["status_code"] >= 400) / len(endpoint_data)
        
        # Check if average response time is high
        if avg_response_time > 200:  # Example threshold
            recommendation = "Consider caching this endpoint to reduce response time."
        
        # Check if error rate is high
        if error_rate > 0.1:  # Example threshold for 10% error rate
            recommendation = "High error rate detected. Consider reviewing server configurations or database connections."

    return {"recommendation": recommendation}