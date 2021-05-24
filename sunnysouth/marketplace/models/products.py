""" Produc Models."""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser

#models
# from sunnysouth.marketplace.models import Profile
# from sunnysouth.marketplace.models import Category

#utitilties
from sunnysouth.utils.models import BaseModel

class Product(BaseModel):
    """ Product Model
            this class represents the product that customers will buy
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    stock = models.PositiveIntegerField(default=1)
    custom_features = models.JSONField()
    code = models.CharField(max_length=50, null=True)
    picture = models.ImageField(
        'product picture',
        upload_to='products/pictures',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text= 'softdelete product'
    )
    is_hidden = models.BooleanField(
        'hidden',
        default=False,
        help_text='define if the product is hidden on product list'
    )
    home_service_enabled = models.BooleanField(default=True)
    # supplier = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'marketplace.Category',
        on_delete=models.CASCADE
    )
