# Generated by Django 4.0.6 on 2022-07-25 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syrent_app', '0011_rename_phone_contact_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company',
            field=models.CharField(max_length=30, verbose_name='Company name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email_address',
            field=models.EmailField(max_length=100, verbose_name='e-mail address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='note',
            field=models.TextField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number'),
        ),
    ]
