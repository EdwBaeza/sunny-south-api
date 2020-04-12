""" admin register."""

#django
from django.contrib import admin

#Models
from genericsl_django.sales.models import(
    ProductCategory,
    Product,
    Sale,
    Order
)

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Order)
