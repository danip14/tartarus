# Generated by Django 3.1.6 on 2023-02-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0306_companyinfo_logoinvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='datejoined',
            field=models.DateField(default='2023-02-10', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='datehour',
            field=models.CharField(default='2023-02-10', max_length=30, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='last_credit_date',
            field=models.DateField(default='2023-02-10', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='detcredit',
            name='datehour',
            field=models.CharField(default='2023-02-10', max_length=30, verbose_name='Fecha y Hora'),
        ),
        migrations.AlterField(
            model_name='detcredit',
            name='last_credit_date',
            field=models.DateField(default='2023-02-10', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='day',
            field=models.DateField(default='2023-02-10', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2023-02-10', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Precio costo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=180, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_bs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Precio bolivares'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_dl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Precio venta'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datehour',
            field=models.CharField(default='2023-02-10', max_length=30, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datejoined',
            field=models.DateField(default='2023-02-10', max_length=10, verbose_name='Fecha'),
        ),
    ]
