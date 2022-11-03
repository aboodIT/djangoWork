import pdb
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.shortcuts import render, get_object_or_404

@api_view(['GET'])
def employeeList(request):
    tasks = Employee.objects.all()
    serializer = employeeSerializer(tasks, many=True)
    return Response(serializer.data,  status=status.HTTP_200_OK)


@api_view(['GET'])
def employeeDetail(request, pk):
    tasks = get_object_or_404(Employee, empId=pk)
    serializer = employeeSerializer(tasks, many=False)
    return Response(serializer.data,  status=status.HTTP_200_OK)


@api_view(['POST'])
def employeeCreate(request):

    currTeam = request.data['currTeam']
    role = request.data['role']
    name = request.data['name']
    workArr = request.data['workArr']
    if(role.lower() =='leader'):
        try:
            team = Team.objects.get(name = currTeam)
            if(team.leader.name == name):
                pass
            else:
                return Response("Team already has a leader",status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("Team " + currTeam + " does not exist", status=status.HTTP_404_NOT_FOUND)
    try:
        if(currTeam==''):pass
        else:
            team = Team.objects.get(name = currTeam)
            request.data["currTeam"] = team.teamId
    except:
        if(currTeam != None):
            return Response("Team: " + currTeam + "does not exist", status=status.HTTP_404_NOT_FOUND)
    
    try:
        if(role==''):pass
        else:
            role = Role.objects.get(name = role)
            request.data['role'] = role.roleID
    except:
        if(role != None):
            return Response("Role: " + role.name + "does not exist",status=status.HTTP_404_NOT_FOUND)

    try:
        if(workArr == ''): pass
        else:
            workArr = workArrangement.objects.get(name = workArr)
            request.data['workArr'] = workArr.waID
    except:
        if(workArr != None):
            return Response("Work Arrangement: " + workArr.name + "does not exist",status=status.HTTP_404_NOT_FOUND)
    

  
    serializer = addEmployeeSerializer(data=request.data)


    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)

    return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
   


@api_view(['PUT'])
def employeeUpdate(request, pk):
    employee = Employee.objects.get(empId=pk)
    
    currTeam = request.data['currTeam']
    role = request.data['role']
    name = request.data['name']
    workArr = request.data['workArr']
    if(role.lower() =='Leader'):
        try:
            team = Team.objects.get(name = currTeam)
            if(team.leader.name == name):
                pass
            else:
                return Response("Team already has a leader", status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("Team" + currTeam + " does not exist", status=status.HTTP_404_NOT_FOUND)
    try:
        if(currTeam == ''): pass
        else:
            team = Team.objects.get(name = currTeam)
            request.data['currTeam'] = team.teamId
    except:
        if(currTeam != None ):

            return Response("Team: " + currTeam + " does not exist", status=status.HTTP_404_NOT_FOUND)
    
    try:
        if(role==''): pass
        else:
            role = Role.objects.get(name = role)
            request.data['role'] = role.roleID
    except:
        if(role != None):
            return Response("Role: " + role + "does not exist", status=status.HTTP_404_NOT_FOUND)

    try:
        if(workArr == ''): pass
        else:
            workArr = workArrangement.objects.get(name = workArr)
            request.data['workArr'] = workArr.waID
    except:
        if(workArr != None):
            return Response("Work Arrangement: " + workArr.name + "does not exist", status=status.HTTP_404_NOT_FOUND)
    serializer = addEmployeeSerializer(instance=employee, data=request.data)


    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def employeeDelete(request, pk):
    try:
        employee = get_object_or_404(Employee, empId=pk)
        employee.delete()
        return Response('Employee succsesfully delete!')
    except:
        return Response("Employee does not exist", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def teamList(request):
    tasks = Team.objects.all()
    serializer = teamSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def teamDetail(request,pk):
    tasks = get_object_or_404(Team, teamId=pk)
    serializer = teamSerializer(tasks, many=True)
    return Response(serializer.data,  status=status.HTTP_200_OK)


@api_view(['POST'])
def teamCreate(request):
    leader = request.data['leader']
    try:
        if(leader == ''):
            pass
        else:
            leader = Employee.objects.get(name = leader)
            request.data['leader'] = leader
    except:
        return Response("Employee "+leader+"does not exist", status=status.HTTP_404_NOT_FOUND)

    serializer = addTeamSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,  status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def teamUpdate(request,pk):
    team = Team.objects.get(teamId=pk)
    leader = request.data['leader']
    try:
        if(leader == ''):
            pass
        else:
            leader = Employee.objects.get(name = leader)
            team.leader = leader
    except:
        return Response("Employee "+leader+"does not exist", status=status.HTTP_400_BAD_REQUEST)

    serializer = addTeamSerializer(instance=team, data=request.data)

    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def teamDelete(request, pk):
    try:
        team = get_object_or_404(Team, teamId=pk)
        team.delete()

        return Response('Team succsesfully deleted!',  status=status.HTTP_200_OK)
    except:
        return Response("Team does not exist", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','POST'])
def get_Post_workArrangement(request):
    if(request.method == 'GET'):
        tasks = workArrangement.objects.all()
        serializer = workArrSerializer(tasks, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    
    if(request.method == 'POST'):
        serializer = workArrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','DELETE','PUT'])
def get_Delete_Update_workArrangement(request, pk):
    if request.method == 'GET':
        workArr = get_object_or_404(workArrangement, waID=pk)
        serializer = workArrSerializer(workArr)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        try:
            workArr = workArrangement.objects.get(waID=pk)
            workArr.delete()
            return Response('Work arrangement succsesfully deleted!')
        except:
             Response("Arrangment does not exist", status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        workArr = get_object_or_404(workArrangement, waID=pk)
        serializer = workArrSerializer(instance=workArr, data=request.data)

        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,  status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def get_Post_role(request):
    #Get all roles
    if request.method == 'GET':                 
        tasks = Role.objects.all()
        serializer = roleSerializer(tasks, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = roleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','DELETE','PUT'])
def get_Delete_Update_Role(request, pk):
    if request.method == 'GET':
        role = get_object_or_404(Role, roleID=pk)
        serializer = roleSerializer(role)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        try:
            role = Role.objects.get(roleID=pk)
            role.delete()
            return Response('Role succsesfully deleted!')
        except:
             Response("Role does not exist", status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        role = get_object_or_404(Role, roleID=pk)
        serializer = roleSerializer(instance=role, data=request.data)

        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,  status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def get_Post_Hours(request):
    #Get all roles
    if request.method == 'GET':                 
        hours = payRoll.objects.all()
        serializer = payRollSerializer(hours, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    if request.method == 'POST':
        get_object_or_404(Employee,empId=request.data['emp'])
        serializer = payRollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','DELETE','PUT'])
def get_Delete_Update_Hours(request, pk):
    if request.method == 'GET':
        hours = get_object_or_404(payRoll,emp=pk)
        serializer = payRollSerializer(hours)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        try:
            hours = payRoll.objects.get(emp=pk)
            hours.delete()
            return Response('Hours succsesfully deleted!')
        except:
            return Response("Payroll does not exist", status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        hours = payRoll.objects.get(emp=pk)
        serializer = payRollSerializer(instance=hours, data=request.data)

        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,  status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)









