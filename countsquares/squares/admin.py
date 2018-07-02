# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Square
class SquareDetail(admin.ModelAdmin):
    list_display=('number','sqr')
admin.site.register(Square,SquareDetail)

# Register your models here.
