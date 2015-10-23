$(document).ready(function(){
  console.log('this is being loaded');

  // ===== GLOBAL ===== //
  $(".hover-remove").mouseover(function(){
    $(this).addClass("hide");
    Materialize.toast('Gotcha!! :D', 5000);
  });
});
