""" sales models."""

#django
from django.db import models

#models
from sunnysouth.users.models import Profile

#utitlities
from sunnysouth.utils.models import BaseModel


class Sale(BaseModel):
    """ Sales Class """

    class StatusSales(models.TextChoices):
        STARTED = 'started'
        CANCELED = 'canceled'
        FINISHED = 'finished'

    code = models.CharField(max_length=60)
    amount = models.FloatField()
    location = models.JSONField(null=True)
    products = models.ManyToManyField('sales.product', through='sales.order')
    paid_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=20,
        choices=StatusSales.choices,
        default=StatusSales.STARTED,
    )

    client_ranking = models.FloatField(default=5.0)
    supplier_raking = models.FloatField(default=5.0)

    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='supplier'
    )
