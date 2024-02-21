# Generated by Django 3.1.6 on 2021-07-07 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0245_auto_20210707_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['id'], 'verbose_name': 'Empresa/Clínica/Hospital/Centro', 'verbose_name_plural': 'Empresas/Clínicas/Centros'},
        ),
        migrations.AddField(
            model_name='business',
            name='city',
            field=models.CharField(default=2, max_length=255, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='names',
            field=models.CharField(max_length=255, verbose_name='Nombres / Razón Social'),
        ),
        migrations.AlterField(
            model_name='business',
            name='nit',
            field=models.CharField(max_length=50, verbose_name='NIT ó C.C'),
        ),
        migrations.AlterField(
            model_name='equipmentsummary',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.business', verbose_name='Empresa/Clínica/Hospital/Centro'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.business', verbose_name='Empresa/Clínica/Hospital/Centro'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.business', verbose_name='Empresa/Clínica/Hospital/Centro'),
        ),
        migrations.AlterField(
            model_name='services',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.business', verbose_name='Empresa/Clínica/Hospital/Centro'),
        ),
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='19:44:47 PM', max_length=250, verbose_name='Hora de entrega'),
        ),
        migrations.AlterField(
            model_name='services',
            name='equipment_date',
            field=models.CharField(default='2021-07-07 19:44:47 PM', max_length=50, verbose_name='Fecha y Hora'),
        ),
        migrations.CreateModel(
            name='InvoicesAndQuotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.IntegerField(default=0)),
                ('number_invoice', models.CharField(max_length=255, verbose_name='Nº Factura')),
                ('number_quotes', models.CharField(max_length=255, verbose_name='Nº Cotización')),
                ('sub_total', models.DecimalField(decimal_places=0, default=0.0, max_digits=30, verbose_name='Sub-Total')),
                ('discount_percentage', models.CharField(max_length=2, verbose_name='Descuento %')),
                ('discount', models.DecimalField(decimal_places=0, default=0.0, max_digits=30, verbose_name='Descuento')),
                ('total', models.DecimalField(decimal_places=0, default=0.0, max_digits=30, verbose_name='Total')),
                ('literalTotal', models.CharField(max_length=255, verbose_name='Total literal')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.business', verbose_name='Empresa/Clínica/Hospital/Centro')),
            ],
            options={
                'verbose_name': 'Factura y Cotización',
                'verbose_name_plural': 'Facturas y Cotizaciones',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='DetInvoicesAndQuotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=255, verbose_name='Código del producto')),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255, verbose_name='Descripción del producto')),
                ('price_unitary', models.DecimalField(decimal_places=0, default=0.0, max_digits=30, verbose_name='Precio unitario')),
                ('total', models.DecimalField(decimal_places=0, default=0.0, max_digits=30, verbose_name='Total')),
                ('invoicesAndQuotes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.invoicesandquotes', verbose_name='Relación con Facturas/Cotizaciones')),
            ],
            options={
                'verbose_name': 'Detalle factura/cotización',
                'verbose_name_plural': 'Detalles facturas/cotizaciones',
                'ordering': ['pk'],
            },
        ),
    ]
