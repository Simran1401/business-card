# Generated by Django 3.2.5 on 2023-05-26 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0007_alter_aboutinfo_upload_documents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cominfo',
            old_name='company_profile',
            new_name='profile_picture',
        ),
    ]
