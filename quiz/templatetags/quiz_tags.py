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

	title = '<div>' + str(serial_no) + '. ' + obj.question + '</div>'
	a = '<div> a) ' + obj.a + '</div>'
	b = '<div> b) ' + obj.b + '</div>'
	c = '<div> c) ' + obj.c + '</div>'
	d = '<div> d) ' + obj.d + '</div>'

	if obj.answer == obj.a:
		a = '<div class="right"> a) ' + obj.a + '</div>'
		chosen = 'a) ' + chosen_ans
	elif obj.a == chosen_ans:
		a = '<div class="wrong"> a) ' + obj.a + '</div>'
		chosen = 'a) ' + chosen_ans

	if obj.answer == obj.b:
		b = '<div class="right"> b) ' + obj.b + '</div>'
		chosen = 'b) ' + chosen_ans
	elif obj.b == chosen_ans:
		b = '<div class="wrong"> b) ' + obj.b + '</div>'
		chosen = 'b) ' + chosen_ans

	if obj.answer == obj.c:
		c = '<div class="right"> c) ' + obj.c + '</div>'
		chosen = 'c) ' + chosen_ans
	elif obj.c == chosen_ans:
		c = '<div class="wrong"> c) ' + obj.c + '</div>'
		chosen = 'c) ' + chosen_ans

	if obj.answer == obj.d:
		d = '<div class="right"> d) ' + obj.d + '</div>'
		chosen = 'd) ' + chosen_ans
	elif obj.d == chosen_ans:
		d = '<div class="wrong"> d) ' + obj.d + '</div>'
		chosen = 'd) ' + chosen_ans

	if chosen_ans != 'No option':
		chosen_ans = chosen

	conclusion = '<div> Ans: <b>' + obj.answer + '</b>, you have selected: <b>' + chosen_ans + '</b></div>'

	if obj.explanation != '':
		explanation = '<div> Explanation: ' + obj.explanation + '</div>'
	else:
		explanation = ''


	return title + a + b + c + d + conclusion + explanation
