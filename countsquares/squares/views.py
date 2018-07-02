# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Square
from .serializers import SquareSerializer
from rest_framework import status





@api_view(['GET'])
def getsquare(request,_number):

    cal = Square.objects.filter(number=_number)
    print (list(cal))
    if cal:
        serializer = SquareSerializer(cal,many=True)
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

@api_view(['POST'])
def postnum(request):
    #if serializer = squareSerializer(data=request.data):

        number = request.dat.get("number",None)
        sqr = request.data.get("sqr",None)
        square = Square.objects.create(number=number,
                                         sqr=sqr)
        return Response({'message': 'square {:d} created'.format(square.id)}, status=301)
    #else:







@api_view(['GET', 'POST'])
def cal_list(request,_number):

    if request.method == 'GET':
        mul = square.objects.filter(number=_number)
        serializer = SquareSerializer(mul, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SquareSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            del serializer_data['number']
            return Response(serializer.data,{'message': 'square {:d} created'}, status= 301)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
