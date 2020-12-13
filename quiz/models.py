from django.db import models

# Quiz models

class HSC_Quiz(models.Model):
    subject = models.CharField(max_length=50)
    chapter_name = models.CharField(max_length=50)
    chapter_no = models.CharField(max_length=2)
    question = models.CharField(max_length=300)
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)
    c = models.CharField(max_length=50)
    d = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    explanation = models.TextField(blank=True)

    def __str__(self):
        return self.subject + ' ' + self.chapter_no + ' : ' + self.question




'''    chapter_no = models.CharField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    caption = models.CharField(max_length=150)
    content = models.TextField()'''
