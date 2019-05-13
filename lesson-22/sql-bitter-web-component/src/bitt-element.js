export class BittElement extends HTMLElement {
  constructor(text, username) {
    // Always call super() first in constructor
    super();

    // this if statement is useful if you'd like to create bitt-element directly in HTML using attributes
    // example: <bitt-element text="some text" username="ninja"></bitt-element>
    if (!text) {
        text = this.getAttribute("text");
        username = this.getAttribute("username");
    }

    // create a paragraph element
    let bittElement = document.createElement("p");

    // add bitt text and username to the paragraph
    bittElement.innerHTML = text + "<br> <small>" + username + "</small>";

    // append the element to the "shadow" DOM
    let shadow = this.attachShadow({mode: 'open'});
    shadow.appendChild(bittElement);
  }
}

// add <bitt-element> as a custom HTML element
customElements.define('bitt-element', BittElement);
