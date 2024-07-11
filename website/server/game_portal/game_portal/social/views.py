from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from .serializers import FriendSerializer
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Friend

User = get_user_model()

@login_required
def add_friend(request, user_id):
    user = request.user
    friend = get_object_or_404(User, id=user_id)
    Friend.objects.add_friend(user, friend)
    return redirect('profile', user_id=user_id)

@login_required
def remove_friend(request, user_id):
    user = request.user
    friend = get_object_or_404(User, id=user_id)
    Friend.objects.remove_friend(user, friend)
    return redirect('profile', user_id=user_id)

class FriendListView(generics.ListAPIView):
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Friend.objects.filter(user=self.request.user)
