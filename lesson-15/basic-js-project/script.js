"use strict";  // using this is a good practice

// variables
let num = 22;
num = 31;
let someName = "Matt";
let bool = false;
let nothing = null;

console.log(num);
console.log(someName);
console.log(bool);
console.log(nothing);

// single line comment

/*
    multi
    line
    comment
*/

// data structures
let someArray = [1, 5, 67, "hey", 245, true];  // array (like list in Python)
console.log(someArray);

let someObject = {"name": "Matt", "age": 22, "admin": false};
console.log(someObject.name);

// if/else
let mood = "happy";

if (mood === "happy") {
    console.log("It's great to see you happy!");
} else {
    console.log("Cheer up!");
}

// while loop
let counter = 0;

while (counter < 5) {
    console.log("Counter is less than 5");
    console.log("Counter value: " + counter);
    counter++;
}

// for loops
let animals = ["dog", "cat", "bunny"];

console.log("For loop similar to Python's:");
for (let animal of animals) {
    console.log(animal);
}

console.log("More common for loop:");
for (let i = 0; i < animals.length; i++) {
    console.log(animals[i]);
}

// functions
function sum(x, y) {
    console.log(x + y);
}

sum(34, 55);
sum(12, 21);

// QUIRKS

// var accessible out of scope
for (var z = 0; z < 5; z++) {
    console.log(z);
}

console.log("Outside of for loop (var): " + z);

// global variables
console.log(anotherVar);

// weird string and number operations
console.log("35" + 5);  // result is string "355"
console.log("35" - 5);  // result is integer 30

// equality
console.log("22" == 22)  // returns true
console.log("22" === 22)  // returns false (as it should)

// hoisting example (calling a variable from another file)

