from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.note, name='note'),
    path('hsc/<str:sub>/chap<int:chap_no>/', views.hsc_note, name='hsc_note'),
]
