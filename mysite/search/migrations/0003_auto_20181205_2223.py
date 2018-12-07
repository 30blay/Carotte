# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-06 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20181205_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Specie'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Seller'),
        ),
    ]