# from django.urls import path
# from .views import PostAPIView, PostDetailAPIView, UserAPIView, UserDetailAPIView

# urlpatterns = [
#     path('posts/', PostAPIView.as_view(), name='post-list'),
#     path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
#     path('users/', UserAPIView.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
# ]

from django.urls import path
from .views import IsAdminView

urlpatterns = [
    path('is_admin/', IsAdminView.as_view(), name='is_admin'),
]
