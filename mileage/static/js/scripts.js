


let navbar = document.getElementById("navbar");
const navbutton = document.getElementById("navbutton");
const header = document.getElementById("header");
const logoutHeader = document.getElementById("logoutHeader")
const ergRefresh = document.getElementById('refreshErgPane')


navbutton.addEventListener("click", () => {
  navbar.classList.toggle("menu-toggle");

  
});

window.addEventListener("mouseup", (event) => {
  if (event.target != navbar && event.target != navbutton) {
    navbar.classList.remove("menu-toggle");
    // navbutton.classList.remove("menu-open")
    // logoutHeader.classList.remove("menu-open")
  }
})

window.addEventListener("load", () => {
  Sijax.request('checkForErgs');
})

ergRefresh.addEventListener("click", () => {
  Sijax.request('checkForErgs');
  document.getElementById('status').innerHTML = "...";
})

