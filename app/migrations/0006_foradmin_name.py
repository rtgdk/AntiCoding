# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-02-22 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180222_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='foradmin',
            name='name',
            field=models.CharField(default='A', max_length=10, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
