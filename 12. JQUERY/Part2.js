// $("h1").click(function () {
//   //   console.log("There was a click!");
//   $(this).text("I was changed!"); //여기서 this는 h1을 말함.
// });

// $("li").click(function () {
//   console.log("any li was clicked!");
// });

// //KEY PRESS
// $("input")
//   .eq(0)
//   .keypress(function () {
//     if (event.which === 13) {
//       //enter key
//       $("h3").toggleClass("turnBlue");
//     }
//     // console.log(event);
//     // $("h3").toggleClass("turnBlue");
//   });

// // on()
// // $("h1").on("dblclick", function () {
// $("h1").on("mouseenter", function () { //hover
//   $(this).toggleClass("turnBlue");
// });

$("input")
  .eq(1)
  .on("click", function () {
    $(".container").slideUp(3000); ///3초 후에 동작함. //effects
  });
