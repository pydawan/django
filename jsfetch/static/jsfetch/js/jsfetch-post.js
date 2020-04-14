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

function jsfetch_post_data() {
  let form_data = new FormData(document.getElementById('form'))
  var csrftoken = get_cookie('csrftoken')
  URL = '/jsfetch/post/'
  fetch(URL, {
      method: 'post',
      headers: new Headers({
        'X-CSRF-TOKEN': csrftoken,
      }),
      credentials: 'include',
      redirect: 'follow',
      body: form_data,
    })
    .then(function(response) {
      return response.json()
    })
    .then(function(data) {
      let paragraph = document.getElementById(elementId = 'result')
      text = `Bem vindo ${data['first_name']} ${data['last_name']} (${data['info']})`
      paragraph.innerHTML = text
    }).catch(function(err) {
      console.log(err)
    })
}
