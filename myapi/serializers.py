from imp import source_from_cache
from os import set_inheritable
from django.template import context
from rest_framework import serializers

from .models import *

# class tSe(serializers.Serializer):
#     name =  serializers.CharField(max_length=200)
#     empId = serializers.IntegerField()
#     currTeam = serializers.CharField(max_length=200)
#     workArr =  serializers.CharField(max_length=200)
#     role = serializers.CharField(max_length=200)
#     rate = serializers.DecimalField(max_digits=5,decimal_places=2)
#     # pay = serializers.IntegerField()

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team

class payrollSerializer(serializers.Serializer):
    hours = serializers.IntegerField()
        
class employeeSerializer(serializers.ModelSerializer):

    currTeam = serializers.CharField()
    workArr = serializers.CharField()
    role = serializers.CharField()
    
    pay = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_pay(self,obj):
        hours= payrollSerializer(
            payRoll.objects.get(emp=obj.empId),
        )   
        pay = hours.data['hours']*obj.rate
        return pay
