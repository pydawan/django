from django.urls import path

from .views import js_xmlhttprequest_get, js_xmlhttprequest_post, index

app_name = 'jsxmlhttprequest'
urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='get/', view=js_xmlhttprequest_get, name='get'),
    path(route='post/', view=js_xmlhttprequest_post, name='post'),
]
