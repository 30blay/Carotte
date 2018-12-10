# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-09 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20181209_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='latitude',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=18),
        ),
        migrations.AlterField(
            model_name='seller',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=18),
        ),
    ]
