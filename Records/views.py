from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import halls
from . serializers import hallsSerializer
#from Records import serializers
#from rest_framework.decorators import api_view



class halls_list(APIView):
    def get(self,request):
      hall1=halls.objects.all()
      serializer=hallsSerializer(hall1,many = True)
      return  Response(serializer.data)

    def post(self,request):
        serializer = hallsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        serializer = hallsSerializer(halls, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   

    def delete(self):
        halls.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


