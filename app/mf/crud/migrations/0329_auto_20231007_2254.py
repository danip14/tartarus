# Generated by Django 3.1.6 on 2023-10-08 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0328_auto_20231007_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confrontations',
            old_name='qtyRound',
            new_name='qtyRound1',
        ),
        migrations.RemoveField(
            model_name='dettournament',
            name='qtyRound',
        ),
        migrations.AddField(
            model_name='confrontations',
            name='qtyRound2',
            field=models.IntegerField(default=0),
        ),
    ]
