from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=50,default='')
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Html2(models.Model):
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Quiz3(models.Model):
    name = models.CharField(max_length=50,default='')
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question


class Quiz4(models.Model):
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question


class Quiz5(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question



class Quiz6(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question


class Quiz7(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Quiz8(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Quiz9(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Quiz10(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question
class Quiz11(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Quiz12(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Quiz13(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question
class Quiz14(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Quiz15(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question
class Quiz16(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question
class Quiz17(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Quiz18(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question
class Quiz19(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question
class Quiz20(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length =200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

#Results Model

class Results(models.Model):
    username = models.CharField(max_length=50,null=True, blank=True)
    quizname = models.CharField(max_length=50,null=True, blank=True)
    score = models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username 
