# Generated by Django 3.2.12 on 2023-08-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0035_alter_bankdetail_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='is_delete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]