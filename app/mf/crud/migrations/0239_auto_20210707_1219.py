# Generated by Django 3.1.6 on 2021-07-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0238_auto_20210707_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsandservices',
            name='image',
            field=models.FileField(blank=True, default='products/default.png', null=True, upload_to='img/products'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='12:19:47 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-07 12:19:47 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
