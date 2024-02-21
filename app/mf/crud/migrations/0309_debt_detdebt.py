# Generated by Django 3.1.6 on 2023-02-12 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0308_auto_20230211_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre/Razón Social')),
                ('last_credit_date', models.DateField(default='2023-02-11', max_length=10, verbose_name='Fecha')),
                ('datehour', models.CharField(default='2023-02-11', max_length=30, verbose_name='Fecha')),
                ('totalDebt', models.DecimalField(decimal_places=2, default=0.0, max_digits=30)),
            ],
            options={
                'verbose_name': 'Cuenta por pagar',
                'verbose_name_plural': 'Cuentas por pagar',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetDebt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_debt_date', models.DateField(default='2023-02-11', max_length=10, verbose_name='Fecha')),
                ('datehour', models.CharField(default='2023-02-11', max_length=30, verbose_name='Fecha y Hora')),
                ('operation', models.CharField(default='+', max_length=2, verbose_name='Operación')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Cantidad')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción')),
                ('debt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.debt')),
            ],
            options={
                'verbose_name': 'Detalle de cuenta por pagar',
                'verbose_name_plural': 'Detalle de cuentas por pagar',
                'ordering': ['id'],
            },
        ),
    ]