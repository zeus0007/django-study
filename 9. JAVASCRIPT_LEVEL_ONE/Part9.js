// 내코드
// var firstName = prompt("First Name: ");
// var lastName = prompt("Last Name: ");
// var age = prompt("Age: ");
// var tall = prompt("Tall: ");
// var petName = prompt("Pet Name: ");

// var message = "Name : Jose Johnson\nAge : 26\nTall : 175cm\nPet Name: Sammy";

// if (firstName[0] == lastName[0]) {
//   if (age >= 20 && age <= 30) {
//     if (tall >= 170) {
//       if (petName[petName.length - 1] == "y") {
//         alert(message);
//       } else {
//         alert("Welcome to Our Page!");
//       }
//     } else {
//       alert("Welcome to Our Page!");
//     }
//   } else {
//     alert("Welcome to Our Page!");
//   }
// } else {
//   alert("Welcome to Our Page!");
// }

//솔루션
var firstName = prompt("First Name: ");
var lastName = prompt("Last Name: ");
var age = prompt("Age: ");
var tall = prompt("Tall: ");
var petName = prompt("Pet Name: ");
var nameCond = false;
var ageCond = false;
var tallCond = false;
var petCond = false;

if (firstName[0] == lastName[0]) {
  nameCond = true;
} else {
  nameCond = false;
}
if (age >= 20 && age <= 30) {
  ageCond = true;
} else {
  ageCond = false;
}
if (tall >= 170) {
  tallCond = true;
} else {
  tallCond = false;
}
if (petName[petName.length - 1] == "y") {
  petCond = true;
} else {
  petCond = false;
}

if (nameCond && ageCond && tallCond && petCond) {
  alert(message);
} else {
  alert("Welcome to Our Page!");
}
