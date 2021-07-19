# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0049_auto_20180926_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configglobal',
            name='electriccost',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AlterField(
            model_name='configglobal',
            name='emailtype',
            field=models.CharField(choices=[(b'Gmail', b'Gmail'), (b'Other', b'Other')], default=b'Gmail', max_length=20),
        ),
        migrations.AlterField(
            model_name='configglobal',
            name='sitename',
            field=models.CharField(default='Pimon', max_length=100),
        ),
    ]
