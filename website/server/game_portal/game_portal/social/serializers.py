from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Friend

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
