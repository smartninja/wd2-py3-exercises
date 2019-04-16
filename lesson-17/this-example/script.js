// user object example
let someUser = {
    firstName: "Smart",
    lastName: "Ninja",
    powerLevel: 9000,

    fullName: function() {
        console.log(this.firstName + " " + this.lastName);
    }
}

someUser.fullName();


// this blue button example
let blueButton = document.getElementById("blueButton");

blueButton.addEventListener("click", function() {
    let mainHeadingId = document.getElementById("hello");
    mainHeadingId.classList.add("blue-text");

    this.textContent = "DONE!";
});
