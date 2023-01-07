# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Employee
# from .forms import MyUserCreationForm, MyUserChangeForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    print(ImportExportModelAdmin)
    pass

admin.site.register(User)
