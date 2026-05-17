const API_URL = "http://127.0.0.1:8000/analyze";

async function analyzeCode() {

    const code = document.getElementById("code").value;
    const language = document.getElementById("language").value;

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "Analyzing...";

    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            code,
            language
        })
    });

    const data = await response.json();

    if (data.errors.length === 0) {
        resultDiv.innerHTML = "No errors found.";
        return;
    }

    let output = "";

    data.errors.forEach(error => {
        output += `
            <p>
                <strong>${error.type}</strong><br>
                ${error.message}
            </p>
            <hr>
        `;
    });

    resultDiv.innerHTML = output;
}
