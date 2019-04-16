let blueButton = document.getElementById("blueButton");

blueButton.addEventListener("click", function() { // Anonymous function tied to an event
    let mainHeadingId = document.getElementById("hello");
    mainHeadingId.classList.add("blue-text");
});

// Anonymous function tied to a variable
let sumNumbers = function(x, y) {
    console.log(x + y);
}

sumNumbers(3, 4);
