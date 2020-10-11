""" sales models."""

#django
from django.db import models
from django.contrib.postgres.fields import JSONField
#models
from sunnysouth.users.models import Profile
#utitlities
from sunnysouth.utils.models import BaseModel


class Sale(BaseModel):
    """ Sales Class """

    class StatusInSales(models.TextChoices):
        STARTED = 'started'
        CANCELED = 'canceled'
        FINISHED = 'finished'


    code = models.CharField(max_length=60)
    amount = models.FloatField()
    location = JSONField(null=True)
    products = models.ManyToManyField('sales.product', through='sales.order')
    paid_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=20,
        choices=StatusInSales.choices,
        default=StatusInSales.STARTED,
    )

    client_ranking = models.FloatField(default=5.0, null= True)
    supplier_raking = models.FloatField(default=5.0, null=True)

    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='supplier'
    )
