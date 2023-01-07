from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset
from django.utils import timezone
from .admin import EmployeeResource
from .models import Employee,User
from django.utils.timezone import localtime
from datetime import datetime
from dateutil import tz



def UserCreated(request):
   user_data =  User.objects.all()
   user_time = User.objects.values_list('date_joined')
   from_zone = tz.tzutc()
   to_zone = tz.tzlocal()

   utc = datetime.strptime('2022-06-17 05:39:09', '%Y-%m-%d %H:%M:%S')

   utc = utc.replace(tzinfo=from_zone)

   # Convert to local time zone
   to_local_time = utc.astimezone(to_zone)

   print(utc,to_local_time)
   print('==============================================')
   print(user_time)
   context = {
      'user':user_data
   }
   # print(request.user.timezone)
   return render(request,'user.html',context)
