# Generated by Django 3.1.1 on 2020-12-06 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_auto_20201205_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=255, verbose_name='Nombres y Apellidos')),
                ('ci', models.CharField(max_length=255, unique=True, verbose_name='Cédula')),
            ],
            options={
                'verbose_name': 'Conductor',
                'verbose_name_plural': 'Conductores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=255, unique=True, verbose_name='Placa')),
                ('brand', models.CharField(max_length=255, verbose_name='Marca')),
                ('model', models.CharField(max_length=255, verbose_name='Modelo')),
                ('features', models.CharField(max_length=255, verbose_name='Características')),
            ],
            options={
                'verbose_name': 'Vehículo',
                'verbose_name_plural': 'Vehículos',
                'ordering': ['id'],
            },
        ),
    ]