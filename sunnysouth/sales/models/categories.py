
#django
from django.db import models

#utils
from sunnysouth.utils.models import BaseModel

class Category(BaseModel):
    """ Category Model"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
