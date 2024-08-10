from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import FriendSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Friend

User = get_user_model()

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

class FriendListView(generics.ListAPIView):
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Friend.objects.filter(user=self.request.user)
