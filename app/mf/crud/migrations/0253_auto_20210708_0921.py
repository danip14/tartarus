# Generated by Django 3.1.6 on 2021-07-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0252_auto_20210708_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='09:21:34 AM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-08 09:21:34 AM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]