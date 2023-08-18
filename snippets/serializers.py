from rest_framework import serializers
from snippets.models import Snippet
from rest_framework.serializers import ModelSerializer


class SnippetSerializer(ModelSerializer):
     
     class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']