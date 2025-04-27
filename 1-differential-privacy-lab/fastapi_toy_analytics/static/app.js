// Parameters
const epsilon = 1.0;

// Randomized Response
function randomizedResponse(value, epsilon) {
    const p = Math.exp(epsilon) / (Math.exp(epsilon) + 1);
    return Math.random() < p ? value : 1 - value;
}

// Register user when page loads
window.onload = function() {
    fetch("/register_user/", {
        method: "POST"
    });
    setInterval(updateResults, 5000); // Auto-refresh every 5 seconds
}

// Send event with Local DP applied
function sendEvent(eventType) {
    let trueValue = 1; // Simulating the user really clicked
    let noisedValue = randomizedResponse(trueValue, epsilon);

    fetch("/submit_event/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            event_type: eventType,
            noised_value: noisedValue
        })
    }).then(response => {
        console.log("Event sent.");
        updateResults();
    });
}

// Update aggregation results
function updateResults() {
    fetch("/get_estimates/")
    .then(response => response.json())
    .then(data => {
        document.getElementById("results").innerText = JSON.stringify(data, null, 2);
    });
}

