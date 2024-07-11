from django.urls import path
from .views import add_friend, remove_friend, FriendListView

urlpatterns = [
  path('add/<int:user_id>/', add_friend, name='add_friend'),
  path('remove/<int:user_id>/', remove_friend, name='remove_friend'),
  path('list/', FriendListView.as_view(), name='friend-list'),
]