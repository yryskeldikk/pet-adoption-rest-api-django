from rest_framework import serializers
from .models import Notifications

class NotificationSerializer(serializers.ModelSerializer):
    creation_time = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Notifications
        fields = ['id', 'message', 'owner', 'read', 'creation_time', 'type', 'action_link']
        