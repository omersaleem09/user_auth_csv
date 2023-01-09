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
   user_time = User.objects.values_list('date_joined',flat=True)
   request.session['timeZone'] = request.COOKIES.get('timeZone')
   timezone = request.session['timeZone'] 
   context = {
      'user':user_data,
      'timeZone':timezone
   }
   # print(request.user.timezone)
   return render(request,'user.html',context)
