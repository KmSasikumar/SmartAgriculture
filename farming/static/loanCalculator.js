const loanCalculator = document.getElementById("loan-calculator");
const monthlyPaymentDisplay = document.getElementById("monthly-payment");

loanCalculator.addEventListener("submit", function (e) {
    e.preventDefault();

    const loanAmount = parseFloat(document.getElementById("loan-amount").value);
    const loanTerm = parseInt(document.getElementById("loan-term").value);
    const annualInterestRate = parseFloat(document.getElementById("annual-interest-rate").value) / 100;

    if (isNaN(loanAmount) || isNaN(loanTerm) || isNaN(annualInterestRate) || loanAmount <= 0 || loanTerm <= 0) {
        alert("Please enter valid numeric values.");
        return;
    }

    const monthlyInterestRate = annualInterestRate / 12;
    const numberOfPayments = loanTerm * 12;

    // A 0% loan has no interest: the payment is simply principal / months.
    // The general formula divides by (1 - (1 + r)^-n), which is 0 when r = 0
    // and used to produce NaN here.
    const monthlyPayment = monthlyInterestRate === 0
        ? loanAmount / numberOfPayments
        : (loanAmount * monthlyInterestRate) / (1 - Math.pow(1 + monthlyInterestRate, -numberOfPayments));

    monthlyPaymentDisplay.textContent = `Monthly Payment: Rs${monthlyPayment.toFixed(2)}`;
});