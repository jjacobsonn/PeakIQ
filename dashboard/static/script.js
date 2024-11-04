document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/metrics")
        .then(response => response.json())
        .then(data => {
            document.getElementById("metrics").innerText = JSON.stringify(data);
        })
        .catch(error => console.error("Error fetching metrics:", error));
});