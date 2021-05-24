"""Order models."""

#django
from django.db import models

#utilities
from sunnysouth.utils.models import BaseModel


class PurchaseProduct(BaseModel):
    """ represents a sale of a group of products."""

    product = models.ForeignKey('marketplace.Product', on_delete=models.CASCADE)
    purchase = models.ForeignKey('marketplace.Purchase', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
