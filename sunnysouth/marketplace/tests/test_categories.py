""" Categories tests. """

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from sunnysouth.marketplace.models import User, Profile, Category

# Tokens
from rest_framework_simplejwt.tokens import RefreshToken

# Multipart data
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY

class CategoryAPITestCase(APITestCase):
    """ Users API test case. """

    def setUp(self):
        self.url = "/api/v1/categories/"
        self.user_attributes = {
            "email": "base@test.com",
            "username": "base",
            "password": "123456.a",
            "first_name": "test",
            "last_name": "test",
            "is_verified": True,
            'is_active': True
        }
        self.user = User.objects.create(**self.user_attributes)
        self.profile = Profile.objects.create(biography="Testing biography", user=self.user)
        acces_token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {acces_token}")

    def test_create_category(self):
        """ Create new category and expected successful response. """
        body = dict(name= 'Test', description= 'Testing.....')
        response = self.client.post(
            self.url,
            data=encode_multipart(data=body, boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.__dict__)

    # def test_signup_response_error(self):
    #     """ Create new user without any field and expected error response. """
    #     url = self.url + "users/signup/"
    #     response = self.client.post(url, self.data_error, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
