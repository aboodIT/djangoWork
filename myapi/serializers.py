from contextlib import nullcontext
from imp import source_from_cache
from os import set_inheritable
from unicodedata import name
from django.template import context
from rest_framework import serializers

from .models import *

class tSe(serializers.Serializer):
    name =  serializers.CharField(max_length=200)
    empId = serializers.IntegerField()
    currTeam = serializers.CharField(max_length=200, required=False,allow_null=True)
    workArr =  serializers.CharField(max_length=200, allow_null=True)
    role = serializers.CharField(max_length=200, allow_null=True)
    rate = serializers.DecimalField(max_digits=5,decimal_places=2, required=False)
    # pay = serializers.IntegerField()

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class roleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class payrollSerializer(serializers.Serializer):
    hours = serializers.IntegerField()

class workArrSerializer(serializers.ModelSerializer):
    class Meta:
        model = workArrangement
        fields = '__all__'

class addEmployeeSerializer(serializers.ModelSerializer):

    # currTeam = teamSerializer()
    # role = roleSerializer()
    # role = serializers.CharField()
    
    class Meta:
        model = Employee
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.currTeam = validated_data.get('currTeam', instance.currTeam)
    #     instance.role = validated_data.get('role', instance.role)
    #     instance.work.Arr = validated_data.get('workArr', instance.workArr)
    #     instance.save()
    #     return instance

    
    
    # def get_role(self,obj):
    #     try:
    #         name = roleSerializer(
    #                 Role.objects.get(name=object.role),
    #         )   
    #         role = name.data['name']
    #     except:
    #         return ''
    #     return role

        
class employeeSerializer(serializers.ModelSerializer):

    currTeam = serializers.SlugRelatedField(read_only = True,slug_field='name')
    workArr = serializers.SlugRelatedField(read_only = True,slug_field='name')
    role = serializers.SlugRelatedField(read_only = True,slug_field='name')
    
    pay = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_pay(self,obj):
        try:
            hours= payrollSerializer(
                payRoll.objects.get(emp=obj.empId),
            )   
            pay = hours.data['hours']*obj.rate
        except:
            pay = ''
        return pay
