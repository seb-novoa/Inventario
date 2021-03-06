# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0002_auto_20180619_0906'),
        ('Equipo', '0010_auto_20180703_1243'),
        ('PersonalEquipo', '0010_remove_personalequipo_atrasado'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalEquipoHistoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrega', models.DateTimeField(null=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('hw', models.CharField(max_length=100)),
                ('sw', models.CharField(max_length=100)),
                ('equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Equipo.Equipo')),
                ('persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Personal.Personas')),
            ],
        ),
    ]
