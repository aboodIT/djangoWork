from contextlib import nullcontext
from imp import source_from_cache
from os import set_inheritable
from pickletools import read_floatnl, read_long1
from unicodedata import name
from django.template import context
from rest_framework import serializers

from .models import *

class teamSerializer(serializers.ModelSerializer):

    leader = serializers.SlugRelatedField(read_only = True, slug_field='name')

    class Meta:
        model = Team
        fields = '__all__'

class roleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class payrollSerializer(serializers.Serializer):
    class Meta:
        model = payRoll
        field = "__all__"
class workArrSerializer(serializers.ModelSerializer):
    class Meta:
        model = workArrangement
        fields = '__all__'

class addEmployeeSerializer(serializers.ModelSerializer):

    # currTeam = serializers.SlugRelatedField(read_only = True,slug_field='name')
    # workArr = serializers.SlugRelatedField(read_only = True,slug_field='name')
    # role = serializers.SlugRelatedField(read_only = True,slug_field='name')
  
    class Meta:
        model = Employee
        fields = '__all__'
        
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
            hours = payRoll.objects.get(emp=obj.empId).hours
            if(obj.role.name == "Leader"):
                pay = "%.2f" % (float(obj.rate)*hours*1.1)
            else:
                pay = "%.2f" % (float(obj.rate)*hours)
        except:
            pay = ''
        return pay
