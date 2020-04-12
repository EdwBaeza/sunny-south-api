""" sale models."""

#django
from django.db import models
from django.contrib.postgres.fields import JSONField
#models
#from genericsl_django.models import Product

#utitlities 
from genericsl_django.utils.models import BaseModel


class Sale(BaseModel):
    order_number = models.BigIntegerField()
    products = models.ManyToManyField('sales.product', through='sales.order')
    
    amount = models.FloatField()
    user_ranking = models.FloatField(default=5.0, null= True)
    supplier_raking = models.FloatField(default=5.0, null=True)
    location = JSONField(null=True)
    paid_at = models.DateTimeField(null=True)