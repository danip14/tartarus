# Generated by Django 3.1.1 on 2021-02-01 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0069_auto_20210201_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='change',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='status_change',
        ),
    ]