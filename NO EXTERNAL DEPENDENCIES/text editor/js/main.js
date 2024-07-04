var open = document.querySelector("#options > label");
var save = document.querySelector("#save");
var fileInput = document.querySelector("#file");
var textEditor = document.querySelector("#text-editor");

fileInput.addEventListener("change", function () {
  const reader = new FileReader();
  const file = fileInput.files[0];
  console.log(file);

  reader.readAsText(file);

  reader.addEventListener("load", function (e) {
    const info = e.target.result;
    textEditor.textContent = info;
  });
});

save.addEventListener("click", function () {
  var info = textEditor.value;
  console.log(info);
  var blob = new Blob([info], { type: "text/plain" });
  var url = URL.createObjectURL(blob);

  const fileName = prompt(
    "you will find your file in downloads \n what do you wanna save it as? "
  );

  save.href = url;
  save.download = `${fileName}.txt`;
});
