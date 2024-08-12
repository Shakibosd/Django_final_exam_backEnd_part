from rest_framework import permissions
from .models import Flower
from orders.models import Order

class HasOrdered(permissions.BasePermission):
  
    def has_permission(self, request, view):
        flower_id = request.data.get('flowerId')
        if not flower_id:
            return False

        try:
            flower = Flower.objects.get(id=flower_id)
            # order = Order.objects.filter(flower = flower, user = request.user)

        except flower.DoesNotExist:
            return False
        return Order.objects.filter(user=request.user, flower=flower).exists()