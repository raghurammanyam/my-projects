# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 03:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DETAILS', '0011_auto_20180607_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='subject',
            field=models.ForeignKey(blank=True, db_column=b'subject', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_studentmarks', to='DETAILS.Subject', to_field=b'name'),
        ),
    ]
