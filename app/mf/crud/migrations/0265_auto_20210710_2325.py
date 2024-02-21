# Generated by Django 3.1.6 on 2021-07-11 03:25

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0264_auto_20210710_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/static/media'), upload_to='', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='23:25:17 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-10 23:25:17 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
