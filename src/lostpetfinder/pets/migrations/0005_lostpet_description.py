# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20170820_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostpet',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
