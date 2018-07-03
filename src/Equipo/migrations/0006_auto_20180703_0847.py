# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0005_equipo_mac'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='serieEnap',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='serie',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='serieEntel',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
