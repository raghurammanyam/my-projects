# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import StudentMarks, Subject

class SubjectDetail(admin.ModelAdmin):
    list_display = ('name', 'faculty')

admin.site.register(Subject, SubjectDetail)

class StudentMarksDetail(admin.ModelAdmin):
    list_display = ('student_name','subject','marks')

admin.site.register(StudentMarks,StudentMarksDetail)
# Register your models here.
