# Generated by Django 3.1.1 on 2021-02-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0074_creditnotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='budget_number',
            field=models.CharField(default='00000000', max_length=255, verbose_name='Presupuesto Nº'),
        ),
    ]