# Generated by Django 4.1.3 on 2022-11-07 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('nombre_marca', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('modelo', models.IntegerField()),
                ('unidades', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('detalles', models.CharField(max_length=100)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.marca')),
            ],
        ),
    ]
