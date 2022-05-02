# Django
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Lib
from sunnysouth.lib.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField('marketplace.User', related_name='profile', on_delete=models.CASCADE)
    slug_name = models.CharField(max_length=300, null=True)
    biography = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField('active', default=True)
    reputation = models.FloatField(default=5.0)
    assets = GenericRelation(
        'marketplace.Asset',
        'attachable_object_id',
        'attachable_content_type',
        related_name="assets",
        related_query_name='assets_profile',
    )

    def images(self):
        return self.assets.filter(type='pictures')


