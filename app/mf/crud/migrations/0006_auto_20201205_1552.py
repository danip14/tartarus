# Generated by Django 3.1.1 on 2020-12-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20201205_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelledinvoices',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Cap_Facturas'),
        ),
    ]
