# views.py
from rest_framework import viewsets

from orders.models import Order
from .serializers import FlowerSerializer, CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Flower, Comment
from rest_framework import generics
from flowers.serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied

class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

class FlowerDetail(APIView):
    def get_object(self, pk):
        try:
            return Flower.objects.get(pk=pk)
        except Flower.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flower = self.get_object(pk)
        serializer = FlowerSerializer(flower)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        flower = self.get_object(pk)
        serializer = FlowerSerializer(flower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        flower = self.get_object(pk)
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

class CommentShowAPIView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    def get_queryset(self):
        postId = self.kwargs["postId"]
        flower = Flower.objects.get(id = postId)
        return Comment.objects.filter(flower = flower)
        
class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            flowerId = serializer.validated_data['flowerId']
            flower = get_object_or_404(Flower, id=flowerId)
            user = request.user

            # Check if the user has purchased this flower
            has_purchased = Order.objects.filter(user=user, flower=flower).exists()
            if not has_purchased:
                raise PermissionDenied("You cannot comment on this flower because you have not purchased it.")

            names = serializer.validated_data['names']
            body = serializer.validated_data['comment']

            # Save the comment
            comment = Comment.objects.create(flower=flower, name=names, body=body, user=user)
            comment.save()

            return Response({"message": "Comment created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
