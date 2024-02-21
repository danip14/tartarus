# Generated by Django 3.1.6 on 2021-07-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0235_auto_20210707_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='logo',
            field=models.FileField(blank=True, default='Logo/equibiomed.png', null=True, upload_to='Logo'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='06:51:45 AM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-07 06:51:45 AM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
