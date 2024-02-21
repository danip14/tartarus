# Generated by Django 3.1.1 on 2021-01-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0023_auto_20210104_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Razón Social')),
                ('rif', models.CharField(max_length=225, verbose_name='RIF')),
            ],
            options={
                'verbose_name': 'Información de la Empresa',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CompanySedes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=225, verbose_name='Dirección Fiscal')),
                ('postal_zone', models.CharField(max_length=100, verbose_name='Zona Postal')),
                ('phone', models.CharField(max_length=100, verbose_name='Contacto')),
                ('email', models.CharField(max_length=100, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Información de las Sedes',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='cancelledinvoices',
            name='pay_date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='changescanceled',
            name='pay_date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='end_date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha límite'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='start_date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha de Inicio'),
        ),
        migrations.AlterField(
            model_name='dollarpurchase',
            name='pay_date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='earnings',
            name='date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='equipmentmaintenance',
            name='next_serv',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Próximo Servicio'),
        ),
        migrations.AlterField(
            model_name='equipmentmaintenance',
            name='pay_date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='pay_date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha de Pago'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='product_warehouse',
            name='date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datejoined',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='admission_date',
            field=models.DateField(default='2021-01-05', max_length=10, verbose_name='Ingreso'),
        ),
    ]