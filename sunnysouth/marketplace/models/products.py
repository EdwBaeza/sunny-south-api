# Django
from django.db import models

# Lib
from sunnysouth.lib.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    stock = models.PositiveIntegerField(default=1)
    custom_features = models.JSONField()
    code = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField('active', default=True)
    is_hidden = models.BooleanField('hidden', default=False)
    home_service_enabled = models.BooleanField(default=True)
    category = models.ForeignKey('marketplace.Category', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('marketplace.Manufacturer', on_delete=models.CASCADE, related_name='products')
