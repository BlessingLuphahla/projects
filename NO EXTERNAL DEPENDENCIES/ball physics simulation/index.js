var canvas = document.querySelector("#canvas");
var startButton = document.querySelector("#start");
var timeTaken = document.querySelector("#time-taken");
var maxHeight = document.querySelector("#max-height");
var ctx = canvas.getContext("2d");

ctx.transform(1, 0, 0, -1, 1, canvas.height);

startButton.onclick = start;

function start() {
  const angle = document.querySelector("#angle").value;
  const initialVelocity = document.querySelector("#init-velocity").value;
  draw(initialVelocity, angle);
}

function draw(Vo, angle) {
  const Vx = Vo * Math.cos(toRadians(angle));
  const Vy = Vo * Math.sin(toRadians(angle));

  const startTime = Date.now();
  const g = 9.81;
  const radius = 3;

  function update() {
    ctx.clearRect(0, 0, canvas.clientWidth, canvas.height);
    const time = (Date.now() - startTime) / 100;

    var x = Vx * time;
    var y = Vy * time - 0.5 * g * Math.pow(time, 2);

    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.fill();
    if (y < 0 + radius && time > 0.5) {
      timeTaken.textContent = `TIME TAKEN: ${Math.round(time)}s`;
      maxHeight.textContent = `RANGE: ${Math.round(Vx * time)}px`;
      return;
    }
    console.log(time);
    setTimeout(update, time);
  }

  update();
}

function toRadians(angle) {
  return (angle / 180) * Math.PI;
}
