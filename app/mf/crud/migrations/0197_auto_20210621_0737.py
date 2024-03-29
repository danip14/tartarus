# Generated by Django 3.1.6 on 2021-06-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0196_auto_20210620_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='datejoined',
            field=models.DateField(default='2021-06-21', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='objective',
            field=models.TextField(verbose_name='Objetivo'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-06-21', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='services',
            name='datejoined',
            field=models.DateField(default='2021-06-21', max_length=50, verbose_name='Fecha actualización'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='07:37:23 AM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_time',
            field=models.DateField(default='2021-06-21', max_length=50, verbose_name='Fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-06-21 07:37:23 AM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
