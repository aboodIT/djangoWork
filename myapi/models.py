from pyexpat import model
from django.db import models

# Create your models here.

class Employee(models.Model):  
    name = models.CharField(max_length = 50)
    empId = models.AutoField(primary_key = True, auto_created = True)
    currTeam = models.ForeignKey('Team', on_delete = models.SET_NULL, blank = True, null = True)
    rate = models.DecimalField(max_digits = 5, decimal_places = 2)
    workArr = models.ForeignKey('workArrangement', on_delete = models.CASCADE, blank = True, null = True)
    role = models.ForeignKey('Role', on_delete = models.CASCADE, blank = True, null = True)

    def pay(self,hours):
        return self.rate*hours

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length = 50)
    teamId = models.AutoField(primary_key = True, auto_created = True)
    leader = models.ForeignKey('Employee', on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name

class workArrangement(models.Model):
    waID = models.AutoField(primary_key = True, auto_created = True)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class payRoll(models.Model):   #Model to record the hours the employee has worked
    emp = models.ForeignKey('Employee', on_delete = models.CASCADE, blank = True, null = True)
    hours = models.IntegerField()

    def __int__(self):
        return self.emp

class Role(models.Model):
    roleID = models.AutoField(primary_key = True, auto_created = True)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
