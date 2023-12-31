# Generated by Django 3.2.12 on 2023-08-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0034_alter_cards_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='account_type',
            field=models.CharField(blank=True, choices=[('Savings Account', 'Savings Account'), ('Current Account', 'Current Account'), ('Salary Account', 'Salary Account'), ('Fixed Deposit Account', 'Fixed Deposit Account'), ('Recurring Deposit Account', 'Recurring Deposit Account'), ('NRO - Savings Accounts', 'NRO - Savings Accounts'), ('NRO - Fixed Deposit Accounts', 'NRO - Fixed Deposit Accounts'), ('NRE - Savings Accounts', 'NRE - Savings Accounts'), ('NRE - Fixed Deposit Accounts', 'NRE - Fixed Deposit Accounts'), ('FCNR - Account', 'FCNR - Account')], max_length=50, null=True),
        ),
    ]
