# PeakIQ
    
    PeakIQ is an AI-powered optimization tool designed to keep APIs running at peak performance. Built with an LLM-powered recommendation engine and deployed on the Akash Network, PeakIQ analyzes real-time metrics to detect bottlenecks and provide actionable insights for API improvements. These insights include recommendations for caching, load balancing, and database tuning.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Docker Setup](#docker-setup)
- [Usage Guide](#usage-guide)
- [Troubleshooting](#troubleshooting)

---

## Project Overview

PeakIQ aims to help developers and DevOps teams optimize their API performance through intelligent, data-driven recommendations. The tool collects real-time performance metrics, analyzes them, and suggests improvements to reduce latency and optimize resource utilization.

---

## Features

- **Real-Time Metrics Tracking**: Collects response times, request volumes, and error rates.
- **AI-Driven Recommendations**: Suggests optimizations based on metrics, including caching, load balancing, and indexing.
- **Interactive Dashboard**: Visualizes API metrics and recommendations for quick insights.
- **Containerized with Docker**: Easily deployable on the Akash Network.

---

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed and running.
- **Git**: Use Git to clone the repository.

### Clone the Repository

```
git clone https://github.com/your-username/PeakIQ.git
cd PeakIQ
```

---

## Docker Setup

### Build and Run the Application

The application consists of several services, including the backend, LLM engine, Redis database, and a frontend dashboard. 

1. **Start Docker Containers**: Run the following command to build and start the containers:

    ```
    docker-compose up --build
    ```

2. **Check Status**: Verify that all containers (`backend`, `llm_engine`, `redis`, and `dashboard`) are running without errors. You should see logs indicating the backend is accessible at `http://localhost:8000`.

3. **Stop Containers**: To stop the containers, use:

    ```
    docker-compose down
    ```

---

## API Endpoints

### 1. Metrics Endpoint

Use this endpoint to submit API metrics that PeakIQ will analyze.

- **Endpoint**: `/metrics`
- **Method**: `POST`
- **Example Request**:
    ```
    curl -X POST http://localhost:8000/metrics -H "Content-Type: application/json" -d '{"endpoint": "/api test","response_time": 120, "status_code": 200,"timestamp": "2024-11-03T22:10:00"}'
    ```
- **Expected Response**:
    ```
    {"status": "Metrics received"}
    ```

## 2. Recommendations Endpoint
This endpoint provides optimization suggestions based on submitted metrics.

- **Endpoint**: `/recommendations`
- **Method**: `POST`
- **Example Request**:
    ```
    curl -X POST "http://localhost:8000/recommendations" -H "Content-Type: application/json" -d '{"endpoint": "/api/test"}'
    ```
- **Expected Response**:
    ```
    {"recommendation": "Consider caching this endpoint for optimization."}
    ```

## 3. LM Endpoint
To directly interact with the LLM engine for testing purposes:

- **Endpoint**: `/recommendations`
- **Port**: `8001`
- **Example Request**:
    ```
    curl -X POST "http://localhost:8001/recommendations" -H "Content-Type: application/json" -d '{"text": "Optimize API performance"}'
    ```
- **Response**:
    ```
    {"recommendation": "Optimize API performance by..."}
    ```

---

# Usage Guide

1. **Access the Dashboard**: Open your browser and navigate to `http://localhost:YOUR_DASHBOARD_PORT` to view real-time metrics and recommendations.

2. **Submit Metrics**: Use the `/metrics` endpoint to continuously submit data for any API you’re monitoring.

3. **View Recommendations**: After submitting metrics, use the `/recommendations` endpoint to receive improvement suggestions. These insights are shown on the dashboard as well.

---

# Acknowledgments

This project was developed by Jackson Jacobson (github: @jjacobsonn). Special thanks to contributors and collaborators who supported its development.

If you use this project, please provide appropriate credit by linking back to this repository and following the guidelines outlined in the license.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

