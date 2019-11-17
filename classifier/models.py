from django.db import models
import os
# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('cell', ext)
    return os.path.join(upload_to, filename)

class Classifier(models.Model):
    image = models.ImageField(upload_to=path_and_rename, default='images/None/no-img.jpg')
    category = models.CharField(max_length=3)