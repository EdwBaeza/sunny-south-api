""" Me tests. """

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from sunnysouth.marketplace.models import User, Profile

# Tokens
from rest_framework_simplejwt.tokens import RefreshToken


class UserAPITestCase(APITestCase):
    """ Me API test case. """

    def setUp(self):
        self.url = "/api/v1/users/me"
        self.user_attributes = {
            "email": "base@test.com",
            "username": "base",
            "password": "123456.a",
            "first_name": "test",
            "last_name": "test",
            "is_verified": True
        }
        self.user = User.objects.create(**self.user_attributes)
        self.profile = Profile.objects.create(biography="Testing biography", user=self.user)
        acces_token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {acces_token}")

    def test_get_current_user(self):
        """ Get current user """
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_update_current_user(self):
        """ Update current user """
        body = { "first_name": "new name", "profile": { "biography": "Updated.." }}
        response = self.client.patch(self.url, body, format="json")
        json_response =  response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK, json_response)
        self.assertEqual(json_response["first_name"], body['first_name'], json_response)
        self.assertEqual(json_response['profile']['biography'], body['profile']['biography'], json_response)

    def test_update_invalid_current_user(self):
        """ Update invalid current user by he dont verified yet """
        self.user.is_verified = False
        self.user.save()
        body = { "user": { "first_name": "new name fake" } }
        response = self.client.patch(self.url, body, format="json")
        json_response = response.json()
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, json_response)
        self.assertEqual(json_response["detail"], "Invalid user", json_response)
        self.assertEqual(self.user.first_name, "test", self.user.first_name)
