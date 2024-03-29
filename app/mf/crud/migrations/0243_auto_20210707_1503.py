# Generated by Django 3.1.6 on 2021-07-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0242_auto_20210707_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsandservices',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=30, verbose_name='Costo'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='15:03:40 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-07 15:03:39 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
