from django.urls import path, include
from rest_framework import routers

from .views import GitignoreViewSet, GitignoreList, index

router = routers.DefaultRouter()
router.register(r'', GitignoreViewSet)
# router.register(r'tag', GitignoreList, basename='MyModel')

app_name = 'gitignore'
urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/teste/', GitignoreList.as_view(), name='teste'),
    # path('api/tag/<int:pk>/', GitignoreList.as_view()),
    path(route='', view=index, name='index'),
]
