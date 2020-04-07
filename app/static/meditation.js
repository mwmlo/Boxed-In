/* Control playback of meditation tracks */

// Access individual elements on screen
// First meditation
var music1 = document.getElementById('music1');
var duration1 = music1.duration;
var pButton1 = document.getElementById('pButton1');
var playhead1 = document.getElementById('playhead1');
var timeline1 = document.getElementById('timeline1');
var img1 = document.getElementById('img1')

// Second meditation
var music2 = document.getElementById('music2');
var duration2 = music2.duration;
var pButton2 = document.getElementById('pButton2');
var playhead2 = document.getElementById('playhead2');
var timeline2 = document.getElementById('timeline2');
var img2 = document.getElementById('img2')

// Third meditation
var music3 = document.getElementById('music3');
var duration3 = music3.duration;
var pButton3 = document.getElementById('pButton3');
var playhead3 = document.getElementById('playhead3');
var timeline3 = document.getElementById('timeline3');
var img3 = document.getElementById('img3')

// Play button event listenter
pButton1.addEventListener("click", play1);
pButton2.addEventListener("click", play2);
pButton3.addEventListener("click", play3);

//Play and Pause

function play1() {
  // Start track
  if (music1.paused) {
    music1.play();
    pButton1.innerHTML = "";
    pButton1.innerHTML = "pause";
    img1.classList.add('moving');
  } 
  // Pause track
  else {
    music1.pause();
    pButton1.innerHTML = "";
    pButton1.innerHTML = "play_arrow";
    img1.classList.remove('moving');
  }

}

function play2() {
  // Start track
  if (music2.paused) {
    music2.play();
    pButton2.innerHTML = "";
    pButton2.innerHTML = "pause";
    img2.classList.add('moving');
  } 
  // Pause track
  else {
    music2.pause();
    pButton2.innerHTML = "";
    pButton2.innerHTML = "play_arrow";
    img2.classList.remove('moving');
  }
}

function play3() {
  // Start track
  if (music3.paused) {
    music3.play();
    pButton3.innerHTML = "";
    pButton3.innerHTML = "pause";
    img3.classList.add('moving');
  } 
  // Pause track
  else {
    music3.pause();
    pButton3.innerHTML = "";
    pButton3.innerHTML = "play_arrow";
    img3.classList.remove('moving');
  }
}

// Time update event listener
music1.addEventListener("timeupdate", timeUpdate1, false);
music2.addEventListener("timeupdate", timeUpdate2, false);
music3.addEventListener("timeupdate", timeUpdate3, false);

// Calculate how far the playhead should be along the timeline
var timelineWidth1 = timeline1.offsetWidth - playhead1.offsetWidth;
var timelineWidth2 = timeline2.offsetWidth - playhead2.offsetWidth;
var timelineWidth3 = timeline3.offsetWidth - playhead3.offsetWidth;

// Synchronizes playhead position with current point in audio
function timeUpdate1() {
  var playPercent = timelineWidth1 * (music1.currentTime / duration1);
  playhead1.style.marginLeft = playPercent + "px";
  if (music1.currentTime == duration1) {
    pButton1.innerHTML = "";
    pButton1.innerHTML = "play_arrow";
  }
}

function timeUpdate2() {
  var playPercent = timelineWidth2 * (music1.currentTime / duration2);
  playhead2.style.marginLeft = playPercent + "px";
  if (music2.currentTime == duration2) {
    pButton2.innerHTML = "";
    pButton2.innerHTML = "play_arrow";
  }
}

function timeUpdate3() {
  var playPercent = timelineWidth3 * (music3.currentTime / duration3);
  playhead3.style.marginLeft = playPercent + "px";
  if (music3.currentTime == duration3) {
    pButton3.innerHTML = "";
    pButton3.innerHTML = "play_arrow";
  }
}

// Returns elements left position relative to top-left of viewport
function getPosition(el) {
  return el.getBoundingClientRect().left;
}