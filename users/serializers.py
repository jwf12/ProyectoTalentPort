from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from .models import User, FriendList

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        extra_kwargs = {'password': {'write_only': True}}


class FriendListSerializer(ModelSerializer):
    friendlist_username = serializers.ReadOnlyField(source='friendlist.username')

    class Meta:
        model = FriendList
        fields = ['friendlist_username']