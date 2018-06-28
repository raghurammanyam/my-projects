# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-06 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DETAILS', '0004_auto_20180605_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='subject',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='DETAILS.StudentMarks', to_field='subject'),
        ),
    ]
