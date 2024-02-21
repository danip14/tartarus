# Generated by Django 3.1.6 on 2021-07-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0270_auto_20210715_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentsummary',
            name='datejoined',
            field=models.DateField(default='2021-07-20', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='day',
            field=models.DateField(default='2021-07-20', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='datejoined',
            field=models.DateField(default='2021-07-20', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='invoicesandquotes',
            name='datejoined',
            field=models.DateField(default='20-07-2021', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='datejoined',
            field=models.DateField(default='2021-07-20', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-07-20', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='00:24:25 AM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_time',
            field=models.DateField(default='2021-07-20', max_length=50, verbose_name='Fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-20 00:24:25 AM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]