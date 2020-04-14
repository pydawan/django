from django.urls import path

from .views import index

app_name = 'leafletjs'
urlpatterns = [
    path(route='', view=index, name='index'),
]
