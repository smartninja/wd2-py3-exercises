console.log("it works!");

// find elements by tag name
let mainHeadingText = document.getElementsByTagName("h1")[0].textContent;

console.log(mainHeadingText);

// find element by id
let mainHeadingIdText = document.getElementById("hello").textContent;

console.log(mainHeadingIdText);

// find elements by tag name
let mainHeadingClassText = document.getElementsByClassName("ninja")[0].textContent;

console.log(mainHeadingClassText);

// change the mainHeading text
let mainHeadingId = document.getElementById("hello");
mainHeadingId.textContent = "Hello, new heading!";

// change the text color
// mainHeadingId.style.color = "red";

// assign the green-text class
mainHeadingId.classList.add("green-text");

// remove green-text and assign blue-text
mainHeadingId.classList.remove("green-text");
mainHeadingId.classList.add("blue-text");
