"""Order models."""

#django
from django.db import models

#utilities
from sunnysouth.utils.models import BaseModel


class Order(BaseModel):
    """ represents a sale of a group of products."""

    product = models.ForeignKey('sales.product', on_delete=models.CASCADE)
    sale = models.ForeignKey('sales.sale', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    