# Django
from django.db import models

# Lib
from sunnysouth.lib.models import BaseModel


class Purchase(BaseModel):
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
    supplier_ranking = models.FloatField(default=5.0)
    client = models.ForeignKey('marketplace.User', on_delete=models.CASCADE)
