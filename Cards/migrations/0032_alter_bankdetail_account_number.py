# Generated by Django 3.2.12 on 2023-08-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0031_auto_20230811_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='Account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
