from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from .models import HSC_Quiz
import random

# Quiz views

def quiz(request):
    return render(request, 'quiz/home.html')

def hsc_quiz(request, sub, chap_no):
    raws = HSC_Quiz.objects.all()
    raw_list = []
    quiz_num = 20
    quizs = []
    exist = []
    answers_id = []
    subjects = {
        'biology1': 'জীব বিজ্ঞান ১ম পত্র',
        'biology2': 'জীব বিজ্ঞান ২য় পত্র'
    }

    if sub in subjects:
        subject = subjects[sub]
    else:
        subject = 'Unknown'

    for raw in raws:
        if raw.subject == sub and int(raw.chapter_no) == int(chap_no):
            raw_list.append(raw)

    if len(raw_list) < quiz_num:
        return render(request, 'quiz/quiz.html', {'message': 'এই বিষয় বা অধ্যয়ের যথেষ্ট প্রশ্ন আমাদের সার্ভারে নেই'})

    while len(quizs) + 1 <= quiz_num:
        mcq = random.choice(raw_list)
        if not mcq in exist:
            mcq.question = str(len(quizs) + 1) + '. ' + mcq.question
            #print(mcq.multiple_answer)
            quizs.append(mcq)
            exist.append(mcq)

    for x in quizs:
        answers_id.append(x.id)

    main_dic = {
                'quizs':quizs,
                'answers_id':answers_id,
                'subject':subject,
                'quiz_num': quiz_num,
                'each_quiz_time': 40,
                'total_time': str((quiz_num*40)%60) + ' min ' + str((quiz_num*40)%60) + ' sec',
            }
    return render(request, 'quiz/quiz.html', main_dic)


def quiz_result(request):
    subjects = {
        'biology1': 'জীব বিজ্ঞান ১ম পত্র',
        'biology2': 'জীব বিজ্ঞান ২য় পত্র'
    }

    if request.method == 'GET':
        return render(request, 'quiz/result.html', {'method':'This a GET method'})
    else:
        results = filter(request.POST)
        if len(results) < 1:
            message = 'You did not attand to the exam!!'
        else:
            message = 'Thank you for joining with us!!'

        sub = get_object_or_404(HSC_Quiz, pk=results[0][1])
        if sub.subject in subjects:
            subject = subjects[sub.subject]
        else:
            subject = 'Unknown'

        return render(request, 'quiz/result.html', {'results':results, 'message':message, 'subject':subject})

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
            serial_no += 1
            blank = False

    #print(results)
    return results

def ans_spliter(x):
	k, v = x.strip()[1:-2].split(':')
	v = v.split("'")[1]
	return [int(k[:-1]), v]
