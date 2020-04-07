/* ANIMATIONS FOR SIDEBAR */

// Access elements
const logo = document.getElementById("logo")
const sidebar = document.getElementById("sidebar")
const mainContent = document.getElementById("mainContent")
const packageIcon = document.getElementById("package")
const packageIcon2 = document.getElementById("package2")

// Hover over logo
logo.onmouseover = function () {
    logo.className = "animated pulse infinite"
}

logo.onmouseleave = function () {
    logo.className = ""
}

// Hover over package icons
packageIcon.onmouseover = function () {
    packageIcon.className = "package-icon animated pulse infinite"
}

packageIcon.onmouseleave = function () {
    packageIcon.className = "package-icon"
}

packageIcon2.onmouseover = function () {
    packageIcon2.className = "package-icon animated pulse infinite"
}

packageIcon2.onmouseleave = function () {
    packageIcon2.className = "package-icon"
}

// Hover over sidebar
sidebar.onmouseover = function () {
    mainContent.style.filter = "brightness(80%)"
}

sidebar.onmouseleave = function () {
    mainContent.style.filter = "none"
}