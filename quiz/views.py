from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .models import Quiz, Html2, Html3, Html4, Html5,Results
from .models import Css1,Css2, Css3, Css4, Css5
from .models import Js1,Js2,Js3,Js4,Js5
from .models import Django1, Django2,Django3,Django4,Django5
from .models import Vue1,Vue2,Vue3, Vue4, Vue5
from rest_framework import generics
from .serializers import QuizSerializers, Html2Serializers, Html3Serializers, Html4Serializers, Html5Serializers
from .serializers import Css1Serializers, Css2Serializers, Css3Serializers, Css4Serializers, Css5Serializers
from .serializers import Js1Serializers, Js2Serializers, Js3Serializers, Js4Serializers, Js5Serializers
from .serializers import Django1Serializers,Django2Serializers,Django3Serializers,Django4Serializers,Django5Serializers
from .serializers import Vue1Serializers,Vue2Serializers,Vue3Serializers,Vue4Serializers,Vue5Serializers
from django.contrib.auth.decorators import  login_required
from django.http import HttpResponse
from .forms import Score
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    return render(request, 'quiz/home.html')

@login_required
@csrf_exempt
def score(request):
    if request.method == 'GET':
        return render(request, 'quiz/html/end.html',{'form':Score()})
    else:
        try:
            form = Score(data=request.POST)
            newscore = form.save(commit=False)
            newscore.owner = request.user
            newscore.save()
            return redirect('category')
        except ValueError:
            return render(request, 'quiz/html/end.html',{'form':Score(), 'error' :'please fill the form properly'})


@login_required
def category(request):
    return render(request,'quiz/category.html')

@login_required
def quizroom(request):
    return render(request, 'quiz/html/quizroom.html')

@login_required
def html2(request):
    quizname = Html2.objects.all()
    context = {
        'quizname':quizname
    }
    return render(request,'quiz/html/html2.html',context)

@login_required
def html3(request):
    return render(request,'quiz/html/html3.html')


@login_required
def html4(request):
    html4 = Html4.objects.all()
    return render(request,'quiz/html/html4.html',{'html4':html4})

@login_required
def html5(request):
    html5 = Html5.objects.all()
    return render(request,'quiz/html/html5.html',{'html5':html5})

@login_required
def css1(request):
     return render(request,'quiz/css/quiz1.html')


@login_required
def css2(request):
     return render(request,'quiz/css/quiz2.html')

@login_required
def css3(request):
     return render(request,'quiz/css/quiz3.html')

@login_required
def css4(request):
     return render(request,'quiz/css/quiz4.html')

@login_required
def css5(request):
     return render(request,'quiz/css/quiz5.html')


@login_required
def js1(request):
    return render(request,'quiz/javascript/quiz1.html')

@login_required
def js2(request):
    return render(request,'quiz/javascript/quiz2.html')

@login_required
def js3(request):
    return render(request,'quiz/javascript/quiz3.html')

@login_required
def js4(request):
    return render(request,'quiz/javascript/quiz4.html')

@login_required
def js5(request):
    return render(request,'quiz/javascript/quiz5.html')


@login_required
def django1(request):
    return render(request, 'quiz/django/quiz1.html')

@login_required
def django2(request):
    return render(request, 'quiz/django/quiz2.html')

@login_required
def django3(request):
    return render(request, 'quiz/django/quiz3.html')

@login_required
def django4(request):
    return render(request, 'quiz/django/quiz4.html')

@login_required
def django5(request):
    return render(request, 'quiz/django/quiz5.html')


@login_required
def vuejs1(request):
    return render(request, 'quiz/vuejs/quiz1.html')

@login_required
def vuejs2(request):
    return render(request, 'quiz/vuejs/quiz2.html')

@login_required
def vuejs3(request):
    return render(request, 'quiz/vuejs/quiz3.html')

@login_required
def vuejs4(request):
    return render(request, 'quiz/vuejs/quiz4.html')

@login_required
def vuejs5(request):
    return render(request, 'quiz/vuejs/quiz5.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'quiz/accounts/signupuser.html', {'form': UserCreationForm()})
    else:
        #create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('main')
            except IntegrityError:
                return render(request, 'quiz/accounts/signupuser.html',{'forms':UserCreationForm(),'error':"That user name has been taken. Please try someother username"})
        else:
            return render(request, 'quiz/accounts/signupuser.html',{'forms':UserCreationForm(), 'error':'password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'quiz/accounts/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request,username = request.POST['username'],password = request.POST['password'])
        if user is None:
            return render(request, 'quiz/accounts/loginuser.html', {'form':AuthenticationForm,'error':'Username and password did not match'})
        else:
            login(request,user)
            return redirect('main')

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
  

def profile(request):
    scores = Results.objects.filter(username=request.user)
    return render(request,'quiz/profile.html',{'scores':scores})

def profileedit(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)


        if form.is_valid():
            form.save()
            return redirect('profile/')

        else:
            form = UserChangeForm(instance=request.user)
            context = {
                'form':form
            }
            return render(request,'quiz/profileedit.html',context)

#api(html1)

class QuizAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers

class QuizAPIDetailView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers

# #api(html2)
        
class HtmlAPItwo(generics.RetrieveUpdateDestroyAPIView):
      queryset = Html2.objects.all()
      serializer_class = Html2Serializers

class HtmlAPIDetailtwo(generics.ListCreateAPIView):
     queryset = Html2.objects.all()
     serializer_class = Html2Serializers


# #api(html3)
        
class HtmlAPIthree(generics.RetrieveUpdateDestroyAPIView):
      queryset = Html3.objects.all()
      serializer_class = Html3Serializers

class HtmlAPIDetailthree(generics.ListCreateAPIView):
     queryset = Html3.objects.all()
     serializer_class = Html3Serializers

# #api(html4)
        
class HtmlAPIfour(generics.RetrieveUpdateDestroyAPIView):
      queryset = Html4.objects.all()
      serializer_class = Html4Serializers

class HtmlAPIDetailfour(generics.ListCreateAPIView):
     queryset = Html4.objects.all()
     serializer_class = Html4Serializers


# #api(html5)
        
class HtmlAPIfive(generics.RetrieveUpdateDestroyAPIView):
      queryset = Html5.objects.all()
      serializer_class = Html5Serializers

class HtmlAPIDetailfive(generics.ListCreateAPIView):
     queryset = Html5.objects.all()
     serializer_class = Html5Serializers


# #api(css1)
        
class CssAPIone(generics.RetrieveUpdateDestroyAPIView):
      queryset = Css1.objects.all()
      serializer_class = Css1Serializers

class CssAPIDetailone(generics.ListCreateAPIView):
     queryset = Css1.objects.all()
     serializer_class = Css1Serializers

# #api(css2)
        
class CssAPItwo(generics.RetrieveUpdateDestroyAPIView):
      queryset = Css2.objects.all()
      serializer_class = Css2Serializers

class CssAPIDetailtwo(generics.ListCreateAPIView):
     queryset = Css2.objects.all()
     serializer_class = Css2Serializers

# #api(css3)
        
class CssAPIthree(generics.RetrieveUpdateDestroyAPIView):
      queryset = Css3.objects.all()
      serializer_class = Css3Serializers

class CssAPIDetailthree(generics.ListCreateAPIView):
     queryset = Css3.objects.all()
     serializer_class = Css3Serializers


# #api(css4)
        
class CssAPIfour(generics.RetrieveUpdateDestroyAPIView):
      queryset = Css4.objects.all()
      serializer_class = Css4Serializers

class CssAPIDetailfour(generics.ListCreateAPIView):
     queryset = Css4.objects.all()
     serializer_class = Css4Serializers


# #api(css5)
        
class CssAPIfive(generics.RetrieveUpdateDestroyAPIView):
      queryset = Css5.objects.all()
      serializer_class = Css5Serializers

class CssAPIDetailtfive(generics.ListCreateAPIView):
     queryset = Css5.objects.all()
     serializer_class = Css5Serializers


# #api(js1)
        
class JsAPIone(generics.RetrieveUpdateDestroyAPIView):
      queryset = Js1.objects.all()
      serializer_class = Js1Serializers

class JsAPIDetailone(generics.ListCreateAPIView):
     queryset = Js1.objects.all()
     serializer_class = Js1Serializers


 #api(js2)
        
class JsAPItwo(generics.RetrieveUpdateDestroyAPIView):
      queryset = Js2.objects.all()
      serializer_class = Js2Serializers

class JsAPIDetailtwo(generics.ListCreateAPIView):
     queryset = Js2.objects.all()
     serializer_class = Js2Serializers

##api(js3)
        
class JsAPIthree(generics.RetrieveUpdateDestroyAPIView):
      queryset = Js3.objects.all()
      serializer_class = Js3Serializers

class JsAPIDetailthree(generics.ListCreateAPIView):
     queryset = Js3.objects.all()
     serializer_class = Js3Serializers


# #api(js4)
        
class JsAPIfour(generics.RetrieveUpdateDestroyAPIView):
      queryset = Js4.objects.all()
      serializer_class = Js4Serializers

class JsAPIDetailfour(generics.ListCreateAPIView):
     queryset = Js4.objects.all()
     serializer_class = Js4Serializers

# #api(js5)
        
class JsAPIfive(generics.RetrieveUpdateDestroyAPIView):
      queryset = Js5.objects.all()
      serializer_class = Js5Serializers

class JsAPIDetailtfive(generics.ListCreateAPIView):
     queryset = Js5.objects.all()
     serializer_class = Js5Serializers


# #api(django1)
        
class DjangoAPIone(generics.RetrieveUpdateDestroyAPIView):
      queryset = Django1.objects.all()
      serializer_class = Django1Serializers

class DjangoAPIDetailone(generics.ListCreateAPIView):
     queryset = Django1.objects.all()
     serializer_class = Django1Serializers


 #api(djs2)
        
class DjangoAPItwo(generics.RetrieveUpdateDestroyAPIView):
      queryset = Django2.objects.all()
      serializer_class = Django2Serializers

class DjangoAPIDetailtwo(generics.ListCreateAPIView):
     queryset = Django2.objects.all()
     serializer_class = Django2Serializers

# #api(djs3)
        
class DjangoAPIthree(generics.RetrieveUpdateDestroyAPIView):
      queryset = Django3.objects.all()
      serializer_class = Django3Serializers

class DjangoAPIDetailthree(generics.ListCreateAPIView):
     queryset = Django3.objects.all()
     serializer_class = Django3Serializers


# #api(djs4)
        
class DjangoAPIfour(generics.RetrieveUpdateDestroyAPIView):
      queryset = Django4.objects.all()
      serializer_class = Django4Serializers

class DjangoAPIDetailfour(generics.ListCreateAPIView):
     queryset = Django4.objects.all()
     serializer_class = Django4Serializers

# #api(djs5)
        
class DjangoAPIfive(generics.RetrieveUpdateDestroyAPIView):
      queryset = Django5.objects.all()
      serializer_class = Django5Serializers

class DjangoAPIDetailtfive(generics.ListCreateAPIView):
     queryset = Django5.objects.all()
     serializer_class = Django5Serializers


# #api(vuejs1)
        
class VueAPIone(generics.RetrieveUpdateDestroyAPIView):
      queryset = Vue1.objects.all()
      serializer_class = Vue1Serializers

class VueAPIDetailone(generics.ListCreateAPIView):
     queryset = Vue1.objects.all()
     serializer_class = Vue1Serializers


 #api(vuejs2)
        
class VueAPItwo(generics.RetrieveUpdateDestroyAPIView):
      queryset = Vue2.objects.all()
      serializer_class = Vue2Serializers

class VueAPIDetailtwo(generics.ListCreateAPIView):
     queryset = Vue2.objects.all()
     serializer_class = Vue2Serializers

# #api(vuejs3)
        
class VueAPIthree(generics.RetrieveUpdateDestroyAPIView):
      queryset = Vue3.objects.all()
      serializer_class = Vue3Serializers

class VueAPIDetailthree(generics.ListCreateAPIView):
     queryset = Vue3.objects.all()
     serializer_class = Vue3Serializers


# #api(vuejs4)
        
class VueAPIfour(generics.RetrieveUpdateDestroyAPIView):
      queryset = Vue4.objects.all()
      serializer_class = Vue4Serializers

class VueAPIDetailfour(generics.ListCreateAPIView):
     queryset = Vue4.objects.all()
     serializer_class = Vue4Serializers

# #api(vuejs5)
        
class VueAPIfive(generics.RetrieveUpdateDestroyAPIView):
      queryset = Vue5.objects.all()
      serializer_class = Vue5Serializers

class VueAPIDetailtfive(generics.ListCreateAPIView):
     queryset = Vue5.objects.all()
     serializer_class = Vue5Serializers
import json


def target_view(request):
    if request.method == 'GET':
        return render(request, 'quiz/html/end.html',{'form':Score()})
    else:
        try:
            form = Score(data=request.POST)
            newscore = form.save(commit=False)
            newscore.user= request.user
            newscore.save()
            return redirect('profile')
        except ValueError:
            return render(request, 'quiz/html/end.html',{'form':Score(), 'error' :'please fill the form properly'})


   
def main(request):
    return render(request,'quiz/main.html')
   
   
   
  