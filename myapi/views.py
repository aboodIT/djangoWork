
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
    serializer = addEmployeeSerializer(data=request.data)

    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response(serializer.errors)
   


@api_view(['PUT'])
def employeeUpdate(request, pk):
    employee = Employee.objects.get(empId=pk)
    serializer = addEmployeeSerializer(instance=employee, data=request.data)

    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['DELETE'])
def employeeDelete(request, pk):
    employee = Employee.objects.get(empId=pk)
    employee.delete()

    return Response('Employee succsesfully delete!')

@api_view(['GET'])
def teamList(request):
    tasks = Team.objects.all()
    serializer = teamSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def teamDetail(request,pk):
    tasks = Team.objects.get(teamId = pk)
    serializer = teamSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def teamCreate(request):
    serializer = teamSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def teamUpdate(request):
    serializer = teamSerializer(data=request.data)

    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['DELETE'])
def teamDelete(request, pk):
    employee = Team.objects.get(teamId=pk)
    employee.delete()

    return Response('Team succsesfully deleted!')


@api_view(['GET'])
def workArrangementList(request):
    tasks = workArrangement.objects.all()
    serializer = workArrSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def workArrangementDetail(request, pk):
    tasks = workArrangement.objects.get(waId = pk)
    serializer = workArrSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def workArrangementCreate(request):
    serializer = workArrSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def workArrangementUpdate(request):
    serializer = workArrSerializer(data=request.data)

    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['DELETE'])
def workArrangementDelete(request, pk):
    employee = workArrangement.objects.get(teamId=pk)
    employee.delete()

    return Response('Arrangement succsesfully deleted!')


@api_view(['GET'])
def roleList(request):
    tasks = Role.objects.all()
    serializer = roleSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def roleDetail(request, pk):
    tasks = Role.objects.get(waId = pk)
    serializer = roleSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def roleCreate(request):
    serializer = roleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def roleUpdate(request):
    serializer = roleSerializer(data=request.data)

    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['DELETE'])
def roleDelete(request, pk):
    employee = Role.objects.get(teamId=pk)
    employee.delete()

    return Response('Arrangement succsesfully deleted!')





