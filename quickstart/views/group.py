from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    # api endpoint that allows group to be viewed and edited
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]