let resultInfo = document.getElementById("resultInfo");
let secret = Math.floor(Math.random() * 100) + 1;

function guessSecretNumber() {
    let guessInput = parseInt(document.getElementById("guess").value);

    if(guessInput === secret) {
        resultInfo.textContent = "CONGRATS! " + secret + " is the secret number! :) Reload the site to start a new game.";
    } else if(guessInput > secret) {
        resultInfo.textContent = "Your guess is TOO HIGH! Try something lower.";
    } else if(guessInput < secret) {
        resultInfo.textContent = "Your guess is TOO LOW! Try something higher.";
    }
}
