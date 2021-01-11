from django.db import models

# Create your models here.

class Visitor_History(models.Model):
    path = models.CharField(max_length=150)
