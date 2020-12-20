from django.shortcuts import render
#from django.http import QueryDict
#from django.http import HttpResponse
from .models import HSC_Quiz
import re

# Quiz views

def quiz(request):
    return render(request, 'quiz/home.html')

def hsc_quiz(request, sub, chap_no):
    quizs = HSC_Quiz.objects.all()
    return render(request, 'quiz/quiz.html', {'quizs':quizs})

def quiz_result(request):
    if request.method == 'GET':
        quizs = HSC_Quiz.object.all()
        return render(request, 'quiz/result.html', {'method':'This a GET method', 'quizs':quizs})
    else:
        results = querydict_to_pylist(request.POST)
        #print(results)
        return render(request, 'quiz/result.html', {'results':results})

def querydict_to_pylist(querydict):
    split = str(querydict).split(',')
    size = split[1:]
    strip = list(map(lambda x: x.strip(), size))
    strip[-1] = strip[-1][0:-2]
    final_list = list(map(list_maker, strip))
    return final_list

def list_maker(x):
    arr = []
    k, h = x.split(':')
    k, h = int(k.strip()[1:-1]), h.strip()[2:-2]
    arr.append(k)
    arr.append(h)
    return arr
