# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DETAILS', '0007_auto_20180607_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_names', to='DETAILS.Subject'),
        ),
    ]
