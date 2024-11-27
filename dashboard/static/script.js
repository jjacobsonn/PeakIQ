document.addEventListener("DOMContentLoaded", () => {
    const metricsDiv = document.getElementById("metrics");
    const alertsDiv = document.getElementById("alerts");

    // Fetch metrics
    function fetchMetrics() {
        fetch("/api/metrics")
            .then(response => response.json())
            .then(data => {
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
    }

    // Fetch alerts
    function fetchAlerts() {
        fetch("/api/alerts")
            .then(response => response.json())
            .then(data => {
                alertsDiv.innerHTML = ""; // Clear previous alerts
                data.alerts.forEach(alert => {
                    const alertEntry = document.createElement("div");
                    alertEntry.style.color = "red";
                    alertEntry.innerHTML = `
                        <p><strong>Anomaly Detected:</strong> ${alert.issue}</p>
                        <p>Endpoint: ${alert.endpoint}</p>
                        <p>Response Time: ${alert.response_time} ms</p>
                        <p>Timestamp: ${alert.timestamp}</p>
                        <hr>
                    `;
                    alertsDiv.appendChild(alertEntry);
                });
            })
            .catch(error => console.error("Error fetching alerts:", error));
    }

    // WebSocket for real-time updates
    const ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = (event) => {
        const alert = JSON.parse(event.data);
        const alertEntry = document.createElement("div");
        alertEntry.style.color = "red";
        alertEntry.innerHTML = `
            <p><strong>Real-Time Alert:</strong> ${alert.issue}</p>
            <p>Endpoint: ${alert.endpoint}</p>
            <p>Response Time: ${alert.response_time} ms</p>
            <p>Timestamp: ${alert.timestamp}</p>
            <hr>
        `;
        alertsDiv.prepend(alertEntry);
    };

    // Periodic fetches
    setInterval(fetchMetrics, 5000); // Fetch metrics every 5 seconds
    setInterval(fetchAlerts, 5000); // Fetch alerts every 5 seconds
});