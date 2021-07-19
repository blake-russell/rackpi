# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-30 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0007_auto_20180830_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miner',
            name='algo',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(b'SHA-256', b'SHA-256'), (b'Ethash', b'Ethash'), (b'Scrypt', b'Scrypt'), (b'X11', b'X11'), (b'Equihash', b'Equihash'), (b'Zhash', b'Zhash'), (b'CryptoNightLiteV1', b'CryptoNightLiteV1'), (b'CryptoNightV7', b'CryptoNightV7'), (b'Blake (14r)', b'Blake (14r)'), (b'Blake (2b)', b'Blake (2b)'), (b'LBRY', b'LBRY'), (b'Pascal', b'Pascal'), (b'Lyra2REv2', b'Lyra2REv2'), (b'Myr-Groestl', b'Myr-Groestl'), (b'Qubit', b'Qubit'), (b'Skein', b'Skein'), (b'TimeTravel10', b'TimeTravel10'), (b'PHI1612', b'PHI1612'), (b'PHI2', b'PHI2'), (b'NeoScrypt', b'NeoScrypt'), (b'X11Gost', b'X11Gost'), (b'Any', b'Any')], max_length=189),
        ),
        migrations.AlterField(
            model_name='miner',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='miner',
            name='software',
            field=models.CharField(choices=[(b'ccminer', b'ccminer'), (b'cgminer', b'cgminer'), (b'sgminer', b'sgminer'), (b'bgminer', b'bgminer'), (b'bfgminer', b'bfgminer'), (b'ethminer', b'ethminer')], max_length=10),
        ),
        migrations.AlterField(
            model_name='miner',
            name='type',
            field=models.CharField(choices=[(b'ASIC', b'ASIC'), (b'FPGA', b'FPGA'), (b'cFPGA', b'Custom FPGA'), (b'GPU', b'GPU')], max_length=10),
        ),
        migrations.AlterField(
            model_name='myrig',
            name='monitor',
            field=models.CharField(choices=[(b'yes', b'yes'), (b'no', b'no')], default=b'yes', max_length=3),
        ),
        migrations.AlterField(
            model_name='myrig',
            name='reset',
            field=models.CharField(choices=[(b'yes', b'yes'), (b'no', b'no')], default=b'yes', max_length=3),
        ),
        migrations.AlterField(
            model_name='myrig',
            name='software',
            field=models.CharField(choices=[(b'ccminer', b'ccminer'), (b'cgminer', b'cgminer'), (b'sgminer', b'sgminer'), (b'bgminer', b'bgminer'), (b'bfgminer', b'bfgminer'), (b'ethminer', b'ethminer')], max_length=10),
        ),
    ]
