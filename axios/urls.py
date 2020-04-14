from django.urls import path

from .views import axios_get, axios_post, index

app_name = 'axios'
urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='get/', view=axios_get, name='get'),
    path(route='post/', view=axios_post, name='post'),
]
