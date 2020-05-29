// function helloYou(name) {
//   console.log("Hello " + name);
// }

// helloYou("zeus");

// function addNum(num1, num2) {
//   console.log(num1 + num2);
// }

// addNum(2, 3);

// function helloSomeone(name = "Frankie") {
//   console.log("Hello " + name);
// }
// helloSomeone();
// helloSomeone("zeus");

// function formal(name = "Sam", title = "Sir") {
//   return title + " " + name;
// }

// console.log("Welcome " + formal());

// function timesFive(numInput) {
// Local scope to the function
//   var result = numInput * 5;
//   return result;
// }

// console.log(timesFive(4));
// Global Scope
var v = "GLOBAL V";
var stuff = "GLOBAL STUFF";

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff insdie func";
  console.log(stuff);
}

fun();
console.log(stuff);
