//fixed interval variables
const addInterval = document.getElementById("addInterval")
const remove = document.getElementById("remove")
const restInput = document.getElementById("restInput")
const rest = document.getElementsByClassName("rest")
const intervalCount = document.getElementById("intervalCount")
//buttons
const manualUploadPane = document.getElementById("manualUploadPane");
const manualButton = document.getElementById("manualButton");

const csvButton = document.getElementById("csvWorkout");
const singleDistButton = document.getElementById("singleDistButton");
const singleTimeButton = document.getElementById("singleTimeButton");
const intervalFixedButton = document.getElementById("intervalFixedButton");
const intervalVariableButton = document.getElementById("intervalVariableButton");
//add csv button

function SwapPanes(oldPane, newPane) {
  oldPane.classList.toggle("hidden");
  newPane.classList.toggle("hidden");
}

function TogglePane(pane) {
  pane.classList.toggle("hidden");
  console.log('hide/show');
}

//form panes
const csvPane = document.getElementById("csvPane");
const allManualPanes = document.getElementById("allManualForms");
const singleIntervalForm = document.getElementById("singleIntervalForm");
const intervalFixedForm = document.getElementById("intervalFixedForm");
const intervalVariableForm = document.getElementById("intervalVariableForm");

manualButton.addEventListener("click", () => { 
  TogglePane(manualUploadPane);
  csvPane.classList.add("hidden");
  allManualPanes.classList.add("hidden")
  singleIntervalForm.classList.add("hidden");
  intervalFixedForm.classList.add("hidden");
  intervalVariableForm.classList.add("hidden");
})

csvButton.addEventListener("click", () => { 
  SwapPanes(manualUploadPane, csvPane) 
  manualUploadPane.classList.add("hidden");
  TogglePane(allManualPanes);
})
singleDistButton.addEventListener("click", () => { 
  SwapPanes(manualUploadPane, singleIntervalForm) 
  TogglePane(allManualPanes);
})
singleTimeButton.addEventListener("click", () => { 
  SwapPanes(manualUploadPane, singleIntervalForm) 
  TogglePane(allManualPanes);
})
intervalFixedButton.addEventListener("click", () => { 
  SwapPanes(manualUploadPane, intervalFixedForm)
  TogglePane(allManualPanes); 
})
intervalVariableButton.addEventListener("click", () => { 
  SwapPanes(manualUploadPane, intervalVariableForm) 
  TogglePane(allManualPanes);
})


//single intervals
const singleDistance = document.getElementById("singleDistance");
const singleHours = document.getElementById("singleHours");
const singleMinutes = document.getElementById("singleMinutes");
const singleSeconds = document.getElementById("singleSeconds");
const singleSplit = document.getElementById("singleSplit");

function CalcSplit(distance, hours, minutes, seconds){
  let totalTime = parseInt(hours) * 60 * 60 + parseInt(minutes) * 60 + parseInt(seconds);
  let splitSeconds = 500*(totalTime/distance);
  let m = parseInt(splitSeconds / 60);
  let s = (splitSeconds % 60).toFixed(1);
  if (s < 10) {
    s = "0" + s;
  }
  let split = `0${m}:${s}`
  return split
}

singleDistance.addEventListener("change", ()=>{
  split.innerText = CalcSplit(singleDistance.value, singleHours.value, singleMinutes.value, singleSeconds.value)
})
singleHours.addEventListener("change", ()=>{
  split.innerText = CalcSplit(singleDistance.value, singleHours.value, singleMinutes.value, singleSeconds.value)
})
singleMinutes.addEventListener("change", ()=>{
  split.innerText = CalcSplit(singleDistance.value, singleHours.value, singleMinutes.value, singleSeconds.value)
})
singleSeconds.addEventListener("change", ()=>{
  split.innerText = CalcSplit(singleDistance.value, singleHours.value, singleMinutes.value, singleSeconds.value)
})

const uploadCSV = document.getElementById("uploadCSV");
const csvInput = document.getElementById("csvInput")
const fileNameLabel = document.getElementById("fileNameLabel")
const csvSubmit = document.getElementsByName("csvSubmit")
csvSubmit.disabled = true;

function validateCSV(input) {
  const fileName = input.value;
  const fileExt = fileName.split(".").pop().toLowerCase();
  if (fileExt === "csv") {
    fileNameLabel.innerText = csvInput.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
    fileNameLabel.classList.add("alert-success")
    fileNameLabel.classList.remove("alert-warning")

  } else { 
    fileNameLabel.innerText = "Not a CSV file";
    fileNameLabel.classList.remove("alert-success")
    fileNameLabel.classList.add("alert-warning")
  }
}

uploadCSV.addEventListener("click", () => {
  csvInput.click();
})

csvInput.addEventListener("change", e => {
  if (csvInput.value) {
    validateCSV(csvInput);
  }
  else {
    fileNameLabel.innerHTML = "No file chosen";
  }
});

//fixed interval form
let count = 0
function UpdateIntervalCount(count){
  intervalCount.value = count
}

addInterval.addEventListener("click", () => {
  console.log("add")
  count++
  UpdateIntervalCount(count)
  let newForm = document.createElement('div');
  newForm.classList.add("row")
  newForm.id = "interval" + count
  newForm.innerHTML = 
    `<label for="distance">Distance</label>
    <input id="distance" name="distance${count}" placeholder="Meters" required>
    <label for="time">Time</label>
    <input id="time" name="time${count}" placeholder="mm:ss" required>
    <label for="rest">Rest</label>
    <input id="rest" class="rest" name="rest${count}" placeholder="mm:ss" required readonly>
    `//<button id="remove" class="button red small">Remove</button>
  document.getElementById("intervalForms").appendChild(newForm);
})


remove.addEventListener("click", () => {
  console.log("remove")
  let toRemove = document.getElementById("interval" + count)
  toRemove.remove()
  count--
  UpdateIntervalCount(count)
})

restInput.addEventListener("input", () => {
  console.log("rest")
  for (let x of rest){
    x.value = restInput.value
  }
})  


