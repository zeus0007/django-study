var tds = document.querySelectorAll("td");
var restart = document.querySelector("#restartBtn");

//리스타트 함수
restart.addEventListener("click", function () {
  for (td of tds) {
    resetStatus(td);
  }
});

//상황에 따른 status적용
function changeStatus(prevStatus) {
  if (prevStatus == "X") {
    return "O";
  } else if (prevStatus == "O") {
    return "";
  } else if (prevStatus == "") {
    return "X";
  }
}
//매 클릭시 textContent에 넣어줄 텍스트값 적용
function setStatus(id) {
  id.textContent = changeStatus(id.textContent);
}

//reset버튼 클릭시 ""을 넣어주기 위한 값 세팅.
function resetStatus(id) {
  id.textContent = changeStatus("O");
}

//클릭 이벤트 적용
function ticTacToe(id) {
  id.addEventListener("click", function () {
    setStatus(id);
  });
}

//각 칸 별 이벤트 적용
for (td of tds) {
  ticTacToe(td);
}
