# Generated by Django 3.1.6 on 2021-07-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0258_auto_20210709_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='logo_business',
        ),
        migrations.AddField(
            model_name='business',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='Logos'),
        ),
        migrations.AlterField(
            model_name='equipmentsummary',
            name='datejoined',
            field=models.DateField(default='2021-07-10', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='day',
            field=models.DateField(default='2021-07-10', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='datejoined',
            field=models.DateField(default='2021-07-10', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='invoicesandquotes',
            name='datejoined',
            field=models.DateField(default='10-07-2021', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='datejoined',
            field=models.DateField(default='2021-07-10', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-07-10', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='services',
            name='datejoined',
            field=models.DateField(default='2021-07-10', max_length=50, verbose_name='Fecha actualización'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='13:06:13 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_time',
            field=models.DateField(default='2021-07-10', max_length=50, verbose_name='Fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-10 13:06:13 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
