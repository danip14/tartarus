# Generated by Django 3.1.6 on 2021-07-09 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0256_auto_20210708_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='22:50:32 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-08 22:50:32 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]