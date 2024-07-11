from django.conf import settings
from django.db import models

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
