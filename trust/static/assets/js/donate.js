

function onSelectType(){
  var type = document.getElementById("type1").selectedIndex;
  if (type == 1){
    document.getElementById("money").style.display = "inherit";
  }
  else{
    document.getElementById("money").style.display = "none";
  }

  // TODO: Validate if ----Select---- is selected
}


function onSelectType2(){
  var type = document.getElementById("type2").selectedIndex;
  if (type == 1){
    document.getElementById("money2").style.display = "inherit";
    document.getElementById("email1").style.display = "inherit";

  }
  else{
    document.getElementById("money2").style.display = "none";
    document.getElementById("email1").style.display = "none";

  }

  // TODO: Validate if ----Select---- is selected
}

// When the user clicks on div, open the popup
function showPopup() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}
