# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-23 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_auto_20161224_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='u', max_length=255, unique=True),
        ),
    ]
