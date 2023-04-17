# Generated by Django 4.1.7 on 2023-04-11 08:13

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('unidades', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('modelo', models.CharField(max_length=30)),
                ('detalles', models.TextField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidades', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('fecha', models.DateTimeField(default=datetime.datetime(2023, 4, 11, 10, 13, 12, 737485))),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tienda.producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
