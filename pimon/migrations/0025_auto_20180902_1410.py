# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 19:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0024_configwallet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configpool',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='configwallet',
            options={'ordering': ['name']},
        ),
    ]