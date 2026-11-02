from django.shortcuts import render
from .models import Student
from. serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view()
def get_student(request, id):
    student = Student.objects.get(id = id)
    serializer = StudentSerializer(student)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view()
def list_student(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_student(request):
        serializer = StudentSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    
        else:
            serializer.errors
            
@api_view(['PUT','PATCH'])
def update_student(request,id):
    try:
        student = Student.objects.get(id=id)
    except:
        return Response({"Student not found"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = StudentSerializer(student, data = request.data, partial=True)
    else:    
        serializer = StudentSerializer(student, data = request.data)

    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:  
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student = Student.objects.get(id = id)
    except:
        return Response({"Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    student.delete()
    return Response({"delete successfully"}, status=status.HTTP_200_OK)
     
        