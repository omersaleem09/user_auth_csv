# myapp's urls.py
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # path("", views.index, name="index"),
    path("user/", views.UserCreated, name="user"),
]