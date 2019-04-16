function changeToBlue() {
    let mainHeadingId = document.getElementById("hello");
    mainHeadingId.classList.add("blue-text");
}

let blueButton = document.getElementById("blueButton");
blueButton.addEventListener("click", changeToBlue);
