from django.db import models
from ordered_model.models import OrderedModel
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Question(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name="Question Name")
    text = models.TextField()

    def __str__(self):
        return self.name

class Answer_Choice(OrderedModel):
    answer_choice = models.TextField()
    score = models.IntegerField()
    question = models.ForeignKey(Question, default=1, verbose_name="Category", on_delete=models.CASCADE)
    order_with_respect_to = 'question'

    class Meta:
        ordering = ('question', 'order')