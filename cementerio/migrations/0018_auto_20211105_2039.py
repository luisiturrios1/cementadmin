# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2021-11-06 03:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cementerio', '0017_auto_20210322_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='terreno',
            old_name='beneficiario',
            new_name='notas',
        ),
    ]