from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend API is running"}

@app.post("/metrics")
def collect_metrics(data: dict):
    # Process the incoming data (dummy response for testing)
    return {"status": "Metrics received"}

@app.post("/recommendations")
def get_recommendations(data: dict):
    # Return a mock recommendation (replace with LLM integration)
    return {"recommendation": "Consider caching this endpoint for optimization."}