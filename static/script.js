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
$("#egg").click(function() {
  document.getElementById("loginFormWrapper").style.display = "block";
});
$("#info").click(function() {
  document.getElementById("loginFormWrapper").style.display = "block";
});
function close_overlay() {
  document.getElementById("overlay").style.display = "none";
  window.location.href = '/templates/signup.html'; //relative to domain
  return false;
}
$(document).ready(function() {
  $("#flat-egg")
    .on("click", function() {
      var seconds = new Date().getTime() / 1000;
      var username = getCookie("username")
      $(this).addClass("rotate");
      $.post( "/postmethod", {
      javascript_data: [username, seconds]
        
});
       
  })
    .on("animationend", function() {
      $(this).removeClass("rotate");
      document.getElementById("match-text-curve").style.display = "block";
    });
});
