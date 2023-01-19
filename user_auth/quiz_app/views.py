from django.shortcuts import render
from django.db.models import Prefetch

# Create your views here.
from quiz_app.models import *
from django.views import View

class QuestionView(View):
    def get(self,request):
        question_category_qs = Question.objects.prefetch_related('answer_choice_set').filter(pk=1)
        print('qqqqqqq',question_category_qs)
        print(Answer_Choice.objects.get(pk=1))
        print(Answer_Choice.objects.all())
        print('orderBY',Answer_Choice.objects.all().order_by('order'))

        print('----->',Question.objects.prefetch_related(Prefetch('answer_choice_set', queryset=Answer_Choice.objects.order_by('order'), to_attr='rgs')).all())

        context = {'a':Question.objects.prefetch_related(Prefetch('answer_choice_set', queryset=Answer_Choice.objects.order_by('order'))).all()}
        
    
        return render(request,"quest.html",context)