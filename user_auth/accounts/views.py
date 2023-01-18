from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset
from django.utils import timezone
from .admin import EmployeeResource
from .models import Employee,User
from django.utils.timezone import localtime
from datetime import datetime
from dateutil import tz



def indexPage(request):
   users = User.objects.all()
   print(users)
   # request.COOKIES.get('timeZone')
   request.session['timeZone'] = request.COOKIES.get('timeZone')
   # request.COOKIES.get('timeZone')
   
   # print(request.session['timeZone'])
   print(request.COOKIES.get('timeZone'))
   context={
      'user':users

   }
   return render(request,'home.html',context)

def UserCreated(request):
   user_data =  User.objects.all()
   user_time = User.objects.values_list('date_joined',flat=True)
   while True:
      request.session['timeZone'] = request.COOKIES.get('timeZone')
      timezone = request.session['timeZone'] 
      context = {
         'user':user_data,
         'timeZone':timezone
      }
   # print(request.user.timezone)
      return render(request,'user.html',context)
