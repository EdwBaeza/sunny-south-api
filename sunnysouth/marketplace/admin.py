""" admin register."""

# django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from sunnysouth.marketplace.models import(
    Category,
    Product,
    Purchase,
    PurchaseProduct,
    User,
    Profile
)


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_verified')
    list_filter = ('is_staff', 'created', 'modified')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(PurchaseProduct)
