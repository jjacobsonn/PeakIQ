from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Initialize the LLM model
model = pipeline("text-generation", model="gpt2")  # Replace with your chosen model

@app.get("/")
def read_root():
    return {"message": "LLM Engine is running"}

@app.post("/recommendations")
def get_recommendations(data: dict):
    # Generate a response using the LLM model
    response = model(data.get("text", ""), max_length=50)
    return {"recommendation": response[0]["generated_text"]}