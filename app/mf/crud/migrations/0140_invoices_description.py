# Generated by Django 3.1.1 on 2021-03-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0139_invoices'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='description',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Descripción'),
        ),
    ]
