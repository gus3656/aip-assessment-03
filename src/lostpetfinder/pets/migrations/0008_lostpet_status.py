# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_auto_20170820_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostpet',
            name='status',
            field=models.CharField(choices=[('Lost', 'Lost'), ('Found', 'Found')], max_length=20, null=True),
        ),
    ]
