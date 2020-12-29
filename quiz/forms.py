from django.forms import ModelForm
from .models import Guest_Quiz

class Guest_Quiz_Form(ModelForm):
    class Meta:
        model = Guest_Quiz
        fields = ['subject', 'chapter_no', 'question', 'a', 'b', 'c', 'd', 'answer', 'explanation']




''' class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important'] '''
