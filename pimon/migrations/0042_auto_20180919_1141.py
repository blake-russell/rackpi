# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0041_auto_20180919_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configglobal',
            name='profitrefresh',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='configglobal',
            name='wtmrefresh',
            field=models.IntegerField(default=60),
        ),
    ]