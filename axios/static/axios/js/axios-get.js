function axios_get_data() {
  first_name = document.getElementById('id_first_name').value;
  last_name = document.getElementById('id_last_name').value;

  axios.get('/axios/get/', {
    params: {
      first_name: first_name,
      last_name: last_name
    }
  })
    .then(function (response) {
      let paragraph = document.getElementById((elementId = 'result'));
      text = `Bem vindo ${response['data']['first_name']} ${response['data']['last_name']} (${response['data']['info']})`;
      paragraph.innerHTML = text;
    })
    .catch(function (error) {
      console.log(error);
    });
}