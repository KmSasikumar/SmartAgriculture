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