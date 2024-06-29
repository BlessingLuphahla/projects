var cells = document.querySelectorAll(".cell");
var button = document.querySelector("#restart");
var statusText = document.querySelector("#game-container > h2");

let currentPlayer = "X";
let running = false;
let options = ["", "", "", "", "", "", "", "", ""];
let winConditions = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 4, 8],
  [0, 3, 6],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [2, 4, 6],
];

initialiseGame();

function initialiseGame() {
  running = true;
  if (running) {
    cells.forEach((cell) => cell.addEventListener("click", cellClicked));

    button.addEventListener("click", restart);
    statusText.textContent = `${currentPlayer} 's TURN`;
  }
}

function cellClicked() {
  var cellIndex = this.getAttribute("cellIndex");

  if (options[cellIndex] != "" || !running) {
    return;
  }
  this.textContent = currentPlayer;
  options[cellIndex] = currentPlayer;
  changePlayer();

  checkWinner();
}
function changePlayer() {
  currentPlayer = currentPlayer == "X" ? "O" : "X";
  this.textContent = currentPlayer;
  statusText.textContent = `${currentPlayer}'S TURN`;
}
function checkWinner() {
  var winner = false;

  for (var i = 0; i < winConditions.length; i++) {
    var conditions = winConditions[i];

    var cellA = options[conditions[0]];
    var cellB = options[conditions[1]];
    var cellC = options[conditions[2]];

    if (cellA != "" && cellA == cellB && cellB == cellC) {
      winner = true;
      break;
    }
  }

  if (winner) {
    currentPlayer = currentPlayer == "X" ? "O" : "X";

    statusText.textContent = `PLAYER '${currentPlayer}' WINS`;
    running = false;
  } else if (!options.includes("")) {
    statusText.textContent = "ITS A DRAW";
    running = false;
  }
}

function restart() {
  running = true;
  currentPlayer = "X";
  statusText.textContent = `${currentPlayer}'S TURN`
  options = ["", "", "", "", "", "", "", "", ""];

  cells.forEach((cell) => {
    cell.textContent = "";
  });
}
