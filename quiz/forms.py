from django.forms import ModelForm
from .models import HSC_Quiz


class HSC_Quiz_Form(ModelForm):
    class Meta:
        model = HSC_Quiz
        fields = ['subject', 'chapter_no', 'stimulation', 'question', 'multiple_answer', 'a', 'b', 'c', 'd', 'answer', 'explanation']
