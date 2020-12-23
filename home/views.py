from django.shortcuts import render
from quiz.models import HSC_Quiz
import random
#from django.http import HttpResponse

# home views

def home(request):
    all_obj = HSC_Quiz.objects.all()
    obj = random.choice(all_obj)
    ten_obj = []
    exist = []

    while len(ten_obj) < 10:
        obj = random.choice(all_obj)
        #print(len(ten_obj))
        if len(obj.a + obj.b + obj.c + obj.d) < 200 and len(obj.multiple_answer) < 3 and len(obj.stimulation) < 1:
            if not obj in exist:
                ten_obj.append(obj)
                exist.append(obj)

    return render(request, 'home/home.html', {'ten_obj':ten_obj})
