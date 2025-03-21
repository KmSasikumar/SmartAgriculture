// Function to update crop data
function updateCropData() {
    // Simulated data (replace with real data retrieval)
    const temperature = Math.random() * (35 - 20) + 20;
    const soilMoisture = Math.random() * (80 - 20) + 20;
    const cropHealth = Math.random() * 100;
    
    // Display data on the web page
    const dataDisplay = document.getElementById("data-display");
    dataDisplay.innerHTML = `
        <p>Temperature: ${temperature.toFixed(2)}°C</p>
        <p>Soil Moisture: ${soilMoisture.toFixed(2)}%</p>
        <p>Crop Health: ${cropHealth.toFixed(2)}%</p>
    `;
}

// Update crop data every 5 seconds (adjust as needed)
setInterval(updateCropData, 5000);
// Function to fetch and display weather forecast
function fetchWeatherForecast() {
    const apiKey = 'YOUR_API_KEY'; // Replace with your OpenWeatherMap API key
    const apiUrl = `https://api.openweathermap.org/data/2.5/forecast?q=YourCity,YourCountryCode&units=metric&appid=${apiKey}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const weatherDisplay = document.getElementById("weather-display");
            weatherDisplay.innerHTML = ''; // Clear previous data

            // Display weather forecast for the next 5 days
            for (let i = 0; i < data.list.length; i++) {
                const forecast = data.list[i];
                const date = new Date(forecast.dt * 1000); // Convert timestamp to date
                const temperature = forecast.main.temp;
                const description = forecast.weather[0].description;

                // Create a paragraph element to display the forecast
                const forecastElement = document.createElement("p");
                forecastElement.innerHTML = `${date.toLocaleDateString()}: ${temperature}°C, ${description}`;
                weatherDisplay.appendChild(forecastElement);
            }
        })
        .catch(error => {
            console.error("Error fetching weather data:", error);
        });
}

// Update weather forecast every 30 minutes (adjust as needed)
fetchWeatherForecast();
setInterval(fetchWeatherForecast, 30 * 60 * 1000); // 30 minutes



// Financial //
// Loan calculator functionality
const loanCalculator = document.getElementById("loan-calculator");
const monthlyPaymentDisplay = document.getElementById("monthly-payment");

loanCalculator.addEventListener("submit", function (e) {
    e.preventDefault();
    
    const loanAmount = parseFloat(document.getElementById("loan-amount").value);
    const loanTerm = parseInt(document.getElementById("loan-term").value);
    const annualInterestRate = parseFloat(document.getElementById("annual-interest-rate").value) / 100;
    
    if (isNaN(loanAmount) || isNaN(loanTerm) || isNaN(annualInterestRate)) {
        alert("Please enter valid numeric values.");
        return;
    }
    
    const monthlyInterestRate = annualInterestRate / 12;
    const numberOfPayments = loanTerm * 12;
    
    const monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - Math.pow(1 + monthlyInterestRate, -numberOfPayments));
    
    monthlyPaymentDisplay.textContent = `Monthly Payment: Rs${monthlyPayment.toFixed(2)}`;
});






