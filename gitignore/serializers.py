from rest_framework import serializers

from .models import Gitignore


class GitignoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gitignore
        fields = ['content']
