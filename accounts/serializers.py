from .models import Account
from rest_framework import serializers

class CreateAccountSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    isShelter =  serializers.BooleanField(default = False)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Account
        fields = ["id","username","email", "first_name", "last_name",'password1','password2','isShelter','location','phone_number']


class AccountSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    isShelter = serializers.BooleanField(read_only=True)
    class Meta:
        model = Account
        fields = ["id", "username", "email", "first_name", 'last_name','location','phone_number','isShelter', 'avatar']
        
