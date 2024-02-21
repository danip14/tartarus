# Generated by Django 3.1.1 on 2021-02-05 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0086_auto_20210204_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='exchange',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=30, verbose_name='Cambio'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='exchange1',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=30, verbose_name='Cambio'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='exchange2',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=30, verbose_name='Cambio'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='received',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=30, verbose_name='Entrada (1)'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='received1',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=30, verbose_name='Entrada (2)'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='received2',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=30, verbose_name='Entrada (3)'),
        ),
    ]