# Generated by Django 3.1.6 on 2021-05-19 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0174_auto_20210518_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debts',
            name='type_debts',
            field=models.CharField(choices=[('Cobrar', 'Cobrar'), ('Pagar', 'Pagar')], default='Cobrar', max_length=10),
        ),
        migrations.DeleteModel(
            name='Type_debts',
        ),
    ]
