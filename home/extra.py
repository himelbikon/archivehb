from .models import Visitor_History
import os


def visitor_log(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')

	#print(ip, '----------------------------------------')


	log = Visitor_History(ip=ip)
	log.save()

