from django.urls import path
from .views import (RegisterApiView, LoginApiView, EditUserApiView,
                     UserGetViewAPIView, LogoutApiView, FriendAdd, FriendListView,
                     DeleteFriendView, UserSearcherView, OpenWorkView)

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('edituser/', EditUserApiView.as_view(), name='edituser'),
    path('user/',UserGetViewAPIView.as_view(), name='userget'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('search/<str:search_term>/', UserSearcherView.as_view(), name='searcher'),
    path('work/', OpenWorkView.as_view(), name='open_work'),



    #Friends
    path('addfriend/', FriendAdd.as_view(), name='friend_add'),
    path('listfriend/', FriendListView.as_view(), name='friend_list'),
    path('deletefriend/<int:pk>/', DeleteFriendView.as_view(), name='friend_delete'),


]
