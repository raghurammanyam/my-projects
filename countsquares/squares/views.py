# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import square
from .serializers import squareSerializer
from rest_framework import status
import MySQLdb

HOST = 'localhost'
USER = 'ram'
PASSWORD = 'Raghuram@9'
DATABASE = 'count'


@api_view(['GET'])
def getsquare(request,_number):

    cal = square.objects.filter(number=_number)
    print (list(cal))
    if cal:
        serializer = squareSerializer(cal,many=True)
        return Response(serializer.data)
    else:
        _sq = int(_number) * int(_number)
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('INSERT INTO  squares_square (number, sqr) values(%s, %s)',(float(_number),float(_sq)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': "New number inserted", 'Number': _number, 'Square': _sq})



@api_view(['GET'])
def comp(request, _values):
    _number, _sq = _values.split('-')
    _stat = square.objects.filter(number = _number)
    if _stat:
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('UPDATE squares_square  SET sqr = %s WHERE number = %s',(float(_sq),float(_number)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': 'Square of the given number is updated', 'Number': _number, 'Square': _sq})
    else:
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('INSERT INTO squares_square (number, sqr) values(%s, %s)',(float(_number),float(_sq)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': 'New number and square inserted', 'Number': _number, 'Square': _sq})



@api_view(['POST'])
def postnum(request):
    #if serializer = squareSerializer(data=request.data):

        number = request.POST.get("number",None)
        sqr = request.POST.get("sqr",None)
        square = square.objects.create(number=number,
                                         sqr=sqr)
        return Response({'message': 'square {:d} created'.format(square.id)}, status=301)
    #else:







@api_view(['GET', 'POST'])
def cal_list(request,_number):

    if request.method == 'GET':
        mul = square.objects.filter(number=_number)
        serializer = squareSerializer(mul, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = squareSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            del serializer_data['number']
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
