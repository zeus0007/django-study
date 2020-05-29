var carInfo = { make: "Toyota", year: 1990, model: "Camry" };
carInfo;
carInfo["make"];
carInfo[make]; //make를 variable로 인식할수도 있기 때문에 string type으로 넣어줘야 한다.

var myNewObject = { a: "hello", b: [1, 2, 3], c: { inside: ["a", "b"] } };

myNewObject["a"];
myNewObject["b"];
myNewObject["b"][1];
myNewObject["c"]["inside"][1];

carInfo;
carInfo["year"] = 2006;
carInfo;

console.dir(carInfo);

//object에는 순서가 없음을 기억해라.
for (key in carInfo) {
  console.log(key); //key값들만 불러온다.
  console.log(carInfo[key]); //이렇게 해야 value가 나온다.
}
