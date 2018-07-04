# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0010_auto_20180703_1243'),
        ('PersonalEquipo', '0004_auto_20180704_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalequipo',
            name='equipos',
        ),
        migrations.AddField(
            model_name='personalequipo',
            name='equipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Equipo.Equipo'),
        ),
    ]