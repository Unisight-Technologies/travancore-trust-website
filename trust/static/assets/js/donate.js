

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
  }
  else{
    document.getElementById("money2").style.display = "none";
  }

  // TODO: Validate if ----Select---- is selected
}
