# Generated by Django 3.1.6 on 2021-07-22 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0274_auto_20210721_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='dateRegister',
            field=models.DateField(default='2021-07-21', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='23:07:38 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-21 23:07:37 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]