//' The watch id References the current 'watchHead'

var watchID = null;

// Wait for device API libraries t6o load
//
document.addEventListener("deviceready", onDeviceReady, false);

// device APIs are available
//
function onDeviceReady() {
  startWatch();
}

//Start watching the compass
//
function startWatch() {

//Update compass 60 times / second form smooth animation
var option = {
  frequency :16
};
