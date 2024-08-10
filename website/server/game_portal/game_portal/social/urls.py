from django.urls import path
from .views import add_friend, remove_friend, FriendListView

urlpatterns = [
  path('add/<str:user_id>/', add_friend, name='add_friend'),
  path('remove/<str:user_id>/', remove_friend, name='remove_friend'),
  path('list/', FriendListView.as_view(), name='friend_list'),
]