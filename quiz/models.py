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


class Html3(models.Model):
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


class Html4(models.Model):
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


class Html5(models.Model):
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



class Css1(models.Model):
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


class Css2(models.Model):
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

class Css3(models.Model):
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

class Css4(models.Model):
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

class Css5(models.Model):
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

#javascript
class Js1(models.Model):
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
class Js2(models.Model):
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

class Js3(models.Model):
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
class Js4(models.Model):
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

class Js5(models.Model):
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

#Django
class Django1(models.Model):
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

class Django2(models.Model):
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

class Django3(models.Model):
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
class Django4(models.Model):
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

class Django5(models.Model):
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



#VueJs
class Vue1(models.Model):
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
class Vue2(models.Model):
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

class Vue3(models.Model):
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
class Vue4(models.Model):
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

class Vue5(models.Model):
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
    username = models.CharField(max_length=50,default='')
    quizname = models.CharField(max_length=50, default='Quiz')
    score = models.IntegerField()

    def __str__(self):
        return self.username
