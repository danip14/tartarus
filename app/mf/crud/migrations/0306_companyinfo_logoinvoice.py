# Generated by Django 3.1.6 on 2023-02-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0305_budget_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='logoInvoice',
            field=models.ImageField(blank=True, null=True, upload_to='img/logo'),
        ),
    ]
