from rest_framework import serializers

from main.models import Project, Task
from main.serializers.user import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    tasks_count = serializers.SerializerMethodField()

    def create(self, validated_data):
        user = self.context["request"].user
        return Project.objects.create(owner=user, **validated_data)

    def get_tasks_count(self, obj):
        return Task.objects.filter(project=obj).count()

    class Meta:
        model = Project
        fields = ["id", "owner", "name", "tasks_count"]
