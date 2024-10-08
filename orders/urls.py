from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderView, OrderAPIView

router = DefaultRouter()

urlpatterns = [
    path('create_order/', OrderView.as_view(), name='create_order'),
    path('my_orders/', OrderAPIView.as_view(), name='my-orders'),
]
