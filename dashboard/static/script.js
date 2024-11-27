document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/metrics")
        .then(response => response.json())
        .then(data => {
            const metricsDiv = document.getElementById("metrics");
            metricsDiv.innerHTML = ""; // Clear previous content
            if (data.metrics.length === 0) {
                metricsDiv.innerHTML = "<p>No metrics available.</p>";
            } else {
                data.metrics.forEach(metric => {
                    const metricEntry = document.createElement("div");
                    metricEntry.innerHTML = `
                        <p>Endpoint: ${metric.endpoint}</p>
                        <p>Response Time: ${metric.response_time} ms</p>
                        <p>Status Code: ${metric.status_code}</p>
                        <p>Timestamp: ${metric.timestamp}</p>
                        <p>CPU Usage: ${metric.cpu_usage}%</p>
                        <p>Memory Usage: ${metric.memory_usage} MB</p>
                        <p>Queue Length: ${metric.queue_length}</p>
                        <p>Success Ratio: ${metric.success_ratio}</p>
                        <hr>
                    `;
                    metricsDiv.appendChild(metricEntry);
                });
            }
        })
        .catch(error => {
            console.error("Error fetching metrics:", error);
            const metricsDiv = document.getElementById("metrics");
            metricsDiv.innerHTML = "<p>Error fetching metrics. Please try again later.</p>";
        });
});