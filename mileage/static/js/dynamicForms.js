// const intervalCount = document.getElementById("intervalCount")
// const intervalWarning = document.getElementById("intervalWarning")
// const fieldContainer = document.getElementById("intervalFields")

// intervalCount.addEventListener("change", () => {
//   if (intervalCount.value > 20) {
//     intervalWarning.innerText = "Too many intervals"
//     intervalWarning.classList.add("alert-warning")
//   } else {
//     intervalWarning.innerText = ""
//     intervalWarning.classList.remove("alert-warning")

//     for(num in intervalCount){
      
//     }

//   } 
// })

const restInput = document.getElementById("restInput")
const rest = document.getElementsByClassName("rest")
restInput.addEventListener("change", () => {
  console.log("change")
  for (var i = 0; i < rest.length; i++) {
    rest[i].value = restInput.value
  }
})

