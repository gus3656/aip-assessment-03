# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_lostpet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostpet',
            name='status',
            field=models.CharField(choices=[('Lost', 'Lost'), ('Found', 'Found'), ('Registered', 'Registered')], default='Registered', max_length=20),
        ),
    ]
