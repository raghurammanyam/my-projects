# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 04:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DETAILS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DETAILS.SubjectFaculty'),
        ),
    ]
