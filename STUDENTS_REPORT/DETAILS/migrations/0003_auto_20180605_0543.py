# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DETAILS', '0002_auto_20180605_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='subject',
            field=models.CharField(max_length=30),
        ),
    ]