from .models import Choice, Question
from django.utils import timezone

def newpoll(name, option1, option2):
    print(name)
    print(option1)
    print(option2)
    q = Question(question_text=name,pub_date=timezone.now())
    q.save()
    print(1) 
    op1 = Choice(question = q, choice_text = option1)
    print(2)
    op2 = Choice(question = q, choice_text = option2)
    print(3)
    op1.save()
    print(4)
    op2.save()
    print(5)