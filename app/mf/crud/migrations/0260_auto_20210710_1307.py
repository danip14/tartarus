# Generated by Django 3.1.6 on 2021-07-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0259_auto_20210710_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='Logos', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='13:07:10 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-10 13:07:10 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
