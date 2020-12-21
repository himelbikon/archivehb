from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('hsc/<str:sub>/chapter/<int:chap_no>/', views.hsc_quiz, name='hsc_quiz'),
    path('hsc/result/', views.quiz_result, name='quiz_result'),
]
