from django import template

register = template.Library()

@register.filter
def js_list(ten_obj):
	arr = []
	for x in ten_obj:
		question = x.question + ' <br>'
		a = 'a) ' + x.a + '&nbsp'*3
		b = 'b) ' + x.b + ' <br>'
		c = 'c) ' + x.c + '&nbsp'*3
		d = 'd) ' + x.d + ' <br>'
		answer = 'সঠিক উত্তর: ' + x.answer + ' <br>'

		if len(x.explanation) < 2:
			explanation = ' '*150
		else:
			explanation = 'ব্যাখ্যা: ' + x.explanation[0:100] + '.....' + ' '*150

		arr.append(question + a + b + c + d + answer + explanation)
	return 'var arr = ' + str(arr) + ';'
