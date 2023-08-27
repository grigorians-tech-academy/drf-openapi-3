from rest_framework import serializers

from main.models import LogItem


class LogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogItem
        fields = "__all__"
