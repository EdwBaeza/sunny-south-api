""" User tests. """

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from sunnysouth.marketplace.models import Supplier


class SupplierAPITestCase(APITestCase):
    """ Users API test case. """

    def setUp(self):
        self.url = '/api/v1/'
        self.supplier_attributes = {
            "username": "fake_username",
            "first_name": "fake",
            "last_name": "fake2",
            "email": "username@gmail.com",
            "phone_number": "9994169040",
            "password": "devtest02",
            "password_confirmation": "devtest02",
            "supplier": {
                "name": "Test01",
                "description": "Description 1,2,3,4",
                "addresses": [
                    {
                        "name": "My Home",
                        "city": "Merida",
                        "state": "Yucatan",
                        "country": "Mexico",
                        "latitude": "99.232323",
                        "longitude": "18.9999923",
                        "reference": "Fake reference",
                        "custom_address": "Testing..",
                        "is_primary": True
                    }
                ]
            }
        }

    def test_signup_response_success(self):
        """ Create new supplier and expected successful response. """
        url = self.url + "suppliers/signup/"
        response = self.client.post(url, self.supplier_attributes, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(1, Supplier.objects.count())
