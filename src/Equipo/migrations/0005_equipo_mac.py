# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0004_hardware'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(max_length=30)),
                ('serieEntel', models.CharField(max_length=30)),
                ('estado', models.BooleanField(default=True)),
                ('clase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Equipo.Clase')),
                ('hardware', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Equipo.Hardware')),
                ('software', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Equipo.Software')),
            ],
        ),
        migrations.CreateModel(
            name='MAC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(max_length=17)),
                ('descripcion', models.CharField(max_length=30)),
                ('equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Equipo.Equipo')),
            ],
        ),
    ]
