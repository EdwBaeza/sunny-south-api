from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    Product = apps.get_model('sales', 'Product')
    Sale = apps.get_model('sales', 'Sale')
    Order = apps.get_model('sales', 'Order')
    ProductCategory = apps.get_model('sales', 'ProductCategory')

    models = [Product, Sale, ProductCategory, Order]
    for model in models:
        for row in model.objects.all():
            row.uuid = str(uuid.uuid4()).replace('-', '')
            row.save(update_fields=['uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20201012_0106'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
