from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import HSC_Quiz, Subject
from .forms import HSC_Quiz_Form
from django.contrib.auth.decorators import login_required
from home.extra import visitor_log
from threading import Thread
from collections import defaultdict
import random, re

# Quiz views

def quiz(request):
    visitors(request)
    return render(request, 'quiz/home.html')

def admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'GET':
            quizs = HSC_Quiz.objects.all()
            quizs = list(quizs)
            subjects = Subject.objects.all()
            tem_list = []
            total = len(quizs)
            count_dic = defaultdict(int)
            all_subs = set()

            for subject in subjects:
                for quiz in quizs:
                    if quiz.subject == subject.code_name:
                        count_dic[quiz.subject] += 1
                        if quiz.chapter_no == '':
                            count_dic[quiz.chapter_name] += 1
                        else:
                            count_dic[quiz.chapter_no] += 1

                    all_subs.add(quiz.subject)

                tem_list.append(dict(sorted(count_dic.copy().items())))
                count_dic.clear()

            visitors(request)
            return render(request, 'quiz/admin.html', {'total': total, 'tem_list': tem_list, 'all_subs': all_subs})
    else:
        visitors(request)
        return redirect('loginuser')

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
        visitors(request)
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
    visitors(request)
    return render(request, 'quiz/quiz.html', main_dic)


def quiz_result(request):
    subjects = {
        'biology1': 'জীব বিজ্ঞান ১ম পত্র',
        'biology2': 'জীব বিজ্ঞান ২য় পত্র'
    }
    right = 0
    wrong = 0
    blank = 0

    if request.method == 'GET':
        visitors(request)
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

        mcq_num = len(results)
        for res in results:
            cho_ans = res[2]
            ans = get_object_or_404(HSC_Quiz, pk=res[1]).answer

            if cho_ans == ans:
                right += 1
            elif cho_ans == 'No option':
                blank += 1
            else:
                wrong += 1

        main_dic = {'results':results,
                    'message':message,
                    'subject':subject,
                    'mcq_num':mcq_num,
                    'right' : right,
                    'wrong': wrong,
                    'blank': blank,
                }
        visitors(request)
        return render(request, 'quiz/result.html', main_dic)

def filter(querydict):
    #print(querydict)
    string = str(querydict)
    dic = re.findall("{.*}", string)
    ans_dic = eval(*dic)
    ans_dic.pop('csrfmiddlewaretoken')

    answer_ids = eval(*ans_dic['answers_id'])
    ans_dic.pop('answers_id')

    mcq_ids = []
    for ans in ans_dic:
        mcq_ids.append([int(ans), *ans_dic[ans]])

    #print(answer_ids, mcq_ids, '--------------------------------------------------------------------')
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

@login_required
def hsc_add(request):
    if request.method == 'GET':
        visitors(request)
        return render(request, 'quiz/hscadd.html', {'form': HSC_Quiz_Form()})
    elif request.method == 'POST':
        hsc_quiz = HSC_Quiz_Form(request.POST)
        hsc_quiz.save()
        visitors(request)
        return redirect('quiz:hsc_add')

def visitors(request):
    extra = Thread(target=lambda: visitor_log(request))
    extra.start()
