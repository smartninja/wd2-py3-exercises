let blueButton = document.getElementById("blueButton");

blueButton.addEventListener("click", function() {
    let mainHeadingId = document.getElementById("hello");
    mainHeadingId.classList.add("blue-text");

    this.textContent = "DONE!";
});
