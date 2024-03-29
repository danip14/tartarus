# Generated by Django 3.1.6 on 2021-07-11 03:31

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0265_auto_20210710_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/static/media'), upload_to='', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='logo',
            field=models.ImageField(blank=True, default='logo/equibiomed.png', null=True, upload_to='img/logo'),
        ),
        migrations.AlterField(
            model_name='equipmentsummary',
            name='imageEquipment',
            field=models.ImageField(blank=True, default='Equipments/empty.png', null=True, upload_to='Equipments'),
        ),
        migrations.AlterField(
            model_name='productsandservices',
            name='image',
            field=models.ImageField(blank=True, default='img/products/default.png', null=True, upload_to='img/products', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='23:31:57 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-10 23:31:57 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image_equipment',
            field=models.ImageField(blank=True, default='Equipments/empty.png', null=True, upload_to='Equipments', verbose_name='Imagen del equipo'),
        ),
    ]
