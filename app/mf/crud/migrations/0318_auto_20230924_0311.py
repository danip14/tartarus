# Generated by Django 3.1.6 on 2023-09-24 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0317_auto_20230924_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ridding',
            old_name='roundNumber',
            new_name='free',
        ),
    ]