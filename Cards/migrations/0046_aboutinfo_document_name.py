# Generated by Django 3.2.5 on 2023-08-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0045_alter_aboutinfo_estblishment_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinfo',
            name='document_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
