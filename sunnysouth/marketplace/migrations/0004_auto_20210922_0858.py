# Generated by Django 3.1 on 2021-09-22 08:58

from django.db import migrations, models
import sunnysouth.marketplace.models.assets


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_auto_20210922_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='attachment',
            field=models.FileField(null=True, upload_to=sunnysouth.marketplace.models.assets.resolve_asset_directory_path),
        ),
        migrations.AlterField(
            model_name='asset',
            name='image',
            field=models.ImageField(null=True, upload_to=sunnysouth.marketplace.models.assets.resolve_asset_directory_path),
        ),
    ]
