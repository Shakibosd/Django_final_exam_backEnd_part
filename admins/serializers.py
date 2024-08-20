from rest_framework import serializers
from .models import CustomUser

#user serrializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_disabled']
