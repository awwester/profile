$(document).ready(function(){
  // ===== GLOBAL ===== //
  $(".hover-remove").mouseover(function(){
    $(this).addClass("hide");
    Materialize.toast('Gotcha!! :D', 5000);
  });
});
