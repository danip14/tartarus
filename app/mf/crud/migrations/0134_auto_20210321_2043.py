# Generated by Django 3.1.1 on 2021-03-22 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0133_auto_20210321_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facilitator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Facilitador')),
                ('ci', models.CharField(max_length=50, unique=True, verbose_name='CI/RIF')),
                ('contact', models.CharField(max_length=50, verbose_name='Teléfono')),
                ('identity', models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='crud.id_type', verbose_name='Identificación')),
            ],
            options={
                'verbose_name': 'Facilitador',
                'verbose_name_plural': 'Facilitadores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='Grupo')),
            ],
            options={
                'verbose_name': 'Grupo de Productos',
                'verbose_name_plural': 'Grupo de Productos',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterField(
            model_name='detbudget',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.product'),
        ),
        migrations.AlterField(
            model_name='detsale',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.product'),
        ),
        migrations.DeleteModel(
            name='Product_warehouse',
        ),
        migrations.AddField(
            model_name='product',
            name='product_group',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='crud.product_group', verbose_name='Grupo'),
            preserve_default=False,
        ),
    ]