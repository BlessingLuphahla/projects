var canvas = document.querySelector("#wrapper > canvas");
var reset = document.querySelector("#reset");
var pause = document.querySelector("#pause");
var score = document.querySelector("#score > span");
var ctx = canvas.getContext("2d");

const gameWidth = canvas.width;
const gameHeight = canvas.height;
const snakeColor = "rgb(255, 0, 242)";
const screenBackground = "rgb(0, 242, 255)";
const foodColor = "rgba(0,0,0,0.8)";

const unitSize = 7;
let scoreValue = 0;

let Vx = unitSize;
let Vy = 0;

let running = false;
let gameOver = false;
let paused = false;

let foodX;
let foodY;

let snake = [
  { x: unitSize * 4, y: 0 },
  { x: unitSize * 3, y: 0 },
  { x: unitSize * 2, y: 0 },
  { x: unitSize * 1, y: 0 },
  { x: unitSize * 0, y: 0 },
];

initialiseGame();
document.addEventListener("keydown", changeDirection);
reset.addEventListener("click", resetGame);
pause.addEventListener("click", pauseGame);

function initialiseGame() {
  running = true;
  score.textContent = scoreValue;
  createFood();
  setInterval(nextFrame, 40);
}

function nextFrame() {
  if (running && !paused && !gameOver) {
    clearSreen();
    drawFood();
    drawSnake();
    moveSnake();
    checkIfFoodEaten();
    checkIfGameOver();
  } else {
    displayGameOver();
  }
}
function displayGameOver() {
  if (gameOver) {
    ctx.fillStyle = "red";
    ctx.font = "50px monospace";
    ctx.textAlign = "center";
    ctx.fillText("GAME OVER", gameWidth / 2, gameHeight / 2);
  }
}

function checkIfGameOver() {
  for (var i = 3; i < snake.length; i++) {
    if (snake[i].x == snake[0].x && snake[i].y == snake[0].y) {
      gameOver = true;
      break;
    }
  }
}

function checkIfFoodEaten() {
  if (snake[0].x == foodX && snake[0].y == foodY) {
    snake.push(snake[0].x + unitSize, snake[0].y + unitSize);
    createFood();
    scoreValue++;
    score.textContent = scoreValue;
  }
}

function drawFood() {
  ctx.fillStyle = foodColor;
  ctx.fillRect(foodX, foodY, unitSize, unitSize);
}

function createFood() {
  function _generateRandomLocation(min, max) {
    const randLocationCorordinate =
      Math.round((Math.random() * (max - min) + min) / unitSize) * unitSize;

    return randLocationCorordinate;
  }

  foodX = _generateRandomLocation(0, gameWidth - unitSize);
  foodY = _generateRandomLocation(0, gameHeight - unitSize);
}

function clearSreen() {
  ctx.fillStyle = screenBackground;
  ctx.fillRect(0, 0, gameWidth, gameHeight);
}

function moveSnake() {
  const head = { x: snake[0].x + Vx, y: snake[0].y + Vy };
  snake.unshift(head);
  snake.pop();
}

function drawSnake() {
  ctx.fillStyle = snakeColor;
  snake.forEach((snakePart) => {
    ctx.fillRect(snakePart.x, snakePart.y, unitSize, unitSize);
  });
}

function pauseGame() {
  if (!gameOver) {
    function _showPaused() {
      ctx.fillStyle = "green";
      ctx.font = "50px monospace";
      ctx.textAlign = "center";
      ctx.fillText("PAUSED", gameWidth / 2, gameHeight / 2);
    }

    if (paused) {
      paused = false;
      running = true;
    } else {
      paused = true;
      _showPaused();
      running = false;
    }
  }
}

function changeDirection(e) {
  if (e.key == "p" || e.key == "P") {
    pauseGame();
  }
  if (e.key == "r" || e.key == "R") {
    resetGame();
  }

  const UP = "ArrowUp";
  const DOWN = "ArrowDown";
  const RIGHT = "ArrowRight";
  const LEFT = "ArrowLeft";

  const goingUp = Vy == -unitSize;
  const goingDown = Vy == unitSize;
  const goingLeft = Vx == -unitSize;
  const goingRight = Vx == unitSize;

  if (e.key == UP && !goingDown) {
    Vy = -unitSize;
    Vx = 0;
  }

  if (e.key == DOWN && !goingUp) {
    Vy = unitSize;
    Vx = 0;
  }

  if (e.key == RIGHT && !goingLeft) {
    Vx = unitSize;
    Vy = 0;
  }

  if (e.key == LEFT && !goingRight) {
    Vx = -unitSize;
    Vy = 0;
  }
}

function resetGame() {
  paused = false;
  running = true;
  Vx = unitSize;
  Vy = 0;
  gameOver = false;
  scoreValue = 0;
  score.textContent = scoreValue;

  snake = [
    { x: unitSize * 4, y: 0 },
    { x: unitSize * 3, y: 0 },
    { x: unitSize * 2, y: 0 },
    { x: unitSize * 1, y: 0 },
    { x: unitSize * 0, y: 0 },
  ];
}
