# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2021-03-22 22:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cementerio', '0016_auto_20210226_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nombre', 'apellido']},
        ),
        migrations.AlterModelOptions(
            name='difunto',
            options={'ordering': ['nombre', 'apellido']},
        ),
    ]
