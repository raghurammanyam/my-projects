# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import square
from .serializers import squareSerializer





@api_view(['GET'])
def getsquare(request,_number):

    cal = square.objects.filter(number=_number)
    print (list(cal))
    if cal:
        serializer = squareSerializer(cal,many=True)
        return Response(serializer.data)
    else:
        return Response("number not found")



@api_view(['POST'])
def postnum(request):

        serializer = squareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
        serializer = squareSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    number = request.POST.get("number",None)
    sqr = request.POST.get("sqr",None)
    square = square.objects.create(number=number,
                                     sqr=sqr)
    return Response({'message': 'square {:d} created'.format(square.id)}, status=301)"""
