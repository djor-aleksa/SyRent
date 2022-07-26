# Generated by Django 4.0.6 on 2022-07-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syrent_app', '0007_alter_rentalitem_currency_alter_rentalitem_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='note',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='rentalitem',
            name='currency',
            field=models.CharField(default='RSD', max_length=3),
        ),
        migrations.AlterField(
            model_name='rentalitem',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]