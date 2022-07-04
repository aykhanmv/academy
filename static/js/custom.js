const targetDiv = document.getElementById("consroom");
const btn = document.getElementById("consbtn");
btn.onclick = function () {
  if (targetDiv.style.display !== "none") {
    targetDiv.style.display = "none";
  } else {
    targetDiv.style.display = "block";
  }
};

const targetDiv1 = document.getElementById("stdroom");
const btn1 = document.getElementById("stdbtn");
btn1.onclick = function () {
  if (targetDiv1.style.display !== "none") {
    targetDiv1.style.display = "none";
  } else {
    targetDiv1.style.display = "block";
  }
};

const targetDiv2 = document.getElementById("gnrlroom");
const btn2 = document.getElementById("gnrlbtn");
btn2.onclick = function () {
  if (targetDiv2.style.display !== "none") {
    targetDiv2.style.display = "none";
  } else {
    targetDiv2.style.display = "block";
  }
};

const targetDiv3 = document.getElementById("smnrroom");
const btn3 = document.getElementById("smnrbtn");
btn3.onclick = function () {
  if (targetDiv3.style.display !== "none") {
    targetDiv3.style.display = "none";
  } else {
    targetDiv3.style.display = "block";
  }
};

$(document).ready(function(){
  $(".dropdown").click(function(){
      $(this).find(".dropdown-menu").slideToggle("fast");
  });
});
$(document).on("click", function(event){
  var $trigger = $(".dropdown");
  if($trigger !== event.target && !$trigger.has(event.target).length){
      $(".dropdown-menu").slideUp("fast");
  }            
});

