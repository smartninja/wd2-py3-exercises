(function() {

    let resultButton = document.getElementById("resultButton");

    resultButton.addEventListener("click", function() {
        let firstNum = parseFloat(document.getElementById("firstNum").value);
        let selectOperation = document.getElementById("selectOperation");
        let secondNum = parseFloat(document.getElementById("secondNum").value);
        let resultText = document.getElementById("resultText");

        if (selectOperation.value == "+") {
            resultText.textContent = firstNum + secondNum;
        } else if (selectOperation.value == "-") {
            resultText.textContent = firstNum - secondNum;
        } else if (selectOperation.value == "*") {
            resultText.textContent = firstNum * secondNum;
        } else if (selectOperation.value == "/") {
            resultText.textContent = firstNum / secondNum;
        }

        console.log(firstNum.value);
        console.log(selectOperation.value);
        console.log(secondNum.value);
    });

}())
