# Generated by Django 3.1.6 on 2024-01-09 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0338_auto_20240108_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='Sin información', verbose_name='Descripción'),
            preserve_default=False,
        ),
    ]
