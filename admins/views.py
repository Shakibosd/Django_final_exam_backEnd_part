from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class IsAdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:  
            return Response({"is_admin": True})
        return Response({"is_admin": False})

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAdminUser
# from .models import Post, CustomUser
# from .serializers import PostSerializer, UserSerializer

# class UserAPIView(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, request, *args, **kwargs):
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserDetailAPIView(APIView):
#     permission_classes = [IsAdminUser]

#     def get_object(self, pk):
#         try:
#             return CustomUser.objects.get(pk=pk)
#         except CustomUser.DoesNotExist:
#             return None

#     def get(self, request, pk, *args, **kwargs):
#         user = self.get_object(pk)
#         if not user:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def patch(self, request, pk, *args, **kwargs):
#         user = self.get_object(pk)
#         if not user:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, *args, **kwargs):
#         user = self.get_object(pk)
#         if not user:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class PostAPIView(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostDetailAPIView(APIView):
#     permission_classes = [IsAdminUser]

#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return None

#     def get(self, request, pk, *args, **kwargs):
#         post = self.get_object(pk)
#         if not post:
#             return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def patch(self, request, pk, *args, **kwargs):
#         post = self.get_object(pk)
#         if not post:
#             return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, *args, **kwargs):
#         post = self.get_object(pk)
#         if not post:
#             return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

