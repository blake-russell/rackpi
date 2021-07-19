# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-30 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0010_auto_20180830_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='myrig',
            name='gpio',
            field=models.IntegerField(choices=[(0, b'BCM 0'), (1, b'BCM 1'), (2, b'BCM 2'), (3, b'BCM 3'), (4, b'BCM 4'), (5, b'BCM 5'), (6, b'BCM 6'), (7, b'BCM 7'), (8, b'BCM 8'), (9, b'BCM 9'), (10, b'BCM 10'), (11, b'BCM 11'), (12, b'BCM 12'), (13, b'BCM 13'), (14, b'BCM 14'), (15, b'BCM 15'), (16, b'BCM 16'), (17, b'BCM 17'), (18, b'BCM 18'), (19, b'BCM 19'), (20, b'BCM 20'), (21, b'BCM 21'), (22, b'BCM 22'), (23, b'BCM 23'), (24, b'BCM 24'), (25, b'BCM 25'), (26, b'BCM 26'), (27, b'BCM 27')], default=0),
        ),
        migrations.AddField(
            model_name='myrig',
            name='passw',
            field=models.CharField(default='pass', max_length=100),
        ),
        migrations.AddField(
            model_name='myrig',
            name='status',
            field=models.CharField(choices=[(b'Online', b'Online'), (b'Offline', b'Offline')], default=b'Online', max_length=7),
        ),
        migrations.AddField(
            model_name='myrig',
            name='ttwait',
            field=models.IntegerField(default='300'),
        ),
        migrations.AddField(
            model_name='myrig',
            name='user',
            field=models.CharField(default='user', max_length=100),
        ),
    ]