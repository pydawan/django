function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function() {
  $('#btn_jquery_post').click(function() {
    var form_data = $('#form').serialize()
    var csrftoken = jQuery('[name=csrfmiddlewaretoken]').val();

    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
      }
    })

    $.ajax({
      type: 'post',
      async: true,
      url: '/jquery/post/',
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
