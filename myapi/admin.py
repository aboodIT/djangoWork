from pipes import Template
from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register([Employee,workArrangement,Team,payRoll,Role])
