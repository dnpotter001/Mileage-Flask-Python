const intervalCount = document.getElementById("intervalCount")
const incremement = document.getElementById("increment")
const decremement = document.getElementById("decrement")

incremement.addEventListener("click",() => {
  intervalCount.value++
})

decremement.addEventListener("click",() => {
  if(intervalCount.value != 0) {
    intervalCount.value--
  }
})

intervalCount.addEventListener("input", () => {
  console.log("change")
  for(let i = 0; i <= intervalCount.value; i++){
    let distanceLabel = document.createElement("label")
    let TimeLabel = document.createElement("label")
    let RestLabel = document.createElement("label")
    distanceLabel.innerText = "Distance";
    TimeLabel.innerText = "Total Time (Minutes)";
    RestLabel.innerText = "Distance (Rest)";

    let distance = document.createElement("input")
    distance.name = "distance" + i
    distance.placeholder = "Meters"
    distance.required = "required" 
    
    let holder = document.createElement("div")
    holder.classList.add("row")
    holder.appendChild(distanceLable, distance)
    let intervalForm = document.getElementById("intervalForm")
    intervalForm.appendChild(holder)
  }
})


// const restInput = document.getElementById("restInput")
// const rest = document.getElementsByClassName("rest")
// restInput.addEventListener("change", () => {
//   console.log("change")
//   for (var i = 0; i < rest.length; i++) {
//     rest[i].value = restInput.value
//   }
// })

