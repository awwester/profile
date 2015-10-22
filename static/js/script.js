$(document).ready(function(){
  console.log('this is being loaded');

  // ===== GLOBAL ===== //
  $(".hover-remove").mouseover(function(){
    $(this).addClass("hide");

    console.log('triggering..');
    Materialize.toast('Gotcha!! :D', 4000); // 4000 is the duration of the toast
  });
});
