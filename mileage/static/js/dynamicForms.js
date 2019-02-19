const intervalCount = document.getElementById("intervalCount")
const intervalWarning = document.getElementById("intervalWarning")
const fieldContainer = document.getElementById("intervalFields")

intervalCount.addEventListener("change", () => {
  if (intervalCount.value > 20) {
    intervalWarning.innerText = "Too many intervals"
    intervalWarning.classList.add("alert-warning")
  } else {
    intervalWarning.innerText = ""
    intervalWarning.classList.remove("alert-warning")

    for(num in intervalCount){
      
    }

  } 
})