# Generated by Django 3.1.6 on 2023-02-05 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0303_auto_20230205_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendingchanges',
            name='client',
        ),
        migrations.DeleteModel(
            name='DetPendingChanges',
        ),
        migrations.DeleteModel(
            name='PendingChanges',
        ),
    ]