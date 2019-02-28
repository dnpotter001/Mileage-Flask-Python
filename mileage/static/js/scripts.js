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


function secsToTime(secs){
  let hours = parseInt(secs / (60*60))
  let a = secs % (60*60)
  let minutes = parseInt(a / 60)
  a = secs % 60
  let seconds = a.toFixed(1) 
  return `${hours}:${minutes}:${seconds}`
}

function averageSplit(secs, distance){
  let splitSeconds = 500*(secs/distance);
  let m = parseInt(splitSeconds / 60);
  let s = (splitSeconds % 60).toFixed(1);
  if (s < 10) {
    s = "0" + s;
  }
  let split = `0${m}:${s}`
  return split
}

function intervalsToArray(intervals){
  console.log(intervals)
  let newIntervals = []
  intervals.forEach(i => {
    let interval = []
    interval.push(i.distance)
    interval.push(i.time)
    interval.push(i.rest)
    interval.push(averageSplit(i.time,i.distance))
    newIntervals.push(interval)
  }) 
  console.log(newIntervals)
  return newIntervals
}

function totalTime(intervals){
  let totalTime = 0
  intervals.forEach(i => {
    totalTime += i.time
  })
  return totalTime
}

function totalDistance(intervals){
  let dist = 0
  intervals.forEach(i => {
    dist += parseInt(i.distance)
  })
  return dist
}
