window.addEventListener(
    "scroll",
    () => {
      document.body.style.setProperty(
        "--scroll",
        window.pageYOffset / (document.body.offsetHeight - window.innerHeight)
      );
    },
    false
  );

function myFunction() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("show") == -1) {
    x.className += " show";
  } else { 
    x.className = x.className.replace(" show", "");
  }
}

$(function(){
    $("#nav-placeholder2").load("../NavBar2.html");
  });

$(function(){
  $("#nav-placeholder").load("NavBar.html");
});

$(function(){
  $("#footer-placeholder").load("FootBar.html");
});
$(function(){
  $("#footer-placeholder2").load("../FootBar.html");
});