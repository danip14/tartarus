# Generated by Django 3.1.6 on 2021-07-31 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0276_auto_20210730_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detmaintenance',
            name='period',
            field=models.CharField(choices=[('NO APLICA', 'NO APLICA'), ('TRIMESTRAL', 'TRIMESTRAL'), ('SEMESTRAL', 'SEMESTRAL'), ('ANUAL', 'ANUAL')], default='NO APLICA', max_length=50, verbose_name='Período'),
        ),
        migrations.AlterField(
            model_name='equipmentsummary',
            name='calibrationPeriod',
            field=models.CharField(choices=[('NO APLICA', 'NO APLICA'), ('TRIMESTRAL', 'TRIMESTRAL'), ('SEMESTRAL', 'SEMESTRAL'), ('ANUAL', 'ANUAL')], default='NO APLICA', max_length=50, verbose_name='Periocidad calibración metrológico (meses)'),
        ),
        migrations.AlterField(
            model_name='equipmentsummary',
            name='datejoined',
            field=models.DateField(default='2021-07-31', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='day',
            field=models.DateField(default='2021-07-31', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='datejoined',
            field=models.DateField(default='2021-07-31', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='invoicesandquotes',
            name='datejoined',
            field=models.DateField(default='31-07-2021', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='datejoined',
            field=models.DateField(default='2021-07-31', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2021-07-31', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='services',
            name='dateRegister',
            field=models.DateField(default='2021-07-31', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='00:09:55 AM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_time',
            field=models.DateField(default='2021-07-31', max_length=50, verbose_name='Fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-31 00:09:55 AM', max_length=50, verbose_name='Fecha y Hora'),
        ),
    ]
