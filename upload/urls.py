from django.urls import path

from .views import index, upload_file, upload_files, update_file, delete_file

app_name = 'upload'
urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='file/', view=upload_file, name='file'),
    path(route='files/', view=upload_files, name='files'),
    path(route='file/<int:pk>/update/', view=update_file, name='update_file'),
    path(route='file/<int:pk>/delete/', view=delete_file, name='delete_file'),
]
