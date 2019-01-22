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
const manual = document.getElementById("manual");
const manualUpload = document.getElementById("manual-upload");
const manuaForm = document.getElementById("manual");

const singleDist = document.getElementById("singleDist");
const singleTime = document.getElementById("singleTime");
const intervalFixed = document.getElementById("intervalFixed");
const intervalVariable = document.getElementById("intervalVariable");

//form panes
const singleIntervalForm = document.getElementById("singleIntervalForm");
const intervalFixedForm = document.getElementById("intervalFixedForm");
const intervalVariableForm = document.getElementById("intervalVariableForm");


function SwapPanes(oldPane, newPane) {
  oldPane.classList.toggle("hidden");
  newPane.classList.toggle("hidden");
}

function TogglePane(pane) {
  pane.classList.toggle("hidden");
  console.log('hide/show');
}

manual.addEventListener("click", () => {
  TogglePane(manualUpload)
  singleIntervalForm.classList.add("hidden");
  intervalFixedForm.classList.add("hidden");
  intervalVariableForm.classList.add("hidden");
})

singleDist.addEventListener("click", () => { 
  SwapPanes(manualUpload, singleIntervalForm) 
})
singleTime.addEventListener("click", () => { 
  SwapPanes(manualUpload, singleIntervalForm) 
})
intervalFixed.addEventListener("click", () => { 
  SwapPanes(manualUpload, intervalFixedForm) 
})
intervalVariable.addEventListener("click", () => { 
  SwapPanes(manualUpload, intervalVariableForm) 
})

const distance = document.getElementById("distance");
const minutes = document.getElementById("minutes");
const split = document.getElementById("split");

function CalcSplit(distance, minutes){
  let splitDecimal = 500 * (minutes/distance);
  let splitString = splitDecimal.toString().split('.');
  let m = splitString[0]
  console.log(m)
  let s = (splitString[1] * 60).toString()
  console.log(s)
  let split = `0${m}.${s.substr(0,2)}:${s.substr(2,1)}`
  return split;
}

console.log(CalcSplit(8049, 30));

distance.addEventListener("change", ()=>{
  split.innerText = CalcSplit(distance.value, minutes.value)
})
minutes.addEventListener("change", ()=>{
  split.innerText = CalcSplit(distance.value, minutes.value)
})
