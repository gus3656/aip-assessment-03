# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_lostpet_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostpet',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='lostpet',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
    ]
