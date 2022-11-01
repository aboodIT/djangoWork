from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *


# class employeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all().order_by('name')
#     serializer_class = employeeSerializer

@api_view(['GET'])
def employeeList(request):
	tasks = Employee.objects.all()
	serializer = employeeSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def employeeDetail(request, pk):
	tasks = Employee.objects.get(empId=pk)
	serializer = employeeSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def employeeCreate(request):
	serializer = employeeSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def employeeUpdate(request, pk):
	task = Employee.objects.get(empId=pk)
	serializer = employeeSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def employeeDelete(request, pk):
	task = Employee.objects.get(id=pk)
	task.delete()

	return Response('Employee succsesfully delete!')



