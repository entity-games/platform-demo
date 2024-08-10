from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from game_portal.accounts.models import Account
from game_portal.social.views import FriendListView
from game_portal.social.models import FriendManager


class TestAccounts:
    def setup_method(self):
        self.test_user = Account.objects.create_user(
            "test_user", "test@test.com", "pa88w0rd"
        )
        self.test_friend = Account.objects.create_user(
            "test_friend", "friend@test.com", "pa88w0rd"
        )
        self.test_friend2 = Account.objects.create_user(
            "test_friend2", "friend2@test.com", "pa88w0rd"
        )

    def test_add_friend_success(self, api_client):
        url = reverse("add_friend", args=[self.test_friend.id])        
        refresh = RefreshToken.for_user(self.test_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.post(url)
        assert response.status_code == 200

    def test_list_friends_not_logged_in(self, api_client):
        url = reverse("friend_list")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_list_friends_success(self, api_client):
        factory = APIRequestFactory()
        view = FriendListView.as_view()

        request = factory.get(reverse("friend_list"))
        force_authenticate(request, user=self.test_user)
        response = view(request)
        assert response.status_code == 200
        assert response.data == []

        FriendManager().add_friend(self.test_user, self.test_friend)
        FriendManager().add_friend(self.test_user, self.test_friend2)

        response = view(request)
        assert response.status_code == 200
        assert len(response.data) == 2
        names = [x['friend_name'] for x in response.data]
        assert 'test_friend' in names
        assert 'test_friend2' in names
