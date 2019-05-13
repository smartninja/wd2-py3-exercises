(function () {

    fetch('/get-all-bitts')
        .then(function(response) {
            return response.text();
        })
        .then(function(text) {
            let container = document.getElementById("bittsContainer");
            let bitts = JSON.parse(text);

            for (let bitt of bitts) {
                let bittElement = document.createElement("p");
                bittElement.innerHTML = bitt.text + "<br> <small>" + bitt.username + "</small>";

                container.appendChild(bittElement);
            }
        })
        .catch(function(error) {
            console.log('Request failed', error);
        });

}())
