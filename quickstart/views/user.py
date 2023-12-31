from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet) :
    # api endpoint that allows users to be viewed and edited
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]