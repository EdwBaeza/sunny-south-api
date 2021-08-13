# Django
from django.db import models

# Lib
from sunnysouth.lib.models import BaseModel


class PurchaseProduct(BaseModel):
    product = models.ForeignKey('marketplace.Product', on_delete=models.CASCADE)
    purchase = models.ForeignKey('marketplace.Purchase', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
