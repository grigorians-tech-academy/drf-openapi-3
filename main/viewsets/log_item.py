from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
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

    @extend_schema(
        description="Clean all log items",
        responses={
            204: None,
            400: {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Error message",
                    },
                },
            },
        },
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "confirm": {
                        "type": "boolean",
                        "description": "Confirm to clean all log items",
                    },
                },
            }
        },
    )
    @action(detail=False, methods=["POST"])
    @parser_classes([FormParser, MultiPartParser])
    def clean(self, request):
        confirm = request.data.get("confirm", None)
        if not confirm or confirm != "true":
            return Response(
                {"message": "Confirm is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        LogItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        description="Get latest log items",
        responses={
            200: LogItemSerializer(many=True),
            400: "Bad request",
            404: "No log items found",
        },
        parameters=[
            OpenApiParameter(
                name="count",
                description="Number of log items to return",
                required=True,
                type=int,
            )
        ],
    )
    @action(detail=False, methods=["GET"])
    def latest(self, request):
        count = request.query_params.get("count", None)
        if count is None:
            return Response(
                {"nesage": "Count is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        logs = LogItem.objects.all().order_by("-created_at")[
            : int(count)
        ]
        if not logs:
            return Response(
                {"message": "No log items found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = LogItemSerializer(logs, many=True)
        return Response(serializer.data)
