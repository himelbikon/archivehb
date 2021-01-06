from django import template
from django.shortcuts import get_object_or_404
from quiz.models import HSC_Quiz

register = template.Library()

@register.filter
def result_shower(mcq):
	serial_no = mcq[0]
	mcq_id = mcq[1]
	chosen_ans = mcq[2]
	obj = get_object_or_404(HSC_Quiz, pk=mcq_id)
	answer = obj.answer

	title = '<div>' + str(serial_no) + '. ' + obj.question + '</div>'
	multiple_answer = '<div>' + obj.multiple_answer + '</div>'
	a = '<div> a) ' + obj.a + '</div>'
	b = '<div> b) ' + obj.b + '</div>'
	c = '<div> c) ' + obj.c + '</div>'
	d = '<div> d) ' + obj.d + '</div>'

	if answer == obj.a:
		a = '<div class="answer"> a) ' + obj.a + ' </div>'
	elif answer == obj.b:
		b = '<div class="answer"> b) ' + obj.b + ' </div>'
	elif answer == obj.c:
		c = '<div class="answer"> c) ' + obj.c + ' </div>'
	elif answer == obj.d:
		d = '<div class="answer"> d) ' + obj.d + ' </div>'

	if answer == obj.a and chosen_ans == obj.a:
		a = '<div class="right"> a) ' + obj.a + ' </div>'
	elif answer == obj.b and chosen_ans == obj.b:
		b = '<div class="right"> b) ' + obj.b + ' </div>'
	elif answer == obj.c and chosen_ans == obj.c:
		c = '<div class="right"> c) ' + obj.c + ' </div>'
	elif answer == obj.d and chosen_ans == obj.d:
		d = '<div class="right"> d) ' + obj.d + ' </div>'

	if answer != obj.a and chosen_ans == obj.a:
		a = '<div class="wrong"> a) ' + obj.a + ' </div>'
	elif answer != obj.b and chosen_ans == obj.b:
		b = '<div class="wrong"> b) ' + obj.b + ' </div>'
	elif answer != obj.c and chosen_ans == obj.c:
		c = '<div class="wrong"> c) ' + obj.c + ' </div>'
	elif answer != obj.d and chosen_ans == obj.d:
		d = '<div class="wrong"> d) ' + obj.d + ' </div>'


	conclusion = '<div> Ans: <b>' + answer + '</b>, you have selected: <b>' + chosen_ans + '</b></div>'

	if obj.explanation != '':
		explanation = '<div> Explanation: ' + obj.explanation + '</div>'
	else:
		explanation = ''


	return title + multiple_answer + a + b + c + d + conclusion + explanation


@register.filter
def quizs_table(chapters):
	chapter_no = '<tr> '
	quiz_num = '<tr> '
	for key in chapters:
		chapter_no += '<td>' + str(key) + '</td>'
		quiz_num += '<td>' + str(chapters[key]) + '</td>'

	chapter_no += '</tr>'
	quiz_num += '</tr>'
	return chapter_no + quiz_num
