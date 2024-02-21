# Generated by Django 3.1.6 on 2023-09-15 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0314_auto_20230911_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='datejoined',
            field=models.DateField(default='2023-09-14', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='datehour',
            field=models.CharField(default='2023-09-14', max_length=30, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='last_credit_date',
            field=models.DateField(default='2023-09-14', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='debt',
            name='datehour',
            field=models.CharField(default='2023-09-14', max_length=30, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='debt',
            name='last_credit_date',
            field=models.DateField(default='2023-09-14', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='detcredit',
            name='datehour',
            field=models.CharField(default='2023-09-14', max_length=30, verbose_name='Fecha y Hora'),
        ),
        migrations.AlterField(
            model_name='detcredit',
            name='last_credit_date',
            field=models.DateField(default='2023-09-14', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='detdebt',
            name='datehour',
            field=models.CharField(default='2023-09-14', max_length=30, verbose_name='Fecha y Hora'),
        ),
        migrations.AlterField(
            model_name='detdebt',
            name='last_debt_date',
            field=models.DateField(default='2023-09-14', max_length=10, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='day',
            field=models.DateField(default='2023-09-14', max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='permisology',
            name='day',
            field=models.DateField(default='2023-09-14', max_length=50, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datehour',
            field=models.CharField(default='2023-09-14', max_length=30, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datejoined',
            field=models.DateField(default='2023-09-14', max_length=10, verbose_name='Fecha'),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Equipo')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='img/team')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre del Jugador')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.team', verbose_name='Equipo')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
                'ordering': ['id'],
            },
        ),
    ]
