export function getBitts() {
    console.log("occurring every three minutes");

    // get bitts from storage
    let storedBittsRaw = localStorage.bitts;

    let lastBittId = null;
    let storedBitts = null;

    if (storedBittsRaw) { // if there are any bitts in storage, get ID from the first one (the latest Bitt)
        storedBitts = JSON.parse(storedBittsRaw);
        lastBittId = storedBitts[0].id;
    }

    fetch('/get-all-bitts?lastid='+lastBittId)
        .then(function(response) {
            return response.text();
        })
        .then(function(text) {
            console.log(text);

            let response = JSON.parse(text);

            // if browser storage is in sync with server database do this
            if (response.synced) {
                console.log("Synced!");
            } else { // if not, save the bitts in browser local storage
                localStorage.bitts = text;
                storedBitts = JSON.parse(text); // save the bitts also in the storedBitts variable
            }

            // show bitts in HTML
            let container = document.getElementById("bittsContainer");
            container.innerHTML = "";

            for (let bitt of storedBitts) {
                let bittElement = document.createElement("p");
                bittElement.innerHTML = bitt.text + "<br> <small>" + bitt.username + "</small>";

                container.appendChild(bittElement);
            }

        })
        .catch(function(error) {
            console.log('Request failed', error);
        });
}
