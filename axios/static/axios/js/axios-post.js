function axios_post_data() {
  first_name = document.getElementById('id_first_name').value
  last_name = document.getElementById('id_last_name').value

  let form_data = new FormData()
  form_data.append('first_name', first_name)
  form_data.append('last_name', last_name)

  axios.defaults.xsrfCookieName = 'csrftoken'
  axios.defaults.xsrfHeaderName = 'X-CSRFToken'
  axios.post('/axios/post/',
      form_data,
    )
    .then(function(response) {
      var paragraph = document.getElementById('result')
      text = `Bem vindo ${response['data']['first_name']} ${response['data']['last_name']} (${response['data']['info']}).`
      paragraph.innerHTML = text
    })
    .catch(function(error) {
      console.log(error)
    })
}
