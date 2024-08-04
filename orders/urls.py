from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderView, OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create_order/', OrderView.as_view(), name='create_order')
]
