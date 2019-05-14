import { getBitts } from "../src/get-bitts.js";
import { postBitt } from "../src/post-bitt.js";

import * as firebase from "firebase/app";
import * as firebaseui from 'firebaseui';
import 'firebase/auth';
import "firebase/firestore";

// Firebase configuration (use your own apiKey, domain, project ID etc.)
let firebaseConfig = {
    apiKey: "<your-api-key-here>",
    authDomain: "<your-project-id>.firebaseapp.com",
    databaseURL: "https://<your-project-id>.firebaseio.com",
    projectId: "<your-project-id>",
    storageBucket: "<your-project-id>.appspot.com",
    messagingSenderId: "<your-message-sender-id>",
    appId: "<your-app-id>"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// hide the create bitt modal content
let createBittModal = document.getElementById("create-bitt-modal");
createBittModal.style.display = "none";
let createBittFooter = document.getElementById("bitt-modal-footer");
createBittFooter.style.display = "none";

// show the firebase auth UI
let ui = new firebaseui.auth.AuthUI(firebase.auth());

ui.start('#firebaseui-auth-container', {
  signInSuccessUrl: '/',
  signInOptions: [
    firebase.auth.GoogleAuthProvider.PROVIDER_ID,
    //firebase.auth.FacebookAuthProvider.PROVIDER_ID,
    firebase.auth.EmailAuthProvider.PROVIDER_ID,
    //firebase.auth.PhoneAuthProvider.PROVIDER_ID
  ],

});

// get bitts from the Bitter backend
getBitts();  // initial run (before the interval)
setInterval(getBitts, 180*1000);  // 180 * 1000 miliseconds = 3 min

let bittSubmit = document.getElementById("bittSubmit");
bittSubmit.addEventListener("click", postBitt);

// Observe the Firebase authentication state. When it changes, update the DOM.
firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    console.log(user);

    createBittModal.style.display = "block";
    createBittFooter.style.display = "block";

    let firebaseAuthContainer = document.getElementById("firebaseui-auth-container");
    firebaseAuthContainer.style.display = "none";

    let usernameBittInput = document.getElementById("usernameBittInput");
    usernameBittInput.value = user.email;
  } else {
    // No user is signed in.
  }
});
