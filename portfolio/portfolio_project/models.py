from importlib.resources import path
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)        # CharField used for short strings
    url = models.CharField(max_length=100)          
    description = models.TextField()                # TextField used for long strings
    technology = models.CharField(max_length=40)    
    image = models.FilePathField(path="/img")       # FileImageField points to a file path name