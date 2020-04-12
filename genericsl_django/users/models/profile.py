
#Django
from django.db import models
from django.contrib.postgres.fields import JSONField

#utils
from genericsl_django.utils.models import BaseModel

class Profile(BaseModel):
    """ Profile Model"""

    user = models.OneToOneField('users.user', on_delete=models.CASCADE)
    
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)
    location = JSONField(null=True)
    # is_client = models.BooleanField(
    #     'client',
    #     default=True,
    #     help_text=(
    #         'Help easily distinguish users and perform queries. '
    #         'Clients are the main type of user.'
    #     ),
    # )

    is_supplier = models.BooleanField(
        'supplier',
        default=False,
        help_text = 'he sale the product to client'
    )
    
    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the rides taken and offered."
    )