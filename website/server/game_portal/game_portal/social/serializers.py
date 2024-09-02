from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Friend, Group, GroupMembership
from ..accounts.serializers import UserSerializer

User = get_user_model()

class FriendSerializer(serializers.ModelSerializer):
    friend_id = serializers.SerializerMethodField()
    friend_name = serializers.SerializerMethodField()

    class Meta:
        model = Friend
        fields = ['friend_id', 'friend_name']

    def get_friend_id(self, obj):
        return obj.friend.id

    def get_friend_name(self, obj):
        return obj.friend.username

class GroupMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = GroupMembership
        fields = ['user', 'is_admin']

class GroupSerializer(serializers.ModelSerializer):
    members = GroupMembershipSerializer(source='groupmembership_set', many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'members']
