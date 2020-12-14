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
        result = querydict_to_pythondict(request.POST)
        #print(result)
        return render(request, 'quiz/result.html', {'method':result})

def querydict_to_pythondict(querydict):

    split = str(querydict).split(',')
    size = split[1:]
    strip = list(map(lambda x: x.strip(), size))
    strip[-1] = strip[-1][0:-2]

    for a in strip:
        print(a)

    return strip
