from django.forms import ModelForm
from .models import Guest_Quiz, HSC_Quiz

class Guest_Quiz_Form(ModelForm):
    class Meta:
        model = Guest_Quiz
        fields = ['subject', 'chapter_no', 'question', 'a', 'b', 'c', 'd', 'answer', 'explanation']


class HSC_Quiz_Form(ModelForm):
    class Meta:
        model = HSC_Quiz
        fields = ['subject', 'chapter_no', 'stimulation', 'question', 'multiple_answer', 'a', 'b', 'c', 'd', 'answer', 'explanation']
