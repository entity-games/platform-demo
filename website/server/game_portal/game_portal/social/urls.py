from django.urls import path, include
from .views import add_friend, remove_friend, FriendListView, create_group, add_to_group, GroupViewSet, GroupMembershipViewSet, UserGroupsView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'list', GroupViewSet, name='list_groups')
router.register(r'memberships', GroupMembershipViewSet, basename="groups")

urlpatterns = [
]

urlpatterns = [
  path('add/<str:user_name>/', add_friend, name='add_friend'),
  path('remove/<str:user_id>/', remove_friend, name='remove_friend'),
  path('list/', FriendListView.as_view(), name='friend_list'),
  path('groups/create/<str:group_name>/', create_group, name='create_group'),
  path('groups/add/member/<str:group_id>/<str:member_id>', add_to_group, name="add_group_member"),
  path('groups/list', UserGroupsView.as_view(), name='group_list'),
]