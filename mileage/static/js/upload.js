//fixed interval variables
const addInterval = document.getElementById("addInterval")
const remove = document.getElementById("remove")
const restInput = document.getElementById("restInput")
const rest = document.getElementsByClassName("rest")
const intervalCount = document.getElementById("intervalCount")
const intervalCountVariable = document.getElementById("intervalCountVariable")
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
const singleTime = document.getElementById("singleTime");
const singleSplit = document.getElementById("singleSplit");

function CalcSplit(distance, timeString){
  timeArray = timeString.split(":")
  let totalTime = 0;

  switch (timeArray.length) {
    case 1:
      totalTime = parseFloat(timeArray[0])
      break;
  
    case 2:
      totalTime = parseInt(timeArray[0]) * 60 + parseFloat(timeArray[1]);
      break;
    
    case 3:
      totalTime = parseInt(timeArray[0]) * 60 * 60 + parseInt(timeArray[1]) * 60 + parseFloat(timeArray[2]);
      break;
  }

  let splitSeconds = 500*(totalTime/distance);
  let m = parseInt(splitSeconds / 60);
  let s = (splitSeconds % 60).toFixed(1);
  if (s < 10) {
    s = "0" + s;
  }
  let split = `0${m}:${s}`
  return split
}

singleDistance.addEventListener("input", ()=>{
  singleSplit.innerText = CalcSplit(singleDistance.value, singleTime.value)
})
singleTime.addEventListener("input", ()=>{
  singleSplit.innerText = CalcSplit(singleDistance.value, singleTime.value)
})


  //cvs upload
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
let variableCount = 0

function UpdateIntervalCount(count){
  intervalCount.value = count
  intervalCountVariable.value = variableCount
  for(let x = 1; x <= count; x++){
    const distInput = document.getElementById(`distance${x}`)
    const timeInput = document.getElementById(`time${x}`)
    const splitInterval = document.getElementById(`split${x}`)
    distInput.addEventListener("change", () => {
      splitInterval.value = CalcSplit(distInput.value, timeInput.value)
    })
    timeInput.addEventListener("change", () => {
      splitInterval.value = CalcSplit(distInput.value, timeInput.value)
    })
  } 
}

addInterval.addEventListener("click", () => {
  console.log("add")
  count++
  let newForm = document.createElement('div');
  newForm.classList.add("intervalInput")
  newForm.id = "interval" + count
  newForm.innerHTML = 
  `
  <div class="fieldRow">
    <label for="distance">Distance: </label>
    <input id="distance${count}" name="distance${count}" placeholder="Meters" required>
  </div>
  <div class="fieldRow">
    <label for="time">Time: </label>
    <input id="time${count}" name="time${count}" placeholder="Minute:Seconds" required pattern="^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9](.[0-9])?$" title="Minutes:Seconds.Centiseconds(optional)">
  </div>
  <div class="fieldRow">
    <label>Split: </label> 
    <input id="split${count}" readonly></input>
  </div>
  `
  let header = document.createElement('h3')
  header.id = "intervalHeader"+count
  header.classList.add("pad10")
  header.innerText = `Interval ${count}`
  document.getElementById("intervalForms").appendChild(header);
  document.getElementById("intervalForms").appendChild(newForm);
  UpdateIntervalCount(count)
})



remove.addEventListener("click", () => {
  console.log("remove")
  let toRemove = document.getElementById("interval" + count)
  let headerRemove = document.getElementById("intervalHeader"+count)
  toRemove.remove()
  headerRemove.remove()
  count--
  UpdateIntervalCount(count)
}) 

//intervals variable
const addVarInt = document.getElementById("addVariableInterval")
const removeVarInt = document.getElementById("removeVariable")

//need a new counter 
//refactor old one first 
//event listeners and interval fields 
//route for upload

addVarInt.addEventListener("click", () => {
  console.log("add")
  variableCount++
  let newForm = document.createElement('div');
  newForm.classList.add("intervalInput")
  newForm.id = "interval" + variableCount
  newForm.innerHTML = 
  `
  <div class="fieldRow">
    <label for="distance">Distance: </label>
    <input id="distance${variableCount}" name="distance${variableCount}" placeholder="Meters" required>
  </div>
  <div class="fieldRow">
    <label for="time">Time: </label>
    <input id="time${variableCount}" name="time${variableCount}" placeholder="Minute:Seconds" required pattern="^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9](.[0-9])?$" title="Minutes:Seconds.Centiseconds(Optional)">
  </div>
  <div class="fieldRow">
    <label for="rest">Rest: </label>
    <input id="rest${variableCount}" name="rest${variableCount}" placeholder="Minute:Seconds" required pattern="^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$" title="Minutes:Seconds">
  </div>
  <div class="fieldRow">
    <label>Split: </label> 
    <input id="split${variableCount}" readonly></input>
  </div>
  `
  let header = document.createElement('h3')
  header.id = "intervalHeader"+variableCount
  header.classList.add("pad10")
  header.innerText = `Interval ${variableCount}`
  document.getElementById("intervalFormsVariable").appendChild(header);
  document.getElementById("intervalFormsVariable").appendChild(newForm);
  UpdateIntervalCount(variableCount)
})

removeVarInt.addEventListener("click", () => {
  console.log("remove")
  let toRemove = document.getElementById("interval" + variableCount)
  let headerRemove = document.getElementById("intervalHeader"+variableCount)
  toRemove.remove()
  headerRemove.remove()
  variableCount--
  UpdateIntervalCount(variableCount)
}) 