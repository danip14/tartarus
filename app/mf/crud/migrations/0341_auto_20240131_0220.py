# Generated by Django 3.1.6 on 2024-01-31 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0340_auto_20240109_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='day',
            field=models.DateField(default='2024-01-31', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2024-01-31', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='team',
            name='birthdate',
            field=models.DateField(default='2024-01-31', max_length=50, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='datejoined',
            field=models.DateField(default='2024-01-31', max_length=10, verbose_name='Fecha'),
        ),
    ]