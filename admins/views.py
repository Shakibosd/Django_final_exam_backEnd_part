from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from admins.models import CustomUser
from flowers.models import Flower
from flowers.serializers import FlowerSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view

#admin deshboard btn view
class IsAdminView(APIView): 
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:  
            return Response({"is_admin": True})
        return Response({"is_admin": False})


# Post views
class PostListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Flower.objects.all()
        serializer = FlowerSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("inside flower post")
        serializer = FlowerSerializer(data=request.data)
        # print(serializer.data)
        if serializer.is_valid():
            print("serrilizer is valid")
            serializer.save(author=request.user)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            post = Flower.objects.get(pk=id)
        except Flower.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FlowerSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            post = Flower.objects.get(pk=id)
        except Flower.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user != post.author:
            return Response({"error": "You do not have permission to edit this post"}, status=status.HTTP_403_FORBIDDEN)

        serializer = FlowerSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            post = Flower.objects.get(pk=id)
        except Flower.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user != post.author:
            return Response({"error": "You do not have permission to delete this post"}, status=status.HTTP_403_FORBIDDEN)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#user list
class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.filter(is_staff=False)
        serializer = UserSerializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data)

#user details     
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if not request.user.is_superuser:
            return Response({"error": "Only admin can update user information"}, status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def disable_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_disabled = True
        user.save()
        return Response({'message': f'User {user.username} disabled successfully.'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def enable_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_disabled = False
        user.save()
        return Response({'message': f'User {user.username} enabled successfully.'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    

