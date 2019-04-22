(function() {

    let resultButton = document.getElementById("resultButton");

    resultButton.addEventListener("click", function() {

        // get values from the input fields and convert them into integers
        let amount = parseInt(document.getElementById("amount").value);
        let rangeLow = parseInt(document.getElementById("rangeLow").value);
        let rangeHigh = parseInt(document.getElementById("rangeHigh").value);

        // check for unwanted values, like 0 or if the requested amount of random numbers is higher than the range span
        if (amount <= 0 || rangeLow <= 0 || rangeHigh <= 0 || (rangeHigh - rangeLow + 1) < amount) { // || means "or"; && means "and"
            resultText.textContent = "ERROR!";
        } else {

            let resultText = document.getElementById("resultText");

            let numArray = [];  // created an array (list) that will hold the randomly generated numbers

            // as long as the array length is less than the requested amount of numbers, keep running the for loop
            for (let i = 0; numArray.length < amount; i++) {
                let randomNum = Math.floor(Math.random() * (rangeHigh - rangeLow + 1)) + rangeLow;

                // if the number does NOT yet exist in the array, add it in the array (push)
                if (!numArray.includes(randomNum)) {  // ! means "not"
                    numArray.push(randomNum);
                }
            }

            numArray.sort(function(a, b){return a-b});  // normal .sort() does not work properly, one of JS quirks

            resultText.textContent = numArray.toString(); // toString() converts array into a string

        }

    });

}())
