
#Django
from django.db import models

#utils
from sunnysouth.utils.models import BaseModel

class Profile(BaseModel):
    """Profile Model."""

    user = models.OneToOneField('users.user', on_delete=models.CASCADE)
    slug_name = models.CharField(max_length=300, null=True)
    biography = models.TextField(max_length=500, blank=True)
    location = models.JSONField(null=True)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Consumer of products or services.'
        ),
        null=True
    )

    is_supplier = models.BooleanField(
        'supplier',
        default=False,
        help_text = 'Product or Service Provider.'
    )

    reputation = models.FloatField(
        default=5.0,
        help_text="Buying or selling products or services."
    )
