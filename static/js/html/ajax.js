var id_score = document.getElementById('id_score');
  function scoresubmit(){
  $.ajax({
    url: '/',
    method : 'POST',
    data: {score: $('#score').val(), "csrfmiddlewaretoken" : "{{csrf_token}}"},
    success: function() {

      $('#id_score').HTML(score);
      console.log(score);
    }
     });

    }