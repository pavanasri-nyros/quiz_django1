from django.db import models

# Create your models here.
class Quiz(models.Model):
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length = 200)
