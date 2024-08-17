from rest_framework import serializers
from .models import Post
from .models import CustomUser

#post serializer
class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'price', 'image', 'category', 'stock', 'author_name']


#user serrializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_disabled']

