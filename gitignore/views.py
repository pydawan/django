from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets, generics, filters
from rest_framework import permissions
from .serializers import GitignoreSerializer
from .models import Gitignore

def index(request):
    return HttpResponse('okkkkk')


class GitignoreList(generics.ListCreateAPIView):
    search_fields = ['tag']
    filter_backends = (filters.SearchFilter,)
    queryset = Gitignore.objects.all()
    serializer_class = GitignoreSerializer

class GitignoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Gitignore.objects.all()
    serializer_class = GitignoreSerializer
    # permission_classes = [permissions.IsAuthenticated]

