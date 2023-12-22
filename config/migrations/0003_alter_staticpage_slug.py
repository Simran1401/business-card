# Generated by Django 3.2.5 on 2023-05-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_alter_staticpage_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='slug',
            field=models.CharField(choices=[('Terms-&-Conditions', 'Terms-&-Condition'), ('Shipping-&-Delivery-Policy', 'Shipping-&-Delivery-Policy'), ('Refund-&-Cancellation-Policy', 'Refund-&-Cancellation-Policy'), ('Privacy-Policy', 'Privacy-Policy')], max_length=100),
        ),
    ]
