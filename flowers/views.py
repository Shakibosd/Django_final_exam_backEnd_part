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
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            flowerId = serializer.validated_data['flowerId']   
            names = serializer.validated_data['names']   
            comment = serializer.validated_data['comment']   
            flower = get_object_or_404(Flower, id=flowerId)
            Comment.objects.create(
                flower=flower,
                name=names,
                body=comment,
            )
            return Response({"comment created"}, status=status.HTTP_201_CREATED)
        return Response({"comment not created"}, status=status.HTTP_400_BAD_REQUEST)


class CheckPurchaseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, flowerId):
        user = request.user
        try:
            flower = Flower.objects.get(id=flowerId)

            has_purchased = Order.objects.filter(user=user, flower=flower).exists()

            return Response({'hasPurchased': has_purchased}, status=status.HTTP_200_OK)

        except Flower.DoesNotExist:
            return Response({'error': 'Flower not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)