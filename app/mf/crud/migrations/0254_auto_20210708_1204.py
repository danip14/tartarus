# Generated by Django 3.1.6 on 2021-07-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0253_auto_20210708_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicesandquotes',
            old_name='total',
            new_name='totalInvoice',
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='12:03:59 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-08 12:03:59 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
