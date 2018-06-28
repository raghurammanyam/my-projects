# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count, Avg ,Max,Sum, Count
from itertools import chain
from django.http import JsonResponse

# Create your views here.
from DETAILS.models import StudentMarks, Subject
from django.http import HttpResponse, HttpResponseNotFound


""" Displays all student marks with subject"""

def studentdata(request):
    students = StudentMarks.objects.all() #retriving the students data from database
    print (students)
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context) #returns an combined html txt with context
    else:
        return HttpResponseNotFound("student not found") #it displays student not found in a webpage

""" Displays all subjects with realted faculty"""
def facultydata(request):
    faculty = Subject.objects.all() #retriving the subject-faculty data from the database
    if faculty:
        context = {
            'faculty': faculty
        }
        return render(request, 'students.html', context)# it returns a combined txt of html with context
    else:
        return HttpResponseNotFound(" not found")
"""Displays student with marks related to given id"""
def getstudentid(request,_id):
    print (_id)
    students = StudentMarks.objects.filter(id =_id) #retriving the data related to given id from the database using filter method.
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context) #it renders a html with context and returns a http response object
    else:
        return HttpResponseNotFound("student not found")

"""Displays  appropriate subject marks with studentnames depends on the subject name given in the filter function"""
def getsubject(request,_subject):
    _subject = _subject.replace('%', ' ')
    students = StudentMarks.objects.filter(subject =_subject) #retriving the student data related to given subject name in the filter
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context)#it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")

""" Displays appropriate student, marks with subject depends on the student name given in the filter function"""

def getstudentname(request,_studentname):
    students = StudentMarks.objects.filter(student_name =_studentname) #retriving appropriate student data given in the filter from the database
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context) #it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")
""" Displays a student marks with subject depends  on given range of marks """

def getstudentmarks(request,_range):

    print(_range)
    start,end = [int(x) for x in _range.split('-')] #list comphrension for range
    students = StudentMarks.objects.filter(Q(marks__gte=start)&Q(marks__lte=end)&Q(subject='English')) #retriving the studentdata by using queryset in filter for given range of marks and particular subject
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context) #it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")

""" Displays a student marks with subject with above 90 marks """
def getrange(request):

    students = StudentMarks.objects.filter(Q(marks__gte=90)) #retriving the student data who got above 90 marks with subject by using queryset(gte =greater than or equal to) in filters from the database
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context) #it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")

""" Displays a particular marks with students given in the filter """

def getmarks(request,_marks):
    _marks = _marks.replace('%', ' ')

    students = StudentMarks.objects.filter(marks =_marks)  #retriving the student data who got particular marks with subject by using filters from the database
    print (students)
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context) #it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")

"""Displays Maths Topper """

def getmathstopper(request):
    max_rating = StudentMarks.objects.filter(subject="Mathematics").aggregate(Max('marks'))['marks__max']
    students = StudentMarks.objects.filter(marks = max_rating, subject="Mathematics") #retriving data of students marks who got highest in maths from the database
    print (students)
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context) #it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")

"""Displays Maths Topper """

def getmathtopper(request):
    students = StudentMarks.objects.filter(subject="Mathematics").order_by('-marks')[:1] #retriving data of students marks who got highest in maths by using filter method and order_by methods
    print (students)
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context) #it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")

""" Displays the particular subject average mark by  group by subject """

def getengavg(request,_subjectname):
        subjectaverage= StudentMarks.objects.all().values('subject').filter(subject=_subjectname).annotate(avg_sub=Avg('marks')).filter(Q(marks__gte=40)) #retriving the data from database and calculate the partucular subject average
        print (subjectaverage)
        if subjectaverage:
            context = {
                'subjectaverage':subjectaverage
            }
            return render(request, 'students.html', context) #it renders a combination of html with context and returns a http response
        else:
            return HttpResponseNotFound("student not found")

"""Displays the each student total marks and display in json format"""

def getsum(request):
    totalmarks= StudentMarks.objects.all().values('student_name') .annotate(total_marks=Sum('marks')) #retrive the student marks from the database and calculate the total marks of each student by using group_by method to student name and sum function
    print (list(totalmarks))
    if totalmarks:
        context = {
            'totalmarks':list(totalmarks)
        }
        return JsonResponse(context)  #it renders  context and returns a json response
    else:
        return HttpResponseNotFound("student not found")

""" 6th query : AVerage mark for each subject ignore failuers"""

def getsubavg(request):
    students= StudentMarks.objects.all().values('subject') .annotate(total=Avg('marks')).filter(Q(marks__gte=40))# retrive the data of students from the database and caluculate the average mark for each subject by using filter and group_by methods
    if students:
        context = {
            'students':students
        }
        return render(request, 'students.html', context)#it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")

"""1st query:faculty with above 90 marks count"""

def getsubninty(request):
    stud=StudentMarks.objects.all().values('subject').annotate(total=Count('student_name')).filter(Q(marks__gte=90)).order_by('-total') # retrive the data from student marks table get and subject with above 90 marks by using group and count
    subject = stud.first()['subject'] # here we get the highest count of subject by using first method and assigned to subject
    #stud=list(stud)
    print(stud)
    sub= Subject.objects.get(name=stud.first()['subject']) # retrive the data from subject table related to the highest subject count
    print(sub)
    context ={'aboveninty':{'subject':sub.name,'faculty':sub.faculty,'count':stud.first()['total']}} #mapping values to keys
    return JsonResponse(context)

"""2nd query:faculty with above 40marks count"""

def getfachigh(request):
    stud=StudentMarks.objects.all().values('subject') .annotate(total=Count('student_name')).filter(Q(marks__gte=41)).order_by('-total') # retrive the data from student marks table get and subject with above 40 marks by using group and count
    #stud=list(stud)
    subject = stud.first()['subject']# here we get the highest count of subject by using first method and assigned to subject
    print(stud)
    sub=Subject.objects.get(name = stud.first()['subject']) # retrive the data from subject table related to the highest subject count
    context ={'aboveninty':{'subject':sub.name,'faculty':sub.faculty,'count':stud.first()['total']}}
    return JsonResponse(context)


"""3rd query:faculty with below 40marks count"""

def getfacleast(request):
    stud=StudentMarks.objects.all().values('subject') .annotate(total=Count('student_name')).filter(Q(marks__lte=40)).order_by('total') # retrive the data from student marks table get and subject with below 40 marks by using group and count
    #stud=list(stud)
    print(stud)
    subject = stud.first()['subject']# here we get the lowest count of subject by using first method and assigned to subject
    sub=Subject.objects.get(name = stud.first()['subject']) ## retrive the data from subject table related to the lowest subject count
    context ={'least fail count':{'subject':sub.name,'faculty':sub.faculty,'count':stud.first()['total']}}
    return JsonResponse(context)

""" 4th query : STUDENT with highest Total"""

def getmaxtotal(request):
    totalmarks= StudentMarks.objects.all().values('student_name').annotate(total_marks=Sum('marks')).order_by('-total_marks')[:1] #retrive the data from database and calculate the each student total by using order_by and reverse methods we get the topper
    print (totalmarks)
    if totalmarks:
        context = {
            'totalmarks':totalmarks
        }
        return render(request, 'students.html', context) #it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")

""" 7th query:STUDENT with Least Total"""

def getmintotal(request):
    totalmarks= StudentMarks.objects.all().values('student_name').annotate(total_marks=Sum('marks')).order_by('total_marks')[:1] #retrive the data from database and calculate the each student total by using order_by method we get the student with less total
    print (totalmarks)
    if totalmarks:
        context = {
            'totalmarks':totalmarks
        }
        return render(request, 'students.html', context)#it renders a combination of html with context and returns a http response
    else:
        return HttpResponseNotFound("student not found")
