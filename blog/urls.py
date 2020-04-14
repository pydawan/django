from django.urls import path

from .views import index, post_detail, post_new, post_edit, post_delete, post_drafts

app_name = 'blog'
urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='post/drafts/', view=post_drafts, name='post_drafts'),
    path(route='post/<int:pk>/', view=post_detail, name='post_detail'),
    path(route='post/new/', view=post_new, name='post_new'),
    path(route='post/<int:pk>/edit/', view=post_edit, name='post_edit'),
    path(route='post/<int:pk>/delete/', view=post_delete, name='post_delete'),
]
