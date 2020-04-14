choice_text = ["'{% for choice in question.choice_set.all %}{{ choice.choice_text }},{% endfor %}'"]
choice_votes = ["'{% for choice in question.choice_set.all %}{{ choice.votes }},{% endfor %}'"]
background_color = []
border_color = []
for (var prop in choice_text) {
    var r = Math.floor(Math.random() * 256)
    var g = Math.floor(Math.random() * 256)
    var b = Math.floor(Math.random() * 256)
    let rgb = `rgba(${r}, ${g}, ${b})`
    let rgba = `rgba(${r}, ${g}, ${b}, 0.2)`
    background_color.push(rgba)
    border_color.push(rgb)
}
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: choice_text,
        datasets: [{
            label: 'N° de votos',
            data: choice_votes,
            backgroundColor: background_color,
            borderColor: border_color,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});