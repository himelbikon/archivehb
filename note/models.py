from django.db import models

# Create your models here.
class HSC_Biology_1st_Note(models.Model):
    chapter_no = models.CharField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    caption = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.chapter_no + '. ' + self.chapter_name + ' : ' + self.caption
