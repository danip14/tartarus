# Generated by Django 3.1.1 on 2021-03-22 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0135_auto_20210321_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='companysedes',
            name='rif',
            field=models.CharField(default=2, max_length=225, verbose_name='RIF'),
            preserve_default=False,
        ),
    ]
