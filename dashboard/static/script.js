document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/metrics")
        .then(response => response.json())
        .then(data => {
            const metricsDiv = document.getElementById("metrics");
            metricsDiv.innerHTML = ""; // Clear previous content
            data.metrics.forEach(metric => {
                const metricEntry = document.createElement("div");
                metricEntry.innerHTML = `
                    <p>Endpoint: ${metric.endpoint}</p>
                    <p>Response Time: ${metric.response_time} ms</p>
                    <p>Status Code: ${metric.status_code}</p>
                    <p>Timestamp: ${metric.timestamp}</p>
                    <p>CPU Usage: ${metric.cpu_usage}%</p>
                    <p>Memory Usage: ${metric.memory_usage} MB</p>
                    <hr>
                `;
                metricsDiv.appendChild(metricEntry);
            });
        })
        .catch(error => console.error("Error fetching metrics:", error));
});