//element에 css 추가하는 법
var newCSS = {
  color: "white",
  background: "blue",
  border: "red",
};
$("h1").css(newCSS);
//element에 text추가
$("h1").text("asdfasdf");
//element에 html추가
$("h1").html("<strong>asdf</strong>");
//input element에 attribute 추가
$("input").eq(1).attr("placeholder", "hello");
//input element의 value변경
$("input").eq(0).val("hello~~");

//여러개의 element가 선택될경우 하나만 선택할때
var listItems = $("li");
listItems.eq(0).css("color", "orange");

//클래스 추가 제거
$("h1").addClass("turnRed");
$("h1").removeClass("turnRed");

$("h1").toggleClass("turnBlue");
$("h1").toggleClass("turnBlue");
