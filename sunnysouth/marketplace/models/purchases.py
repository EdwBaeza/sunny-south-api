""" sales models."""

#django
from django.db import models

#utitlities
from sunnysouth.utils.models import BaseModel


class Purchase(BaseModel):
    """ Sales Class """

    class PurchaseStatus(models.TextChoices):
        PENDING = 'pending'
        CANCELED = 'canceled'
        PAID = 'paid'

    total_amount = models.FloatField()
    address = models.JSONField()
    products = models.ManyToManyField('marketplace.Product', through='marketplace.PurchaseProduct')
    paid_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, choices=PurchaseStatus.choices, default=PurchaseStatus.PENDING)
    client_ranking = models.FloatField(default=5.0)
    manufacturer_ranking = models.FloatField(default=5.0)
    client = models.ForeignKey('marketplace.Profile', on_delete=models.CASCADE)
