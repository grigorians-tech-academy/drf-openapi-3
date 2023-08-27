from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import LogItem
from main.serializers.log_item import LogItemSerializer


class LogItemPermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        if user.is_superuser and request.method == "GET":
            return True

        if user.is_superuser and view.action == "clean":
            return True

        return False


class LogItemViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = LogItem.objects.all()
    serializer_class = LogItemSerializer
    permission_classes = [LogItemPermissionClass]

    @action(detail=False, methods=["POST"])
    def clean(self, request):
        LogItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["GET"])
    def hello(self, request):
        return Response({"message": "Hello, world!"})
