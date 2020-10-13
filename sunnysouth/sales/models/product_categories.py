
#django
from django.db import models

#utils
from sunnysouth.utils.models import BaseModel

class ProductCategory(BaseModel):
    """ ProductCategory Model"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'product_category'
        verbose_name_plural = 'product_categories'
