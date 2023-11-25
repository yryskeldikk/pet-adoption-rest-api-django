from django.forms import ValidationError
from rest_framework import serializers

from applications.models import Applications
from .models import Comment
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from accounts.models import Account


class CommentsSerializer(serializers.ModelSerializer):
    creation_time = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    target_comment = serializers.IntegerField(write_only=True, required=False)
    content_type = serializers.CharField()
    object_id = serializers.IntegerField()
    from_user_name = serializers.SerializerMethodField()


    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'content_object', 'from_user_name', 'message', 'rating', 'creation_time', 'target_comment']
        
    def create(self, validated_data):
        target_comment = validated_data.pop('target_comment', None)
        content_type = validated_data.pop('content_type', None)
        object_id = validated_data.pop('object_id', None)
            
        if content_type == None:
            raise serializers.ValidationError({"type": "This field is required."})
        if object_id == None:
            raise serializers.ValidationError({"id": "This field is required."})
            
        if content_type.lower() == 'user':
            content_type = ContentType.objects.get_for_model(Account)
            if Account.objects.filter(id=object_id).first() == None:
                raise serializers.ValidationError('Target Account can not be found')
            if Account.objects.get(id=object_id).isShelter == False:
                raise serializers.ValidationError("Target Account is not a Shelter")
        elif content_type.lower() == 'applications':
            content_type = ContentType.objects.get_for_model(Applications)
        else:
            raise serializers.ValidationError({"type": "Invalid type"})
            
        instance = Comment.objects.create(
            content_type = content_type,
            object_id = object_id,
            **validated_data
        )
            
        # If this is a follow up comment
        if target_comment is not None:
            target_comment_entry = get_object_or_404(Comment, id=target_comment)
            target_comment_entry.response = instance
            target_comment_entry.save()
                
        return instance
    
    def get_from_user_name(self, obj):
        return obj.from_user.username
    
    def to_representation(self, instance):  
        representation = super().to_representation(instance)
        representation.pop('content_object', None)
        return representation

    