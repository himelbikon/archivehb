from django import template
from django.shortcuts import get_object_or_404
from quiz.models import HSC_Quiz

register = template.Library()

@register.filter
def result_shower(mcq):
	mcq_id = mcq[0]
	chosen_ans = mcq[1]
	obj = get_object_or_404(HSC_Quiz, pk=mcq_id)

	title = '<div>' + obj.question + '</div>'

	if obj.answer == obj.a:
		a = '<div class="right"> a) ' + obj.a + '</div>'
	elif obj.a == chosen_ans:
		a = '<div class="wrong"> a) ' + obj.a + '</div>'
	else:
		a = '<div> a) ' + obj.a + '</div>'

	if obj.answer == obj.b:
		b = '<div class="right"> b) ' + obj.b + '</div>'
	elif obj.b == chosen_ans:
		b = '<div class="wrong"> b) ' + obj.b + '</div>'
	else:
		b = '<div> b) ' + obj.b + '</div>'

	if obj.answer == obj.c:
		c = '<div class="right"> c) ' + obj.c + '</div>'
	elif obj.c == chosen_ans:
		c = '<div class="wrong"> c) ' + obj.c + '</div>'
	else:
		c = '<div> c) ' + obj.c + '</div>'

	if obj.answer == obj.d:
		d = '<div class="right"> d) ' + obj.d + '</div>'
	elif obj.d == chosen_ans:
		d = '<div class="wrong"> d) ' + obj.d + '</div>'
	else:
		d = '<div> d) ' + obj.d + '</div>'

	conclusion = '<div> Ans: <b>' + obj.answer + '</b>, you selected: <b>' + chosen_ans + '</b></div>'

	if obj.explanation != '':
		explanation = '<div> Explanation: ' + obj.explanation + '</div>'
	else:
		explanation = ''


	return title + a + b + c + d + conclusion + explanation

