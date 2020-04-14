function jsfetch_get_data() {
    let first_name = document.getElementById('id_first_name').value
    let last_name = document.getElementById('id_last_name').value

    URL = `/jsfetch/get/?first_name=${first_name}&last_name=${last_name}`
    fetch(URL, {
        method: 'get',
        headers: new Headers(),
        credentials: 'include',
        redirect: 'follow',
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
            let paragraph = document.getElementById(elementId = 'result')
            text = `Bem vindo ${data['first_name']} ${data['last_name']} (${data['info']})`
            paragraph.innerHTML = text
        }).catch(function (err) {
            console.log(err)
        })
}
