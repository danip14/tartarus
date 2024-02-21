# Generated by Django 3.1.1 on 2021-01-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0030_auto_20210108_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='detbudget',
            name='price_product_bs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='detbudget',
            name='price_product_dl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='detbudget',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30),
        ),
    ]