# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 12:27
from __future__ import unicode_literals

import Personal.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CDC', models.CharField(max_length=8, unique=True, validators=[Personal.validators.value_is_correct_expression_regular])),
                ('Area', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('NombreSecundario', models.CharField(max_length=30, null=True)),
                ('Apellido', models.CharField(max_length=30, null=True)),
                ('ApellidoMaterno', models.CharField(max_length=30, null=True)),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personal.Areas')),
                ('Gestor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Personal.Personas')),
            ],
        ),
        migrations.CreateModel(
            name='Puestos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Puesto', models.CharField(max_length=30, unique=True, validators=[Personal.validators.value_is_lowercase])),
            ],
        ),
        migrations.AddField(
            model_name='personas',
            name='Puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personal.Puestos'),
        ),
    ]
