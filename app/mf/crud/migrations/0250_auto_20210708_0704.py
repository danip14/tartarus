# Generated by Django 3.1.6 on 2021-07-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0249_auto_20210708_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicesandquotes',
            name='report_type',
        ),
        migrations.AddField(
            model_name='invoicesandquotes',
            name='invoice',
            field=models.BooleanField(default=False, verbose_name='Factura'),
        ),
        migrations.AddField(
            model_name='invoicesandquotes',
            name='quote',
            field=models.BooleanField(default=False, verbose_name='Cotización'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='07:04:04 AM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-08 07:04:04 AM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
