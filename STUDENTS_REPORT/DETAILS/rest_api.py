from rest_framework.decorators import api_view
from rest_framework.response import Response
from DETAILS.models import StudentMarks,Subject
from django.shortcuts import render
from django.core import serializers
from .serializers import StudentMarksSerializer,SubjectSerializer
from django.http import JsonResponse
from django.db.models import Q,Sum,Avg,Max,Count


""" it is an testable api function"""
@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def test(request):
	return Response({'Everything': 'Fair and Lovely', 'Welcome': 'everybody'})

"""Displays only particular marks with students given in the filter"""
@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def studentmarks(request,_marks):
    _marks = _marks.replace('%', ' ')
    students = StudentMarks.objects.filter(marks = _marks) #retrive the apppropriate data from database given in the filter
    if students:
        serializer = StudentMarksSerializer(students,many=True) # serializer is  used to convert the model object to json format
        return Response(serializer.data) # returns a serializble json data and displays in a web page

    else:
        return Response({"Message": 'STUDENTS NOT FOUND'})

"""Displays above 90 marks with english subject given in the filter"""

@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def ninty(request):
    #_marks = _marks.replace('%', ' ')
    #print (marks)
    students = StudentMarks.objects.filter(Q(marks__gte=90)&Q(subject='English')) #retrive the apppropriate data from database given in the filter method
    if students:
        serializer = StudentMarksSerializer(students,many=True) # serializer is  used to convert the model object to json format
        return Response(serializer.data) # returns a serializble json data and displays in a web page
    else:
        return HttpResponseNotFound("student not found")


@api_view(['GET'])
def gettotal(request):

    totalmarks= StudentMarks.objects.all().values('student_name') .annotate(total_marks=Sum('marks'))

    print (list(totalmarks))

    if totalmarks:
		serializer = StudentMarksSerializer(totalmarks,many=True)
		print(serializer)
		return Response(serializer.data)
        #context = {
        #    'totalmarks':list(totalmarks)
        #}
        #return Response(serializer.data)
    else:
        return HttpResponseNotFound("student not found")

""" Displays all students data from StudentMarks table"""
@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def studentlist(request):
    students = StudentMarks.objects.all() #retriving data of all students marks with subjects
    if students:
        serializer = StudentMarksSerializer(students,many=True) # here serializer used to convert object form to json format
        return Response(serializer.data) # returns a data in the form of json format in the webpage
    else:
        return Response({"Message": 'STUDENTS NOT FOUND'})

""" Dispalys a highest Mathematics mark with student"""

@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def mathtop(request):
    students = StudentMarks.objects.filter(subject="Mathematics").order_by('-marks')[:1] #retriving data of students marks who got highest in maths by using filter method and order_by methods
    print (students)
    if students:
		 serializer = StudentMarksSerializer(students,many=True) # here serializer used to convert object form to json format
		 return Response(serializer.data) # returns a data in the form of json format in the webpage
    else:
         return Response("student not found")


""" 6th query : Dispalys AVerage mark for each subject ignore failuers"""
@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def subavg(request):
    students= StudentMarks.objects.all().values('subject') .annotate(average = Avg('marks')).filter(Q(marks__gte=40))# retrive the data of students from the database and caluculate the average mark for each subject by using filter and group_by methods
    if students:
		return JsonResponse({'students':list(students)}) # returns a context in the form of json format in the webpage




"""1st query:faculty with above 90 marks count"""
@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def subninty(request):
    stud=StudentMarks.objects.all().values('subject').annotate(total=Count('student_name')).filter(Q(marks__gte=90)).order_by('-total') # retrive the data from student marks table get and subject with above 90 marks by using group and count
    subject = stud.first()['subject'] # here we get the highest count of subject by using first method and assigned to subject
    print(stud)
    sub= Subject.objects.get(name=stud.first()['subject']) # retrive the data from subject table related to subject highest count in above query
    #sub=list(sub)
    print(sub)
    context ={'aboveninty':{'subject':sub.name,'faculty':sub.faculty,'count':stud.first()['total']}}
    return JsonResponse(context) # returns a context in the form of json format in the webpage

"""2nd query:faculty with above 40marks count"""
@api_view(['GET'])
def fachigh(request):
    stud=StudentMarks.objects.all().values('subject') .annotate(total=Count('student_name')).filter(Q(marks__gte=41)).order_by('-total') # retrive the data from student marks table get and subject with above 40 marks by using group and count
    #stud=list(stud)
    subject = stud.first()['subject'] # here we get the highest count of subject by using first method and assigned to subject
    print(stud)
    sub=Subject.objects.get(name = stud.first()['subject']) #retrive the data from subject table related to lowest subject count in above query
    context ={'aboveninty':{'subject':sub.name,'faculty':sub.faculty,'count':stud.first()['total']}}
    return JsonResponse(context) # returns a context in the form of json format in the webpage


"""3rd query:Displays faculty with below 40marks count"""
@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def facleast(request):
    stud=StudentMarks.objects.all().values('subject') .annotate(total=Count('student_name')).filter(Q(marks__lte=40)).order_by('total') # retrive the data from student marks table get and subject with below 40 marks by using group and count
    #stud=list(stud)
    print(stud)
    subject = stud.first()['subject'] # here we get the highest count of subject by using first method and assigned to subject
    sub=Subject.objects.get(name = stud.first()['subject']) #retrive the data from subject table related to lowest subject count in above query
    context ={'least fail count':{'subject':sub.name,'faculty':sub.faculty,'count':stud.first()['total']}}
    return JsonResponse(context) # returns a context in the form of json format in the webpage


"""Displays the each student total marks and display in json format"""
@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def sum(request):
    totalmarks= StudentMarks.objects.all().values('student_name') .annotate(total_marks=Sum('marks')) #retrive the student marks from the database and calculate the total marks of each student by using group_by method to student name and sum function
    print (list(totalmarks))
    context = {'totalmarks':list(totalmarks)} # here list is used to convert json format
    return JsonResponse(context)  #it renders  context and returns a json response and displays a json format in a webpage

""" 4th query :Displays STUDENT with highest Total"""
@api_view(['GET']) # @api_view is an rest_framework decorator and get is used to get the information
def maxtotal(request):
    totalmarks= StudentMarks.objects.all().values('student_name').annotate(total_marks=Sum('marks')).order_by('-total_marks')[:1] #retrive the data from database and calculate the each student total by using order_by and reverse methods we get the topper
    print (totalmarks)
    context = {'totalmarks':list(totalmarks)} # here list is used to convert json format
    return JsonResponse(context)  #it renders  context and returns a json response and displays a json format in a webpage


""" 7th query:Displays STUDENT with Least Total"""
@api_view(['GET'])  # @api_view is an rest_framework decorator and get is used to get the information
def mintotal(request):
    totalmarks= StudentMarks.objects.all().values('student_name').annotate(total_marks=Sum('marks')).order_by('total_marks')[:1] #retrive the data from database and calculate the each student total by using order_by method we get the student with less total
    print (totalmarks)
    context = {"max total with student":{'totalmarks':list(totalmarks)}} # here list is used to convert json format
    return JsonResponse(context)  #it renders  context and returns a json response and displays a json format in a webpage
