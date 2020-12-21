from django.shortcuts import render
#from django.http import QueryDict
#from django.http import HttpResponse
from .models import HSC_Quiz
import random

# Quiz views

def quiz(request):
    return render(request, 'quiz/home.html')

def hsc_quiz(request, sub, chap_no):
    raws = HSC_Quiz.objects.all()
    raw_list = list(raws)
    quizs = []
    exist = []
    answers_id = []

    while len(quizs) + 1 <= 2:
        mcq = random.choice(raw_list)
        if not mcq in exist:
            mcq.question = str(len(quizs) + 1) + '. ' + mcq.question
            quizs.append(mcq)
            exist.append(mcq)

    for x in quizs:
        answers_id.append(x.id)

    return render(request, 'quiz/quiz.html', {'quizs':quizs, 'answers_id':answers_id})


def quiz_result(request):
    if request.method == 'GET':
        return render(request, 'quiz/result.html', {'method':'This a GET method'})
    else:
        results = filter(request.POST)
        if len(results) < 1:
            message = 'You did not attand to the exam!!'
        else:
            message = 'Thank you for joining with us!!'

        return render(request, 'quiz/result.html', {'results':results, 'message':message })

def filter(querydict):
    raw = str(querydict).split('answers_id')
    answers_id = eval(raw[-1].split("'")[2])
    answer_paper = list(map(ans_spliter, raw[0].split(',')[1:-1]))
    results = []
    serial_no = 1

    for x in answers_id:
    	for y in answer_paper:
    		if x == y[0]:
    			results.append([serial_no, x, y[1]])
    			serial_no += 1
    			break
    		else:
    			results.append([serial_no, x, 'No option'])
    			serial_no += 1
    			break
    return results

def ans_spliter(x):
	k, v = x.strip()[1:-2].split(':')
	v = v.split("'")[1]
	return [int(k[:-1]), v]
