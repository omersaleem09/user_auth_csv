# myapp's urls.py
from django.urls import path
from . import views
from .views import indexPage

app_name = "accounts"

urlpatterns = [
    # path("", views.index, name="index"),
    path("",views.indexPage,name='home'),
    path("user/", views.UserCreated, name="user"),
    path("cert-page",views.Certicate.as_view(),name='cert-page')
]

# urls.py
# from django.urls import re_path as url


# from . import views


# app_name = 'quiz_app'

# urlpatterns = [
#     url("quiz_page", views.QuestionView.as_view(),name='quiz-page'),  
#     ]