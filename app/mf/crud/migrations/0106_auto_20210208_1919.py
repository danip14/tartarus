# Generated by Django 3.1.1 on 2021-02-08 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0105_auto_20210208_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='desc_additional',
            field=models.CharField(default='No aplica', max_length=255, verbose_name='Descripción|Extras'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='desc_discounts',
            field=models.CharField(default='No aplica', max_length=255, verbose_name='Descripción|Deducciones'),
        ),
    ]