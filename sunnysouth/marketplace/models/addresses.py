
# Django
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Lib
from sunnysouth.lib.models import BaseModel


class Address(BaseModel):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    reference = models.CharField(max_length=300)
    custom_address = models.CharField(max_length=500)
    is_primary = models.BooleanField("primary", default=False)
    addressable_object_id = models.IntegerField()
    addressable_content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    addressable = GenericForeignKey("addressable_content_type", "addressable_object_id")
