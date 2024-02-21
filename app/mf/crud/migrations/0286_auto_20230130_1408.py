# Generated by Django 3.1.6 on 2023-01-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0285_auto_20230128_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detclient',
            name='client',
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='client',
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='technician',
        ),
        migrations.RemoveField(
            model_name='installation',
            name='client',
        ),
        migrations.RemoveField(
            model_name='installation',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='installation',
            name='service',
        ),
        migrations.RemoveField(
            model_name='installation',
            name='technician',
        ),
        migrations.AlterField(
            model_name='eventos',
            name='day',
            field=models.DateField(default='2023-01-30', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2023-01-30', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='DetClient',
        ),
        migrations.DeleteModel(
            name='Inspection',
        ),
        migrations.DeleteModel(
            name='Installation',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Technician',
        ),
        migrations.DeleteModel(
            name='Zone',
        ),
    ]