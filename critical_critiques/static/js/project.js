/* Project specific Javascript goes here. */
$(function() {

  $('#done-form').submit(function(e){
    e.preventDefault();
    $.ajax({
      type: $(this).attr('method'),
      url: $(this).attr('action'),
      data: $(this).serialize(),
      success: function (data) {
        $('.slide-content').fadeOut(function() {
          $('.done').fadeIn();
        })
      }
    });
  })

})