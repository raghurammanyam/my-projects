# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DETAILS', '0009_auto_20180607_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='subject',
            field=models.ForeignKey(db_column=b'subject', on_delete=django.db.models.deletion.CASCADE, to='DETAILS.Subject'),
        ),
    ]