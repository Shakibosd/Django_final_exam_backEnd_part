from django.urls import path
from .views import PostListView, PostDetailView
from django.urls import path
from .views import UserListView, UserDetailView
from django.urls import path
from .views import IsAdminView

urlpatterns = [
    #post view url
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('post_detail/<int:id>/', PostDetailView.as_view(), name='post_detail'),
    #admin deshboard btn url
    path('is_admin/', IsAdminView.as_view(), name='is_admin'),
    #user view url
    path('user_list/', UserListView.as_view(), name='user_list'), 
    path('user_detail/<int:id>/', UserDetailView.as_view(), name='user_detail'), 
]