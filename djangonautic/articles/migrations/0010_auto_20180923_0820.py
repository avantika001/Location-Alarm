# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-23 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20180923_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontacts',
            name='number',
            field=models.CharField(blank=True, default='None', max_length=12),
        ),
    ]
