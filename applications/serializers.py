from .models import Applications
from rest_framework import serializers
from .models import Account
from listings.models import Pet

class ApplicationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    creation_time = serializers.DateTimeField(read_only = True)
    last_update_time = serializers.DateTimeField(read_only = True)
    applicant = serializers.PrimaryKeyRelatedField(read_only = True)
    pet =  serializers.PrimaryKeyRelatedField(read_only = True)

    class Meta:
        model = Applications
        fields = ['id','creation_time', 'last_update_time','applicant','status','pet']

class CreateApplicationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True) 
    creation_time = serializers.DateTimeField(read_only = True)
    last_update_time = serializers.DateTimeField(read_only = True)
    applicant = serializers.PrimaryKeyRelatedField(read_only = True)
    status = serializers.CharField(read_only = True)
    
    class Meta:
        model = Applications
        fields = ['id','creation_time', 'last_update_time','applicant','status','pet']