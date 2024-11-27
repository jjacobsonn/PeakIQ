document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/metrics")
        .then(response => response.json())
        .then(data => {
            const metricsDiv = document.getElementById("metrics");
            metricsDiv.innerHTML = ""; // Clear previous content

            Object.entries(data.metrics).forEach(([endpoint, metrics]) => {
                const endpointDiv = document.createElement("div");
                endpointDiv.innerHTML = `<h2>Metrics for ${endpoint}</h2>`;
                metricsDiv.appendChild(endpointDiv);

                metrics.forEach(metric => {
                    const metricEntry = document.createElement("div");
                    metricEntry.style.color = metric.is_anomaly ? "red" : "black"; // Highlight anomalies
                    metricEntry.innerHTML = `
                        <p>Response Time: ${metric.response_time} ms</p>
                        <p>Status Code: ${metric.status_code}</p>
                        <p>Timestamp: ${metric.timestamp}</p>
                        <p>CPU Usage: ${metric.cpu_usage}%</p>
                        <p>Memory Usage: ${metric.memory_usage} MB</p>
                        <p>Queue Length: ${metric.queue_length}</p>
                        <p>Success Ratio: ${metric.success_ratio}</p>
                        <p>Anomaly: ${metric.is_anomaly ? "Yes" : "No"}</p>
                        <hr>
                    `;
                    metricsDiv.appendChild(metricEntry);
                });
            });
        })
        .catch(error => console.error("Error fetching metrics:", error));
});