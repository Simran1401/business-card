# Generated by Django 3.2.5 on 2023-05-26 05:15

import config.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0010_alter_aboutinfo_upload_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cominfo',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=config.models.rename_file),
        ),
    ]