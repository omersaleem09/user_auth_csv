from django.core.management.base import BaseCommand
from django.utils import timezone
from quiz_app.models import *
class Command(BaseCommand):
     help = 'Displays current time'
     def handle(self, *args, **kwargs):
        quest = Question.objects.all()
        ans = Answer_Choice.objects.all()
        # print("quest",quest)
        # print("ans",ans)

        count = 0
        for i in quest:
            specfic_choice = Answer_Choice.objects.filter(question=i)
            for j in specfic_choice:
                j.order = count
                j.save()
                count+=2    