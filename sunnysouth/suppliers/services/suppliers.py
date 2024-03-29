# Standard
from typing import Dict

# Django
from django.db import transaction

# Tasks
from sunnysouth.taskapp.tasks import send_confirmation_email

# Models
from sunnysouth.marketplace.models import Supplier, User, Address

from sunnysouth.lib.services import Service

class SupplierCreateService(Service):

    def run(self) -> Supplier:
        password = self.params.pop('password')
        self.params.pop('password_confirmation')
        supplier_data = self.params.pop('supplier', {})
        addresses_data = supplier_data.pop('addresses', [])

        user = User.objects.create(**self.params, is_verified=False)
        user.set_password(password)
        user.save()
        supplier = Supplier.objects.create(user=user, **supplier_data)
        for address_data in addresses_data:
            Address.objects.create(**address_data, addressable=supplier)

        transaction.on_commit(lambda: send_confirmation_email.delay(user_pk=user.pk))

        return supplier
