"use strict";

const navbar = document.getElementById("navbar");
const navbutton = document.getElementById("navbutton");
const header = document.getElementById("header");

navbutton.addEventListener("click", () => {
  //console.log("toggled");
  navbar.classList.toggle("menu-toggle");
  navbutton.classList.toggle("menu-open")
});

window.addEventListener("mouseup", (event) => {
  if (event.target != navbar && event.target != navbutton) {
    //console.log("closing menu")
    navbar.classList.remove("menu-toggle");
    navbutton.classList.remove("menu-open")
  }
})

window.addEventListener("load", () => {
  Sijax.request('checkForErgs');
})

document.getElementById('refreshErgPane').addEventListener("click", () => {
  Sijax.request('checkForErgs');
  document.getElementById('status').innerHTML = "...";
})

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



const distance = document.getElementById("distance");
const hours = document.getElementById("hours");
const minutes = document.getElementById("minutes");
const seconds = document.getElementById("seconds");
const split = document.getElementById("split");

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

distance.addEventListener("change", ()=>{
  split.innerText = CalcSplit(distance.value, hours.value, minutes.value, seconds.value)
})
hours.addEventListener("change", ()=>{
  split.innerText = CalcSplit(distance.value, hours.value, minutes.value, seconds.value)
})
minutes.addEventListener("change", ()=>{
  split.innerText = CalcSplit(distance.value, hours.value, minutes.value, seconds.value)
})
seconds.addEventListener("change", ()=>{
  split.innerText = CalcSplit(distance.value, hours.value, minutes.value, seconds.value)
})

