# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalEquipo', '0008_auto_20180705_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalequipo',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
