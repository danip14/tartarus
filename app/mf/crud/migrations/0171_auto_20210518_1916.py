# Generated by Django 3.1.6 on 2021-05-18 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0170_auto_20210518_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='identity',
            field=models.CharField(choices=[('V', 'V'), ('E', 'E'), ('J', 'J'), ('G', 'G'), ('P', 'P'), ('M', 'M')], default=1, max_length=2),
        ),
    ]
