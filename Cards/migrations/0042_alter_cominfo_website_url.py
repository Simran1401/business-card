# Generated by Django 3.2.12 on 2023-08-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0041_alter_cominfo_website_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cominfo',
            name='website_url',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]