# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0008_auto_20180703_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mac',
            name='descripcion',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
