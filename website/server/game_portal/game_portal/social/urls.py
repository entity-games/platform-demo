from django.urls import path, include
from .views import add_friend, remove_friend, FriendListView, create_group, GroupViewSet, GroupMembershipViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'groupmemberships', GroupMembershipViewSet)

urlpatterns = [
]

urlpatterns = [
  path('add/<str:user_id>/', add_friend, name='add_friend'),
  path('remove/<str:user_id>/', remove_friend, name='remove_friend'),
  path('list/', FriendListView.as_view(), name='friend_list'),
  path('groupadd/<str:group_name>/', create_group, name='create_group'),
  path('groups', include(router.urls)),
]