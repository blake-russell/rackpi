# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-04 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0057_auto_20181004_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='abv',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='coin',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]