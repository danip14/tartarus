# Generated by Django 3.1.6 on 2023-02-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0301_credit_datehour'),
    ]

    operations = [
        migrations.AddField(
            model_name='detcredit',
            name='datehour',
            field=models.CharField(default='2023-02-04', max_length=30, verbose_name='Fecha y Hora'),
        ),
        migrations.AddField(
            model_name='detcredit',
            name='last_credit_date',
            field=models.DateField(default='2023-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='datejoined',
            field=models.DateField(default='2023-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='datehour',
            field=models.CharField(default='2023-02-04', max_length=30, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='last_credit_date',
            field=models.DateField(default='2023-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='day',
            field=models.DateField(default='2023-02-04', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='pendingchanges',
            name='last_credit_date',
            field=models.DateField(default='2023-02-04', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2023-02-04', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datehour',
            field=models.CharField(default='2023-02-04', max_length=30, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datejoined',
            field=models.DateField(default='2023-02-04', max_length=10, verbose_name='Fecha'),
        ),
    ]
