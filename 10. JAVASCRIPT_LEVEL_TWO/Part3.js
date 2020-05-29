myArr = ["one", "two", "three"];

var lastItem = myArr.pop();

myArr.push("new_item");

console.log(myArr);

var matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

matrix.length; //3

var arr = ["A", "B", "C"];

//for문으로 배열 원소 접근
for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

for (letter of arr) {
  console.log(letter);
}

for (jelly of arr) {
  console.log("hello");
}

for (letter of arr) {
  alert(letter);
}

arr.forEach(alert);

function addAwesome(name) {
  console.log(name + " is awesome!");
}

addAwesome("django");

var topics = ["python", "django", "science"];

topics.forEach(addAwesome);
