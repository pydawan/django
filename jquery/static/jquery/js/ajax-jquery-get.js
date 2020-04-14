$(document).ready(function() {
  $('#btn_jquery_get').click(function() {
    var form_data = $('#form').serialize()

    $.ajax({
      type: 'get',
      async: true,
      url: '/jquery/get/',
      data: form_data,
      success: function(response) {
        text = `Bem vindo ${response['first_name']} ${response['last_name']} (${response['info']})`
        $('#result').text(text)
      },
      error: function(error) {
        console.log('Status: ' + error.status + '\nErro: ' + error.statusText)
      }
    })
  })
})
