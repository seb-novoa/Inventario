# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalEquipo', '0006_personalequipo_atrasado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalequipo',
            name='fecha_inicio',
            field=models.DateTimeField(),
        ),
    ]
