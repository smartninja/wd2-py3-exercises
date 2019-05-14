import { getBitts } from "../src/get-bitts.js";
import { postBitt } from "../src/post-bitt.js";

import * as firebase from "firebase/app";
import * as firebaseui from 'firebaseui';
import 'firebase/auth';
import "firebase/firestore";

// Firebase configuration (use your own apiKey, domain, project ID etc.)
let firebaseConfig = {
    apiKey: "AIzaSyA66i2hHPArcAgJ1KrWWTD3Ci-6Txm-PKc",
    authDomain: "bitter-web-app.firebaseapp.com",
    databaseURL: "https://bitter-web-app.firebaseio.com",
    projectId: "bitter-web-app",
    storageBucket: "bitter-web-app.appspot.com",
    messagingSenderId: "251455498605",
    appId: "1:251455498605:web:16f8980b41d08e00"
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

    createBittModal.style.display = "block";
    createBittFooter.style.display = "block";

    let firebaseAuthContainer = document.getElementById("firebaseui-auth-container");
    firebaseAuthContainer.style.display = "none";

    let usernameBittInput = document.getElementById("usernameBittInput");
    usernameBittInput.value = user.email;

    user.getIdToken().then(function(idToken) {
      let idTokenField = document.getElementById("idTokenField");
      idTokenField.value = idToken;
    }).catch(function(error) {
      // Handle error
    });

  } else {
    // No user is signed in.
  }
});
