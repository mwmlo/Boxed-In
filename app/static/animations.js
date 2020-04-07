/* HOME PAGE ANIMATIONS */

// Access elements
const signUpButton = document.getElementById("signup")
const logInButton = document.getElementById("login")
const homePage = document.getElementById("homePage")
const boxImage = document.getElementById("boxImage")

// Hover over sign up or log in button to zoom in

signUpButton.onmouseover = function() {
    homePage.className = "background animated pulse infinite slower"
}

logInButton.onmouseover = function () {
    homePage.className = "background animated pulse infinite slower"
}

signUpButton.onmouseleave = function () {
    homePage.className = "background"
}

logInButton.onmouseleave = function () {
    homePage.className = "background"
}

// Boxes slide back down when moving to next page

signUpButton.onclick = function () {
    boxImage.className = "boxBackground animated slideOutDown"
}

logInButton.onclick = function () {
    boxImage.className = "boxBackground animated slideOutDown"
}
