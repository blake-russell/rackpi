# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-30 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0005_auto_20180830_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miner',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]