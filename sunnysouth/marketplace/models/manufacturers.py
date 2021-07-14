
# Django
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Utilities
from sunnysouth.lib.models import BaseModel


class Manufacturer(BaseModel):
    class ManufacturerStatus(models.TextChoices):
        PENDING = 'pending'
        REJECTED = 'rejected'
        APPROVED = 'approved'

    name = models.CharField(max_length=300, blank=False, null=False)
    biography = models.TextField(max_length=500, blank=True)
    status = models.CharField(
        max_length=100,
        choices= ManufacturerStatus.choices,
        default=ManufacturerStatus.PENDING
    )
    is_active = models.BooleanField('active', default=True)
    reputation = models.FloatField(default=5.0)
    user = models.OneToOneField('marketplace.User', related_name='manufacturer', on_delete=models.CASCADE)
    addresses = GenericRelation(
        'marketplace.Address',
        'addressable_object_id',
        'addressable_content_type',
        related_query_name='manufacturer',
    )

