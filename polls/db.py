from .models import Choice, Question
from django.utils import timezone

def newpoll(name, option1, option2):
    q = Question(question_text=name,pub_date=timezone.now())
    q.save() 
    op1 = Choice(question = q, choice_text = option1)
    op2 = Choice(question = q, choice_text = option2)
    op1.save()
    op2.save()