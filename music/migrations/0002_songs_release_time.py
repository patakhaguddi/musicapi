# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 09:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
