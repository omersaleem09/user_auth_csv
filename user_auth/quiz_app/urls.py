# urls.py
from django.urls import re_path as url


from . import views


app_name = 'quiz_app'

urlpatterns = [
    url("quiz_page", views.QuestionView.as_view(),name='quiz-page'),  
    ]