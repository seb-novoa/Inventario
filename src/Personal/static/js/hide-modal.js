$("#myModal").keypress(function(e){
  if(e.which == 13){
    if((" .error")== ''){
      $("#myModal .close").click();
    }
  }
});
