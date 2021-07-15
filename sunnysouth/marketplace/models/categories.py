
# Django
from django.db import models

# Utils
from sunnysouth.lib.models import BaseModel


class Category(BaseModel):
    """ Category Model"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    picture = models.ImageField(
        'category picture',
        upload_to='categories/pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
