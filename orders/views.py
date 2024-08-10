from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Order
from flowers.models import Flower
from .serializers import OrderSerializer, OrderCreateSerializer, OrderSerializerForCreate
from .constants import PENDING, COMPLETED
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().select_related('user', 'flower')

#     def get_serializer_class(self):
#         if self.action == 'create':
#             return OrderCreateSerializer
#         return OrderSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    
#     @action(detail=False, methods=['get'])
#     def my_orders(self, request):
#         orders = Order.objects.filter(user=request.user)
#         serializer = self.get_serializer(orders, many=True)
#         return Response(serializer.data)

class OrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
       
        orders = Order.objects.filter(user=request.user)
        
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializerForCreate(data=request.data)
        if serializer.is_valid():
            print(serializer)
            user_id = serializer.validated_data['user_id']
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            user = get_object_or_404(User, id=user_id)
            flower = get_object_or_404(Flower, id=product_id)
            order = Order.objects.create(
                user=user,
                flower=flower,
                quantity=quantity,
                status='Pending',  
            )
            flower.stock -= quantity
            flower.save()

            email_subject = 'Order Confirmation'
            email_body = render_to_string('order_confirmation_email.html', {
                'user': user,
                'flower': flower,
                'quantity': quantity,
                'order': order,
            })
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()

            
            return Response({
                'status': 'order placed successfully'
            }, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors) 

        return Response({
            'error': 'order not created',
            'details': serializer.errors 
        }, status=status.HTTP_400_BAD_REQUEST)

