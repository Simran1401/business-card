# Generated by Django 3.2.5 on 2023-06-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0024_alter_orders_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='currency',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
