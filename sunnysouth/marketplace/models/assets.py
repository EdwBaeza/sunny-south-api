
# Django
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Lib
from sunnysouth.lib.models import BaseModel

def resolve_asset_directory_path(instance, filename):
    return f"{type(instance).__name__.lower()}/{instance.uuid}/{filename}"

class Asset(BaseModel):
    name = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=300, null=True)
    type = models.CharField(max_length=300, null=True)
    is_active = models.BooleanField("active", default=True, null=True)
    image = models.ImageField(upload_to=resolve_asset_directory_path, null=True)
    attachment = models.FileField(upload_to=resolve_asset_directory_path, null=True)
    attachable_object_id = models.IntegerField(null=True)
    attachable_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    attachable = GenericForeignKey("attachable_content_type", "attachable_object_id")
