from django.urls import path
from .views import (RegisterApiView, LoginApiView, EditUserApiView,
                     UserGetViewAPIView, LogoutApiView, FriendAdd, FriendListView)

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('edituser/', EditUserApiView.as_view(), name='edituser'),
    path('user/',UserGetViewAPIView.as_view(), name='userget'),
    path('logout/', LogoutApiView.as_view(), name='logout'),

    #Friends
    path('addfriend/', FriendAdd.as_view(), name='friend_add'),
    path('listfriend/', FriendListView.as_view(), name='friend_list'),


]
