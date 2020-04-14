from django.urls import path

from .views import js_fetch_get, js_fetch_post, index

app_name = 'jsfetch'
urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='get/', view=js_fetch_get, name='get'),
    path(route='post/', view=js_fetch_post, name='post'),
]
