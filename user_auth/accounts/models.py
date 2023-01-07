from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

user_role_choices = (
    ("SuperUser","Super User"),
    ("StandardUser","Standar User")
)

class User(AbstractUser):
    mobile_no = models.CharField(max_length=20,null=True,blank=True)

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    day_started = models.DateField()
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):

        return self.first_name+''+self.last_name