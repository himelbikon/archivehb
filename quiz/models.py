from django.db import models

# Quiz models

class HSC_Quiz(models.Model):
    subject = models.CharField(max_length=50)
    chapter_name = models.CharField(max_length=50, blank=True)
    chapters = (('০১', '০১'), ('০২', '০২'), ('০৩', '০৩'), ('০৪', '০৪'), ('০৫', '০৫'),
    ('০৬', '০৬'), ('০৭', '০৭'), ('০৮', '০৮'), ('০৯', '০৯'), ('১০', '১০'), ('১১', '১১'), ('১২', '১২'))
    chapter_no = models.CharField(max_length=2, blank=True, choices=chapters)
    stimulation = models.TextField(blank=True)
    question = models.CharField(max_length=400)
    multiple_answer = models.TextField(blank=True)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explanation = models.TextField(blank=True)

    def __str__(self):
        return self.subject + ' ' + self.chapter_no + ' : ' + self.question


class Subject(models.Model):
    code_name = models.CharField(max_length=50)
    formal_name = models.CharField(max_length=50)
    chap_names = models.TextField(blank=True)

    def __str__(self):
        return self.code_name
