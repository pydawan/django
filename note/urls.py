from django.urls import path

from .views import NoteIndex, NoteCreate, NoteUpdate, NoteDelete

app_name = 'note'
urlpatterns = [
    path(route='', view=NoteIndex.as_view(), name='index'),
    path(route='new/', view=NoteCreate.as_view(), name='create'),
    path(route='<int:pk>/update/', view=NoteUpdate.as_view(), name='update'),
    path(route='<int:pk>/delete/', view=NoteDelete.as_view(), name='delete'),
]
