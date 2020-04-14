from django.shortcuts import render


def index(request):
    data = [
        {
            'name': 'Posição offline 1',
            'lat': -22.8826734,
            'lng': -48.4485717,
        },
        {
            'name': 'Posição offline 2',
            'lat': -22.8845665,
            'lng': -48.4478615,
        },
    ]
    return render(
        request=request,
        template_name='leafletjs/index.html',
        context={'data': data},
    )
