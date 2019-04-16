let topLight = document.getElementById("topLight");
let middleLight = document.getElementById("middleLight");
let bottomLight = document.getElementById("bottomLight");

function redLight() {
    topLight.classList.remove("black");
    topLight.classList.add("red");
}

function yellowLight() {
    middleLight.classList.remove("black");
    middleLight.classList.add("yellow");
}

function greenLight() {
    bottomLight.classList.remove("black");
    bottomLight.classList.add("green");
}

function blackLight() {
    topLight.classList.remove("red");
    middleLight.classList.remove("yellow");
    bottomLight.classList.remove("green");

    topLight.classList.add("black");
    middleLight.classList.add("black");
    bottomLight.classList.add("black");
}
