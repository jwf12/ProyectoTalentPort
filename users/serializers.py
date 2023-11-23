from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from .models import User, FriendList

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('last_login', 'is_superuser', 'first_name',
                   'email', 'is_staff', 'date_joined', 'is_active',
                    'groups', 'user_permissions')
        
        extra_kwargs = {'password': {'write_only': True}}


class FriendListSerializer(ModelSerializer):
    userlist_username = serializers.ReadOnlyField(source='userlist.username')
    friendlist_username = serializers.ReadOnlyField(source='friendlist.username')

    class Meta:
        model = FriendList
        fields = ['id', 'userlist', 'friendlist', 'userlist_username', 'friendlist_username']
        