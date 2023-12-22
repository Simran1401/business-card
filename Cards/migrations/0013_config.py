# Generated by Django 3.2.5 on 2023-05-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0012_alter_cominfo_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.IntegerField(default=9)),
                ('gallery_image', models.IntegerField(default=9)),
                ('card_expiry_days', models.IntegerField(default=30)),
            ],
        ),
    ]
