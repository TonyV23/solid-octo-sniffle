from rest_framework import serializers
from snippets.models import Snippet
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class SnippetSerializer(ModelSerializer):
     owner = serializers.ReadOnlyField(source='owner.username')
     class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlighted']

class UserSerializer(ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']