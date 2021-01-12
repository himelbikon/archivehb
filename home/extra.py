from .models import Visitor_History


def visitor_log(request):
	path = 'URL---> ' + str(request).split("'")[1]

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')

	#print(ip, '----------------------------------------')


	log = Visitor_History(path=path, ip=ip)
	log.save()

