# Generated by Django 3.2.5 on 2023-06-08 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0027_orders_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='user',
        ),
    ]
