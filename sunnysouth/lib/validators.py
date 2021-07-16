
# Django
from django.contrib.auth import password_validation

# RestFramework
from rest_framework import serializers


def validate_password(data):
    """ Validate password from dict. """
    password = data['password']
    password_confirmation = data['password_confirmation']
    if password != password_confirmation:
        raise serializers.ValidationError("Passwords don't match.")

    password_validation.validate_password(password)
