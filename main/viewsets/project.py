from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.models import Project, Task
from main.serializers.project import ProjectSerializer


class ProjectPermissionClass(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        if request.method == "DELETE":
            return Task.objects.filter(project=obj).count() == 0

        return obj.owner == user


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermissionClass]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(owner=user)
