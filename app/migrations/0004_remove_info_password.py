# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-02-22 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180222_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='password',
        ),
    ]
