# Generated by Django 3.2.12 on 2023-08-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_alter_video_section_iframe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]