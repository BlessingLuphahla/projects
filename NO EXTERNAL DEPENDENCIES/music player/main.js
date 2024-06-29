var play = document.querySelector("#play");
var pause = document.querySelector("#pause");
var restart = document.querySelector("#restart");
var duration = document.querySelector("#duration");
var song = document.querySelector("#player > audio");
var details = document.querySelector("#details p");
var chooseSong = document.querySelector("#player > label");
var fileInput = document.querySelector("#file");
var state = document.querySelector("#state");
var totalTime = document.querySelector("#total-time");
var slider = document.querySelector("#slider");
var seeker = document.querySelector("#seeker");
var playlist = document.querySelector("#playlist");
var previous = document.querySelector("#previous");
var next = document.querySelector("#next");

var file;
var files;
var intervalID;
var currentSong;

fileInput.addEventListener("change", function () {
  files = fileInput.files;
  for (file of files) {
    var blob = new Blob([file], { type: "audio/mp3" });
    var url = URL.createObjectURL(blob);
    var button = document.createElement("div");
    button.setAttribute("class", "button");
    button.setAttribute("info", url);
    button.textContent = `${file.name}`;
    playlist.appendChild(button);
  }

  var songs = document.querySelectorAll("#playlist > div");

  file = fileInput.files[0];
  if (file) {
    var blob = new Blob([file], { type: "audio/mp3" });
    var url = URL.createObjectURL(blob);

    song.src = url;
    playSong();
  }

  songs.forEach((audio) =>
    audio.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();

      song.src = e.target.getAttribute("info");

      playSong();
      details.textContent = e.target.textContent;
    })
  );

  previous.addEventListener("click", function (e) {
    e.preventDefault();
    e.stopPropagation();
    currentSong = document.querySelector(`div[info="${song.src}"]`);

    if (currentSong) {
      var previousSong = currentSong.previousElementSibling;
      if (previousSong) {
        song.src = previousSong.getAttribute("info");
        playSong();
        details.textContent = previousSong.textContent;
      } else {
        console.log("we in the first one dawg");
      }
    } else {
      console.log("we in the first one");
    }
  });

  next.addEventListener("click", function (e) {
    e.preventDefault();
    e.stopPropagation();
    currentSong = document.querySelector(`div[info="${song.src}"]`);

    if (currentSong) {
      var nextSong = currentSong.nextElementSibling;
      if (nextSong) {
        song.src = nextSong.getAttribute("info");
        playSong();
        details.textContent = nextSong.textContent;
      } else {
        console.log("we already reached the end");
      }
    } else {
      song.src = document
        .querySelector(`#playlist > div`)
        .nextElementSibling.getAttribute("info");
      playSong();
    }
  });
});

function parseTime(seconds) {
  var mins = Number(Math.round(seconds / 60));
  var secs = Number(Math.round(seconds) % 60);

  if (mins < 10) {
    mins = "0" + mins.toString();
  }
  if (secs < 10) {
    secs = "0" + secs.toString();
  }

  return `${mins}:${secs}`;
}

play.addEventListener("click", playSong);
pause.addEventListener("click", pauseSong);

function playSong() {
  if (file) {
    details.textContent = file.name;
  }
  song.play();
  checkState();
  updateDuration();

  function updateDuration() {
    intervalID = setInterval(function () {
      duration.textContent = `${parseTime(song.currentTime)}`;
      totalTime.textContent = ` ${parseTime(song.duration)}`;
      slider.style.width = `${(song.currentTime / song.duration).toLocaleString(
        undefined,
        {
          style: "percent",
        }
      )}`;
    }, 10);
  }
}

function pauseSong() {
  if (!song.paused) {
    song.pause();
    checkState();
  }
}

function checkState() {
  if (song.paused) {
    state.textContent = "PAUSED";
    state.style.color = "rgb(255,0,0)";
  } else {
    state.textContent = "PLAYING...";
    state.style.color = "rgb(0,255,0)";
  }
}

seeker.addEventListener("mousedown", function (e) {
  var sliderRect = seeker.getBoundingClientRect();

  const x = e.clientX - sliderRect.left;
  const clickPosition = x / seeker.offsetWidth;

  song.currentTime = clickPosition * song.duration;
});

song.addEventListener("ended", restartSong);
restart.addEventListener("click", restartSong);

function restartSong() {
  clearInterval(intervalID);
  song.currentTime = 0;
  slider.style.width = "0%";
  song.paused = false;
  playSong();
}
