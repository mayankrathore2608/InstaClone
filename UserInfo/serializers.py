from rest_framework import serializers
from .models import UserCred


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCred
        fields = ['username','password','name','email']
