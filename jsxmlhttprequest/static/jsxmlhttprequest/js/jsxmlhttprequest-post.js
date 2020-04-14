// Função para obter o valor do csrftoken:
function get_cookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function jsxmlhttprequest_post_data() {
  let form_data = new FormData(document.getElementById('form'))
  var csrftoken = get_cookie('csrftoken')

  var ajax = new XMLHttpRequest()
  ajax.open('POST', '/jsxmlhttprequest/post/', true)
  ajax.setRequestHeader('X-CSRFToken', csrftoken)
  ajax.send(form_data);
  ajax.onreadystatechange = function() {
    // Caso o state seja 4 e o http.status for 200. Requisição OK.
    if (ajax.readyState == 4 && ajax.status == 200) {
      let paragraph = document.getElementById(elementId = 'result')
      let response = JSON.parse(ajax.responseText)
      text = `Bem vindo ${response['first_name']} ${response['last_name']} (${response['info']})`
      paragraph.innerHTML = text
    }
  }
}
