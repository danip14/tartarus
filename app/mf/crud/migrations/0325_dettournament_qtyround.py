# Generated by Django 3.1.6 on 2023-10-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0324_dettournament_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='dettournament',
            name='qtyRound',
            field=models.IntegerField(default=0),
        ),
    ]