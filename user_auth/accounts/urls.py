# myapp's urls.py
from django.urls import path
from . import views
from .views import indexPage

app_name = "accounts"

urlpatterns = [
    # path("", views.index, name="index"),
    path("",views.indexPage,name='home'),
    path("user/", views.UserCreated, name="user"),
    
]