from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    User = apps.get_model('users', 'User')
    Profile = apps.get_model('users', 'Profile')
    models = [User, Profile]
    for model in models:
        for row in model.objects.all():
            row.uuid = str(uuid.uuid4()).replace('-', '')
            row.save(update_fields=['uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201012_0106'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
