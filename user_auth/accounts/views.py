from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset
from django.utils import timezone
from .admin import EmployeeResource
from .models import *
from django.utils.timezone import localtime
from datetime import datetime
from dateutil import tz
from django.views import View


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


class Certicate(View):
   def get(self,request):

      user_cert = User.objects.all().order_by('pk')
      context = {'user_cert':user_cert}

      # user_cert = User.objects.select_related('cert').all()
      # all_cert = Certificate.objects.all()
      # cert_data = request.GET.get('cert_data')
      # print(cert_data)
      # if cert_data is not None:
      #    val_cer = Certificate.objects.create(name=cert_data)
      #    val_cer.save()
      # print("DONE")
      # context = {
      #    'cert':'CERTIFICATE PAGE',
      #    'user_cert':user_cert,
      #    'all_cert':all_cert
      # }



      return render(request,'accounts/cert.html',context)