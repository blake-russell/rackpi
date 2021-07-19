# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0029_auto_20180902_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='configpool',
            name='autosw',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='configpool',
            name='autoswurl',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='configpool',
            name='midurl',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='mypool',
            name='autosw',
            field=models.CharField(choices=[(b'yes', b'yes'), (b'no', b'no')], default=b'no', max_length=3),
        ),
        migrations.AddField(
            model_name='mypool',
            name='followsw',
            field=models.CharField(choices=[(b'yes', b'yes'), (b'no', b'no')], default=b'no', max_length=3),
        ),
        migrations.AlterField(
            model_name='configforecast',
            name='api',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='configforecast',
            name='zipcode',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='configpool',
            name='baseurl',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='configpool',
            name='confirmed',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='configpool',
            name='last24hr',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='configpool',
            name='nethash',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='configpool',
            name='poolhash',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='configpool',
            name='price',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='configpool',
            name='tailurl',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='mypool',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='mypool',
            name='api',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
