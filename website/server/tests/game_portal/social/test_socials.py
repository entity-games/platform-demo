from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from rest_framework import status

from game_portal.accounts.models import Account, AccountType


class TestAccounts:
    def setup_method(self):
        self.test_user = Account.objects.create_user(
            "test_user", "test@test.com", "pa88w0rd"
        )
        self.test_friend = Account.objects.create_user(
            "test_friend", "friend@test.com", "pa88w0rd"
        )
        self.create_url = reverse("register")

    def test_add_friend(self, api_client):
      fail()
