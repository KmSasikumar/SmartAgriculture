// Crop health page scripts (SAMS rebuild 2026-10-26).
// Crop data below is simulated on purpose (no sensor feed is connected).
// Weather uses Open-Meteo, which needs no API key: the city name is
// geocoded first, then a 5-day forecast is fetched for those coordinates.

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

// Function to fetch and display weather forecast (Open-Meteo, no key needed)
async function fetchWeatherForecast() {
    const cityInput = document.getElementById("weather-city");
    const city = (cityInput && cityInput.value.trim()) || "Bengaluru";
    const weatherDisplay = document.getElementById("weather-display");
    weatherDisplay.innerHTML = `<p>Loading forecast for ${city}…</p>`;

    try {
        const geoResponse = await fetch(
            `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(city)}&count=1`
        );
        const geoData = await geoResponse.json();
        if (!geoData.results || geoData.results.length === 0) {
            weatherDisplay.innerHTML = `<p>City not found: ${city}. Try another city name.</p>`;
            return;
        }
        const place = geoData.results[0];
        const forecastResponse = await fetch(
            `https://api.open-meteo.com/v1/forecast?latitude=${place.latitude}&longitude=${place.longitude}` +
            `&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&forecast_days=5&timezone=auto`
        );
        const data = await forecastResponse.json();

        let html = `<p><strong>${place.name}${place.admin1 ? ", " + place.admin1 : ""}${place.country ? ", " + place.country : ""}</strong></p>`;
        data.daily.time.forEach((day, i) => {
            const rain = data.daily.precipitation_probability_max[i];
            html += `<p>${day}: ${data.daily.temperature_2m_min[i]}°C – ${data.daily.temperature_2m_max[i]}°C` +
                (rain !== null && rain !== undefined ? `, rain chance ${rain}%` : ``) + `</p>`;
        });
        weatherDisplay.innerHTML = html;
    } catch (err) {
        weatherDisplay.innerHTML = `<p>Could not load the forecast. Check your connection and try again.</p>`;
    }
}

// Load the forecast on page load, and again when the city search is used.
fetchWeatherForecast();
const weatherSearch = document.getElementById("weather-search");
if (weatherSearch) {
    weatherSearch.addEventListener("click", fetchWeatherForecast);
}
