# Generated by Django 3.1.6 on 2021-07-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0248_auto_20210707_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicesandquotes',
            name='datejoined',
            field=models.DateField(default='2021-07-08', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='equipmentsummary',
            name='datejoined',
            field=models.DateField(default='2021-07-08', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='datejoined',
            field=models.DateField(default='2021-07-08', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='datejoined',
            field=models.DateField(default='2021-07-08', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-07-08', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='services',
            name='datejoined',
            field=models.DateField(default='2021-07-08', max_length=50, verbose_name='Fecha actualización'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='06:52:05 AM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_time',
            field=models.DateField(default='2021-07-08', max_length=50, verbose_name='Fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-08 06:52:05 AM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
