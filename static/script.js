// Crop yield calculator functionality
const cropYieldCalculator = document.getElementById("crop-yield-calculator");
const yieldResult = document.getElementById("yield-result");

cropYieldCalculator.addEventListener("submit", function (e) {
    e.preventDefault();
    
    const cropWeight = parseFloat(document.getElementById("crop-weight").value);
    const landArea = parseFloat(document.getElementById("land-area").value);
    
    if (isNaN(cropWeight) || isNaN(landArea)) {
        alert("Please enter valid numeric values.");
        return;
    }
    
    const yieldPerAcre = cropWeight / landArea;
    
    yieldResult.textContent = `Crop Yield: ${yieldPerAcre.toFixed(2)} kg/acre`;
});
