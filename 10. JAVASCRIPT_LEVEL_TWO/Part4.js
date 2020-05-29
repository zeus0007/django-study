names = [];
var input = "";
while (true) {
  input = prompt("Please select an action: add, remove, display or quit");

  if (input == "add") {
    var name = prompt("plz type name : ");
    names.push(name);
  } else if (input == "remove") {
    var name = prompt("plz type name that you want delete : ");
    names.splice(names.indexOf(name), 1);
  } else if (input == "display") {
    console.log(names);
  } else if (input == "quit") {
    alert("bye~");
    break;
  } else {
    alert("command error");
  }
}
