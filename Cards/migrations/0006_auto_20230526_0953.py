# Generated by Django 3.2.5 on 2023-05-26 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0005_auto_20230525_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cominfo',
            name='company_name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cominfo',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
