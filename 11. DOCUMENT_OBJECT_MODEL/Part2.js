var p = document.querySelector("p");

p.textContent = "<strong>I'm bold</strong>";
p.innerHTML = "<strong>I'm bold</strong>";

var special = document.querySelector("#special");
var specialA = special.querySelector("a");
specialA.setAttribute("href", "https://www.amazon.com");
