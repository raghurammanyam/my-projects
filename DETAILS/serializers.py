from rest_framework import serializers
from .models import StudentMarks,Subject


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('name', 'faculty')

class StudentMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMarks
        fields = ('student_name', 'subject', 'marks')
