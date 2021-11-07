$(document).ready(function() {
  $(window).keydown(function(event) {
    if (event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
  });
});
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
function checkNames() {
  // Find the validation image div
  var validationElement = $("#pass-error");
  // Get the form values
  var match = ($("#password").val() == $("#password-confirm").val());
  document.getElementById("pass-error").style.opacity = "0";
  if (match) {
    document.getElementById("pass-error").style.opacity = "0";
  } else {
    document.getElementById("pass-error").style.opacity = "1";
  }
}
var contPage = 0
function formProgress() {
  if(contPage == 0){
    document.cookie = "username=" +$("#user").val();
    document.cookie = "pass=" +$("#password").val();
    document.getElementById("pass-error").style.display = "none";
    document.getElementById("user").style.display = "none";
    document.getElementById("password").style.display = "none";
    document.getElementById("password-confirm").style.display = "none";
    contPage++;
    document.getElementById("name").style.display = "inline";
    document.getElementById("age").style.display = "inline";
    document.getElementById("bio").style.display = "inline";
    document.getElementById("finalSubmit").style.display = "inline";
    document.getElementById("continue-button").style.display = "none";
  }
  else if(contPage==1){
    window.location.href = 'profile'; //relative to domain
  }
}