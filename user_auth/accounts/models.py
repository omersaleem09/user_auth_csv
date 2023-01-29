from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

user_role_choices = (
    ("SuperUser","Super User"),
    ("StandardUser","Standar User")
)

class Certificate(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.name)

class User(AbstractUser):
    mobile_no = models.CharField(max_length=20,null=True,blank=True)
    cert = models.ManyToManyField(Certificate)

    def __str__(self):
        return str(self.username)

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    day_started = models.DateField()
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):

        return self.first_name+''+self.last_name


from datetime import date
class TimeTrack(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    @property
    def get_time(self):
        print("adasd")
        from datetime import timedelta
    
        a = self.start_date
        b = self.end_date

        if self.end_date is not None:
            time_difference = b - a
            print(time_difference/timedelta(1))
            return time_difference
