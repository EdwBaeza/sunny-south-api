""" admin register."""

#django
from django.contrib import admin

#Models
from sunnysouth.sales.models import(
    Category,
    Product,
    Sale,
    Order
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Order)
