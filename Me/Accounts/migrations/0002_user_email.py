# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-23 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]