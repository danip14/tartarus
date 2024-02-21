# Generated by Django 3.1.6 on 2021-07-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0224_auto_20210705_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='16:14:10 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-05 16:14:10 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
