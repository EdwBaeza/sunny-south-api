# Generated by Django 3.1 on 2021-10-31 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_auto_20210923_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='attachable_object_id',
            field=models.IntegerField(null=True),
        ),
    ]