"use strict";

const navbar = document.getElementById("navbar");
const navbutton = document.getElementById("navbutton");
const header = document.getElementById("header");
const ergRefresh = document.getElementById('refreshErgPane')

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

ergRefresh.addEventListener("click", () => {
  Sijax.request('checkForErgs');
  document.getElementById('status').innerHTML = "...";
})


function secsToTime(secs){
  let hours = parseInt(secs / (60*60))
  let a = secs % (60*60)
  let minutes = parseInt(a / 60)
  a = secs % 60
  let seconds = a.toFixed(1) 
  let formattedTime = ""
  if (seconds < 10){
    seconds = "0"+ seconds
  }
  if (hours == 0){
    formattedTime = `${minutes}:${seconds}`
  } 
  if (seconds == 0.0){
    formattedTime = `${minutes}:00`
  }
  
  if (hours != 0) {
    formattedTime = `${hours}:${minutes}:${seconds}`
  }
  return formattedTime
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
  let count = 1
  intervals.forEach(i => {
    let interval = []
    interval.push(count)
    interval.push(i.distance)
    interval.push(i.time)
    interval.push(i.rest)
    interval.push(500*(i.time/i.distance))
    newIntervals.push(interval)
    count++
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

function createTable(intervals){
  let table = document.createElement("table");
  let tableRow = document.createElement("tr");

  //labels
  let labels = ['Interval', 'Distance', 'Time', 'Rest', 'Split/500']
  labels.forEach((x) => {
    let cell = document.createElement("td");
    cell.innerHTML = x
    tableRow.append(cell)
  });
  table.append(tableRow)

  intervals.forEach((interval) => {
    interval[2] = secsToTime(interval[2])
    interval[3] = secsToTime(interval[3])
    interval[4] = secsToTime(interval[4])
  })

  intervals.forEach((interval) => { 
    console.log(interval)
    tableRow = document.createElement("tr");
    interval.forEach((data) => {
      let cell = document.createElement("td");
      cell.innerHTML = data
      tableRow.append(cell)
    })
    table.append(tableRow)
  })
  return table
}