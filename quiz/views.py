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
    quiz_num = 20

    while len(quizs) + 1 <= quiz_num:
        mcq = random.choice(raw_list)
        if not mcq in exist:
            mcq.question = str(len(quizs) + 1) + '. ' + mcq.question
            #print(mcq.multiple_answer)
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

        #print(results)
        return render(request, 'quiz/result.html', {'results':results, 'message':message })

def filter(querydict):
    raw = str(querydict).split('answers_id')
    answer_ids = eval(raw[-1].split("'")[2])
    mcq_ids = list(map(ans_spliter, raw[0].split(',')[1:-1]))
    results = []
    serial_no = 1

    for ans_id in answer_ids:
    	blank = True
    	for mcq_id in mcq_ids:

    		if mcq_id[0] == ans_id:
    			results.append([serial_no, ans_id, mcq_id[1]])
    			serial_no += 1
    			blank = False

    	if blank:
    		results.append([serial_no, ans_id, 'No option'])
    		blank = False

    #print(results)
    return results

def ans_spliter(x):
	k, v = x.strip()[1:-2].split(':')
	v = v.split("'")[1]
	return [int(k[:-1]), v]
