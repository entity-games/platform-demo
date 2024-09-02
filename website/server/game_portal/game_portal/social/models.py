from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models


User = get_user_model()

class FriendManager(models.Manager):
    def add_friend(self, user, friend):
        friendship, _ = Friend.objects.get_or_create(user=user, friend=friend)
        return friendship

    def remove_friend(self, user, friend):
        Friend.objects.filter(user=user, friend=friend).delete()
        return

    def are_friends(self, user, friend):
        return Friend.objects.filter(user=user, friend=friend).exists()


class Friend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friendship_creator_set', on_delete=models.CASCADE)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friend_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    objects = FriendManager()

    class Meta:
        unique_together = ('user', 'friend')

    def __str__(self):
        return f"{self.user.username} is friends with {self.friend.username}"

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(User, through='GroupMembership')

    def __str__(self):
        return self.name

class GroupMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.group.name}"