from django.forms import ModelForm
from home.models import Visitor_History

class VH_Form(ModelForm):
    class Meta:
        model = Visitor_History
        fields = ['path']
