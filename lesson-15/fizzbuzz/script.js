console.log("Welcome to FizzBuzz!")

let finalNumber = 16;

console.log("Let's count to " + finalNumber);

for (let i = 1; i <= finalNumber; i++) {

    if ((i % 3 === 0) && (i % 5 === 0)) {
        console.log("FizzBuzz");
    }
    else if (i % 3 === 0) {
        console.log("Fizz");
    }
    else if (i % 5 === 0) {
        console.log("Buzz");
    }
    else {
        console.log(i);
    }

}

console.log("FizzBuzz has completed the task. Goodbye!")
