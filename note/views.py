from django.shortcuts import render
from .models import HSC_Biology_1st_Note

# Create your views here.

def note(request):
    return render(request, 'note/note.html')

def hsc_note(request, sub, chap_no):
    dictionary = {}

    if sub == 'bio1':
        notes = HSC_Biology_1st_Note.objects.all()
        tem_list = []
        for note in notes:
            if int(note.chapter_no) == chap_no:
                tem_list.append(note)

        if len(tem_list) > 0:
            dictionary['notes'] = tem_list
        else:
            dictionary['error'] = 'Chapter is not available'
    else:
        dictionary['error'] = 'Subject is not available'

    return render(request, 'note/chap.html', dictionary)
