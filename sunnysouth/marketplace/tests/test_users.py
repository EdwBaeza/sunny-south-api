""" User tests. """

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

# Models
from sunnysouth.marketplace.models.users import User

class UserAPITestCase(APITestCase):
    """ Users API test case. """

    def setUp(self):
        self.url = '/api/v1/'
        self.user_attributes = {
            "email": "base@test.com",
            "username": "base",
            "password": "123456.a",
            "first_name": "test",
            "last_name": "test",
            "is_verified": True
        }
        User.objects.create_user(**self.user_attributes)
        self.other_user_attributes = {
            "email": "test@test.com",
            "username": "test",
            "password": "123456.a",
            "password_confirmation": "123456.a",
            "first_name": "test",
            "last_name": "test",
            "phone_number": "9994169041",
            "profile": {
                "biography": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
            }
        }
        self.data_error = {
            "email": "test2@test.com",
            "username": "test2",
            "password": "123456.a",
            "password_confirmation": "123456.a"
        }
        self.data_error_code = {
            "token": "INCORECT"
        }
        self.data_login = {
            "email":"base@test.com",
            "password": "123456.a"
        }

    def test_signup_response_success(self):
        """ Create new user and expected successful response. """
        url = self.url + "users/signup/"
        response = self.client.post(url, self.other_user_attributes, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_signup_response_error(self):
        """ Create new user without any field and expected error response. """
        url = self.url + "users/signup/"
        response = self.client.post(url, self.data_error, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())

    def test_verificate_account_response_error(self):
        """ Try to validate account with incorrect code and expected error response. """
        url = self.url + "users/verify/"
        response = self.client.post(url, self.data_error_code, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())

    def test_login_response_success(self):
        """ Try to login account and expected success response. """
        url = self.url + "token/"
        response = self.client.post(url, self.data_login, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_login_response_error(self):
        """ Try to login nonexistent account and expected error responce. """
        url = self.url + "token/"
        self.data_login["email"] = 'nonexistent@test.com'
        response = self.client.post(url, self.data_login, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.json())
