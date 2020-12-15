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

	a = '<div> a) ' + obj.a + '</div>'

	b = '<div> a) ' + obj.b + '</div>'

	c = '<div> a) ' + obj.c + '</div>'

	d = '<div> a) ' + obj.d + '</div>'

	return title + a + b + c + d