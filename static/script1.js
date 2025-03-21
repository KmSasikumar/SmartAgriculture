// Crop production calculator functionality
const cropProductionCalculator = document.getElementById("crop-production-calculator");
const productionResult = document.getElementById("production-result");

cropProductionCalculator.addEventListener("submit", function (e) {
    e.preventDefault();

    const cropName = document.getElementById("crop-name").value;
    const landArea = parseFloat(document.getElementById("land-area").value);
    const cropYield = parseFloat(document.getElementById("crop-yield").value);
    const inputCost = parseFloat(document.getElementById("input-cost").value);
    const marketPrice = parseFloat(document.getElementById("market-price").value);

    if (isNaN(landArea) || isNaN(cropYield) || isNaN(inputCost) || isNaN(marketPrice)) {
        alert("Please enter valid numeric values.");
        return;
    }

    const totalProduction = landArea * cropYield;
    const totalRevenue = totalProduction * marketPrice;
    const totalCost = landArea * inputCost;
    const profit = totalRevenue - totalCost;

    productionResult.innerHTML = `
        Crop: ${cropName}<br>
        Total Production: ${totalProduction.toFixed(2)} kg<br>
        Total Revenue: ${totalRevenue.toFixed(2)}<br>
        Total Cost: ${totalCost.toFixed(2)}<br>
        Profit: ${profit.toFixed(2)}
    `;
});
