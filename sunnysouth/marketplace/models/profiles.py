
#Django
from django.db import models

#utils
from sunnysouth.utils.models import BaseModel

class Profile(BaseModel):
    """Profile Model."""

    user = models.OneToOneField('marketplace.User', on_delete=models.CASCADE)
    slug_name = models.CharField(max_length=300, null=True)
    biography = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    reputation = models.FloatField(
        default=5.0,
        help_text="Buying or selling products or services."
    )
