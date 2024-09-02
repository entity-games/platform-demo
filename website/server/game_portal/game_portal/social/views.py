import os

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from livekit import api

from .serializers import FriendSerializer, GroupSerializer, GroupMembershipSerializer
from .models import Friend, Group, GroupMembership

User = get_user_model()
LIVEKIT_API_KEY = os.getenv('LIVEKIT_API_KEY')
LIVEKIT_API_SECRET = os.getenv('LIVEKIT_API_SECRET')

@api_view(['POST']) 
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_friend(request, user_id):
    user = request.user
    friend = get_object_or_404(User, id=user_id)
    Friend.objects.add_friend(user, friend)
    return Response(200) 

@api_view(['POST']) 
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def remove_friend(request, user_id):
    user = request.user
    friend = get_object_or_404(User, id=user_id)
    Friend.objects.remove_friend(user, friend)
    return Response(200)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_group(request, group_name):
    group = Group.objects.create(name=group_name, description="")
    GroupMembership.objects.create(user=request.user, group=group, is_admin=True)
    return Response(201)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_room_token(request, group_id):
    user = request.user
    group = Group.objects.get(group_id)
    
    if group is None:
        return Response("Group not found.", status=400)
    
    if user.id not in group.members:
        return Response("You do not belong to this group.", status=401)
    
    token = api.AccessToken(LIVEKIT_API_KEY, LIVEKIT_API_SECRET) \
        .with_identity("identity") \
        .with_name(user.id) \
        .with_grants(api.VideoGrants(
            room_join=True,
            room=group.name,
        ))
    return token.to_jwt()


class FriendListView(generics.ListAPIView):
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Friend.objects.filter(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class GroupMembershipViewSet(viewsets.ModelViewSet):
    queryset = GroupMembership.objects.all()
    serializer_class = GroupMembershipSerializer
    permission_classes = [IsAuthenticated]
