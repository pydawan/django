from django.urls import path

from .views import jquery_get, jquery_post, index

app_name = 'jquery'
urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='get/', view=jquery_get, name='get'),
    path(route='post/', view=jquery_post, name='post'),
]
