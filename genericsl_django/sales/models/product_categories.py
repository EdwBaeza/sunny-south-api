
#django 
from django.db import models

#utils
from genericsl_django.utils.models import BaseModel


class ProductCategory(BaseModel):
    """ ProductCategorie Model"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'