# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_auto_20170820_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostpet',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='lostpet',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
