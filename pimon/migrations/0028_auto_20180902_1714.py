# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pimon', '0027_auto_20180902_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='algo',
            field=models.CharField(choices=[(b'SHA-256', b'SHA-256'), (b'Ethash', b'Ethash'), (b'Scrypt', b'Scrypt'), (b'X11', b'X11'), (b'Equihash', b'Equihash'), (b'Zhash', b'Zhash'), (b'CryptoNightLiteV1', b'CryptoNightLiteV1'), (b'CryptoNightV7', b'CryptoNightV7'), (b'Blake (14r)', b'Blake (14r)'), (b'Blake (2b)', b'Blake (2b)'), (b'LBRY', b'LBRY'), (b'Pascal', b'Pascal'), (b'Lyra2REv2', b'Lyra2REv2'), (b'Myr-Groestl', b'Myr-Groestl'), (b'Qubit', b'Qubit'), (b'Quark', b'Quark'), (b'Skein', b'Skein'), (b'Nist5', b'Nist5'), (b'TimeTravel10', b'TimeTravel10'), (b'PHI1612', b'PHI1612'), (b'PHI2', b'PHI2'), (b'X16R', b'X16R'), (b'NeoScrypt', b'NeoScrypt'), (b'X11Gost', b'X11Gost'), (b'Any', b'Any'), (b'None', b'None')], default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='configticker',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickercoin', to='pimon.Coin', unique=True),
        ),
        migrations.AlterField(
            model_name='configwtm',
            name='algo',
            field=models.CharField(choices=[(b'SHA-256', b'SHA-256'), (b'Ethash', b'Ethash'), (b'Scrypt', b'Scrypt'), (b'X11', b'X11'), (b'Equihash', b'Equihash'), (b'Zhash', b'Zhash'), (b'CryptoNightLiteV1', b'CryptoNightLiteV1'), (b'CryptoNightV7', b'CryptoNightV7'), (b'Blake (14r)', b'Blake (14r)'), (b'Blake (2b)', b'Blake (2b)'), (b'LBRY', b'LBRY'), (b'Pascal', b'Pascal'), (b'Lyra2REv2', b'Lyra2REv2'), (b'Myr-Groestl', b'Myr-Groestl'), (b'Qubit', b'Qubit'), (b'Quark', b'Quark'), (b'Skein', b'Skein'), (b'Nist5', b'Nist5'), (b'TimeTravel10', b'TimeTravel10'), (b'PHI1612', b'PHI1612'), (b'PHI2', b'PHI2'), (b'X16R', b'X16R'), (b'NeoScrypt', b'NeoScrypt'), (b'X11Gost', b'X11Gost'), (b'Any', b'Any'), (b'None', b'None')], max_length=30),
        ),
        migrations.AlterField(
            model_name='miner',
            name='algo',
            field=models.CharField(choices=[(b'SHA-256', b'SHA-256'), (b'Ethash', b'Ethash'), (b'Scrypt', b'Scrypt'), (b'X11', b'X11'), (b'Equihash', b'Equihash'), (b'Zhash', b'Zhash'), (b'CryptoNightLiteV1', b'CryptoNightLiteV1'), (b'CryptoNightV7', b'CryptoNightV7'), (b'Blake (14r)', b'Blake (14r)'), (b'Blake (2b)', b'Blake (2b)'), (b'LBRY', b'LBRY'), (b'Pascal', b'Pascal'), (b'Lyra2REv2', b'Lyra2REv2'), (b'Myr-Groestl', b'Myr-Groestl'), (b'Qubit', b'Qubit'), (b'Quark', b'Quark'), (b'Skein', b'Skein'), (b'Nist5', b'Nist5'), (b'TimeTravel10', b'TimeTravel10'), (b'PHI1612', b'PHI1612'), (b'PHI2', b'PHI2'), (b'X16R', b'X16R'), (b'NeoScrypt', b'NeoScrypt'), (b'X11Gost', b'X11Gost'), (b'Any', b'Any'), (b'None', b'None')], max_length=30),
        ),
        migrations.AlterField(
            model_name='myrig',
            name='algo',
            field=models.CharField(choices=[(b'SHA-256', b'SHA-256'), (b'Ethash', b'Ethash'), (b'Scrypt', b'Scrypt'), (b'X11', b'X11'), (b'Equihash', b'Equihash'), (b'Zhash', b'Zhash'), (b'CryptoNightLiteV1', b'CryptoNightLiteV1'), (b'CryptoNightV7', b'CryptoNightV7'), (b'Blake (14r)', b'Blake (14r)'), (b'Blake (2b)', b'Blake (2b)'), (b'LBRY', b'LBRY'), (b'Pascal', b'Pascal'), (b'Lyra2REv2', b'Lyra2REv2'), (b'Myr-Groestl', b'Myr-Groestl'), (b'Qubit', b'Qubit'), (b'Quark', b'Quark'), (b'Skein', b'Skein'), (b'Nist5', b'Nist5'), (b'TimeTravel10', b'TimeTravel10'), (b'PHI1612', b'PHI1612'), (b'PHI2', b'PHI2'), (b'X16R', b'X16R'), (b'NeoScrypt', b'NeoScrypt'), (b'X11Gost', b'X11Gost'), (b'Any', b'Any'), (b'None', b'None')], default='Any', max_length=15),
        ),
    ]
