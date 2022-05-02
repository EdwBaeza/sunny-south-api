""" Asset tests. """

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from sunnysouth.marketplace.models import User, Profile

# Tokens
from rest_framework_simplejwt.tokens import RefreshToken

# Multipart data
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY

class AssetAPITestCase(APITestCase):
    """ Me API test case. """

    def setUp(self):
        user_attributes = {
            "email": "base@test.com",
            "username": "base",
            "password": "123456.a",
            "first_name": "test",
            "last_name": "test",
            "is_verified": True
        }
        self.user = User.objects.create(**user_attributes)
        self.profile = Profile.objects.create(biography="Testing biography", user=self.user)
        acces_token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {acces_token}")
        self.url = "/api/v1/assets"

    def test_asset_creator(self):
        """ Create asset by current user """
        body = dict(
            file=open("sunnysouth/marketplace/tests/fixtures/automoviles.jpeg", "rb"),
            attachable_type="profile",
            attachable_id=self.profile.uuid,
            type="pictures"
        )
        response = self.client.post(
            path=self.url,
            data=encode_multipart(data=body, boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
