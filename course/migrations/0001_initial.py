# Generated by Django 3.1.7 on 2021-11-22 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=50, verbose_name='Nit')),
                ('name', models.TextField(verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Revisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=50, verbose_name='Id')),
                ('name', models.TextField(verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Radicacion',
            fields=[
                ('radicacion_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Código de la radicación')),
                ('FechaRadicacion', models.DateField(verbose_name='Fecha de radicación')),
                ('NumeroFactura', models.CharField(max_length=50, verbose_name='Número de factura')),
                ('ValorFactura', models.IntegerField(verbose_name='Valor de la factura')),
                ('FechaFactura', models.DateField(verbose_name='Fecha de la factura')),
                ('Estamento', models.CharField(max_length=50, verbose_name='Afiliado')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.proveedor', verbose_name='Proveedor')),
                ('revisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.revisor', verbose_name='Revisor')),
            ],
        ),
        migrations.CreateModel(
            name='Aprobacion',
            fields=[
                ('aprobacion_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Código de la aprobación')),
                ('aprobado', models.CharField(max_length=50, verbose_name='Aprobado si/no')),
                ('FechaAprobado', models.DateField(verbose_name='Fecha de aprobación')),
                ('aceptado', models.CharField(max_length=50, verbose_name='Aceptado si/no')),
                ('radicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.radicacion', verbose_name='Radicacion')),
            ],
        ),
    ]
