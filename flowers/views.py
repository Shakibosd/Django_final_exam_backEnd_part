#https://docs.google.com/spreadsheets/d/1edlnD8h-s5itNyxCbNrd8s_munC-nMslM_H0IL-QWcs/edit?gid=0#gid=0
from rest_framework import viewsets
from flowers.permissions import HasOrdered
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
from flowers.serializers import CheckOrder
from rest_framework.permissions import IsAuthenticated
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes

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
        
# class CommentAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             flowerId = serializer.validated_data['flowerId']
#             flower = get_object_or_404(Flower, id=flowerId)
#             user = request.user

#             if not Order.objects.filter(user=user, flower=flower).exists():
#                 return Response({"message": "You need to purchase the flower to comment."}, status=status.HTTP_403_FORBIDDEN)

#             names = serializer.validated_data['names']
#             body = serializer.validated_data['comment']
#             comment = Comment.objects.create(flower=flower, name=names, body=body)
#             comment.save()

#             return Response({"message": "Comment created"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.permissions import IsAuthenticated
from .permissions import HasOrdered

class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated, HasOrdered]

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            flowerId = serializer.validated_data['flowerId']
            flower = get_object_or_404(Flower, id=flowerId)

            names = serializer.validated_data['names']
            body = serializer.validated_data['comment']
            comment = Comment.objects.create(flower=flower, name=names, body=body)
            comment.save()

            return Response({"message": "Comment created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CheckOrderView(APIView):
#     # permission_classes = [IsAuthenticated]    

#     def post(self, request):
#         flowerId = request.data.get('flowerId')
        
#         if flowerId:
#             try:
#                 flower = Flower.objects.get(id=flowerId)
#                 order_exists = Order.objects.filter(flower=flower).exists()
#                 return Response({'order_exists': order_exists}, status=status.HTTP_200_OK)
#             except Flower.DoesNotExist:
#                 return Response({'error': 'Flower not found'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

class CheckOrderView(APIView):
    permission_classes = [IsAuthenticated, HasOrdered]
    def post(self, request, *args, **kwargs):
        flowerId = request.data.get('flowerId')
        flower = get_object_or_404(Flower, id=flowerId)
        user = request.user

        if Order.objects.filter(user=user, flower=flower).exists():
            return Response({"order_exists": True}, status=status.HTTP_200_OK)
        return Response({"order_exists": False}, status=status.HTTP_403_FORBIDDEN)
        

@api_view(['GET'])
def admin_dashboard(request):
    if request.user.is_staff:
        return Response({"message": "Welcome to the admin dashboard!"}, status=200)
    else:
        return Response({"message": "Access denied: You are not an admin."}, status=403)