from django import template

register = template.Library()

@register.filter
def js_list(ten_obj):
	arr = []
	for x in ten_obj:
		question = x.question + ' <br>'
		a = 'a) ' + x.a + '&nbsp'*3
		b = 'b) ' + x.b + '&nbsp'*3
		c = 'c) ' + x.c + '&nbsp'*3
		d = 'd) ' + x.d + ' <br>'
		answer = 'Answer: ' + x.answer + ' <br>'
		explanation = 'Explanation: ' + x.explanation[0:100] + '.....' + ' '*50
		arr.append(question + a + b + c + d + answer + explanation)
	return 'var arr = ' + str(arr) + ';'
