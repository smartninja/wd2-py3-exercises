let resultInfo = document.getElementById("resultInfo");
let convertButton = document.getElementById("convertButton");
let ratio = 0.62137119;

function convertToMiles() {
    let km = parseFloat(document.getElementById("km").value);

    let miles = km * ratio;

    resultInfo.textContent = km + " km is equal to " + miles + " miles.";
}

convertButton.addEventListener("click", convertToMiles);
