# Generated by Django 3.1.6 on 2021-05-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0190_auto_20210529_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='delivery_date',
            field=models.CharField(default='18:44:16', max_length=250, verbose_name='Hora de entrega'),
        ),
    ]