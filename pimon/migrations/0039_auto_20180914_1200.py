# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0038_auto_20180913_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='enable',
            field=models.CharField(choices=[(b'yes', b'yes'), (b'no', b'no')], default=b'yes', max_length=3),
        ),
    ]
