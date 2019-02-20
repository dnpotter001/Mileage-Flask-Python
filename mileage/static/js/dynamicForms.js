const addInterval = document.getElementById("addInterval")
const remove = document.getElementById("remove")
let count = 0

addInterval.addEventListener("click", () => {
  console.log("add")
  count++
  let newForm = document.createElement('div');
  newForm.classList.add("row")
  newForm.id = "interval" + count
  newForm.innerHTML = 
    `<label for="distance">Distance</label>
    <input id="distance" name="distance${count}" placeholder="Meters" required>
    <label for="time">Time (Minutes)</label>
    <input id="time" name="time${count}" placeholder="e.g. 1:30" required>
    <label for="rest">Rest (Minutes)</label>
    <input id="rest" name="rest${count}" placeholder="e.g. 1:30" required readonly>
    `//<button id="remove" class="button red small">Remove</button>
  document.getElementById("intervalForms").appendChild(newForm);
})

remove.addEventListener("click", () => {
  console.log("remove")
  let toRemove = document.getElementById("interval" + count)
  toRemove.remove()
  count--
})