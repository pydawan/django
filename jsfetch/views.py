from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST


def index(request):
    return render(
        request=request,
        template_name='jsfetch/index.html',
    )


@require_GET
def js_fetch_get(request):
    first_name = request.GET.get('first_name', None)
    last_name = request.GET.get('last_name', None)
    return JsonResponse(
        data={
            'first_name': first_name,
            'last_name': last_name,
            'info': 'Os dados foram obtidos via JS fetch GET',
        },
        status=200,
    )


@require_POST
def js_fetch_post(request):
    first_name = request.POST.get('first_name', None)
    last_name = request.POST.get('last_name', None)
    return JsonResponse(
        data={
            'first_name': first_name,
            'last_name': last_name,
            'info': 'Os dados foram obtidos via JS fetch POST',
        },
        status=200,
    )
