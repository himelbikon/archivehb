from django.shortcuts import render, redirect
from quiz.models import HSC_Quiz
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm   #UserCreationForm
import random
#from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponse

# home views

def home(request):
    all_obj = HSC_Quiz.objects.all()
    obj = random.choice(all_obj)
    ten_obj = []
    exist = []

    while len(ten_obj) < 10:
        obj = random.choice(all_obj)
        #print(len(ten_obj))
        if len(obj.a + obj.b + obj.c + obj.d) < 200 and len(obj.multiple_answer) < 3 and len(obj.stimulation) < 1:
            if not obj in exist:
                ten_obj.append(obj)
                exist.append(obj)

    return render(request, 'home/home.html', {'ten_obj':ten_obj})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'home/login.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home/login.html', {'form': AuthenticationForm(), 'message': 'Username or Password is incorrect'})
        else:
            login(request, user)
            return redirect('home')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'home/signup.html') #, {'form': UserCreationForm()})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
