from django.shortcuts import render
from quiz.models import HSC_Quiz
#from django.http import HttpResponse

# home views

def home(request):
    ten_obj = HSC_Quiz.objects.all()
    return render(request, 'home/home.html', {'ten_obj':ten_obj})
