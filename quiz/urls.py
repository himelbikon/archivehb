from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('admin/', views.admin, name='admin'),
    path('hsc/result/', views.quiz_result, name='quiz_result'),
    path('hsc/add/', views.hsc_add, name='hsc_add'),
    path('hsc/<str:sub>/chapter/<chap_no>/', views.hsc_quiz, name='hsc_quiz'),
]
