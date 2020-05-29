var simple = {
  prop: "hello",
  myMethod: function () {
    console.log("The myMethod was called");
  },
};

simple.myMethod; // function 을 그냥 가져와 버려서 실행되지는 않는다.
simple.myMethod(); // 이렇게 실행시켜줘야함.

var myObj = {
  name: "Zeus",
  greet: function () {
    console.log("Hello " + this.name); //같은 객체 내의 값을 가져올때는 this를 사용
    console.log("Hello " + myObj.name); //이렇게도 실행이 되긴하넹
  },
};

myObj.greet();
