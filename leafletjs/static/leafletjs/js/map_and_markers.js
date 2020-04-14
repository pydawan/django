function create_offline_map(pos) {
  // Dados do backend.
  var data = JSON.parse(document.getElementById('data').textContent);
  // setView([latitude, longitude], zoom)
  var _map = L.map('map').setView([-22.8826734, -48.4485717], 13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> ' +
      'contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
  }).addTo(_map);

  for (var i = 0; i < data.length; i++) {
    var popup = `<b>Nome</b>: ${data[i]['name']}<br><b>Posição</b>: ${data[i]['lat']}, ${data[i]['lng']}`
    L.marker([data[i]['lat'], data[i]['lng']])
      .addTo(_map)
      .bindPopup(popup)
  }
}

function create_map(pos) {
  var latitude = pos.coords.latitude
  var longitude = pos.coords.longitude
  // setView([latitude, longitude], zoom)
  var _map = L.map('map').setView([latitude, longitude], 13);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> ' +
      'contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
  }).addTo(_map);

  var today = new Date();
  var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate()
  var time = today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds()
  var dateTime = date + ' -- ' + time;
  var popup = '<b>Sua localização</b><br>' +
    `<b>Posição</b>: ${latitude.toFixed(2)}, ${longitude.toFixed(2)}<br>` +
    `<b>Data</b>: ${dateTime}`

  L.marker([latitude, longitude])
    .addTo(_map)
    .bindPopup(popup)
}

function error(err) {
  if (error.code == error.PERMISSION_DENIED) {
    alert('Você optou por não permitir o compartilhamento da posição.\n' +
      'Exibindo dados offline (dados do backend).');
    create_offline_map()
  }
  console.warn(`ERROR(${err.code}): ${err.message}`)
}

var options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
}

function getLocation() {
  if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(create_map, error, options);
  } else {
    alert('O seu navegador não tem suporte a GeoLocalização.' +
      'Exibindo dados offline (dados do backend).');
    create_offline_map()
  }
}

document.onload = getLocation()
