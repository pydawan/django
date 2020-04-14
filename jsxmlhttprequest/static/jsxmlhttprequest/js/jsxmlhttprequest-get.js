function jsxmlhttprequest_get_data() {
    let first_name = document.getElementById('id_first_name').value
    let last_name = document.getElementById('id_last_name').value

    URL = `/jsxmlhttprequest/get/?first_name=${first_name}&last_name=${last_name}`
    var ajax = new XMLHttpRequest()
    ajax.open('get', URL, true)
    ajax.send()
    ajax.onreadystatechange = function () {
        // Caso o state seja 4 e o http.status for 200. Requisição OK.
        if (ajax.readyState == 4 && ajax.status == 200) {
            let paragraph = document.getElementById(elementId = 'result')
            let response = JSON.parse(ajax.responseText)
            text = `Bem vindo ${response['first_name']} ${response['last_name']} (${response['info']})`
            paragraph.innerHTML = text
        }
    }
}
