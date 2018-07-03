# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0003_auto_20180627_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('clases', models.ManyToManyField(to='Equipo.Clase')),
            ],
        ),
    ]