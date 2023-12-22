# Generated by Django 3.2.5 on 2023-05-23 04:26

import config.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateBackgroundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='rename_file')),
            ],
        ),
        migrations.RenameField(
            model_name='cominfo',
            old_name='upload_company_profile',
            new_name='company_profile',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='about_us_cection',
            new_name='about_us_section',
        ),
        migrations.AddField(
            model_name='bankdetail',
            name='UPI_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cominfo',
            name='logo',
            field=models.ImageField(null=True, upload_to=config.models.rename_file),
        ),
        migrations.AddField(
            model_name='setting',
            name='bg_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Cards.templatebackgroundimage'),
        ),
    ]
