# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-05-24 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cementerio', '0014_auto_20200523_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='notas',
            field=models.CharField(
                blank=True, default='', max_length=500, null=True, verbose_name='Notas'),
        ),
    ]
