# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import square
class squareDetail(admin.ModelAdmin):
    list_display=('number','sqr')
admin.site.register(square,squareDetail)

# Register your models here.
