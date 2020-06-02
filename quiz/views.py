from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .models import Quiz, Html2, Quiz3, Quiz4, Quiz5, Results
from .models import Quiz6, Quiz7, Quiz8, Quiz9, Quiz10, Quiz11, Quiz12
from .models import Quiz13, Quiz14, Quiz15, Quiz16,Quiz17, Quiz18, Quiz19, Quiz20
from rest_framework import generics
from .serializers import QuizSerializers, Html2Serializers, Html3Serializers, Html4Serializers, Html5Serializers
from .serializers import Css1Serializers, Css2Serializers, Css3Serializers,Quiz9Serializers, Quiz10Serializers
from .serializers import Quiz11Serializers, Quiz12Serializers
from .serializers import Quiz13Serializers, Quiz14Serializers
from .serializers import Quiz15Serializers, Quiz16Serializers
from .serializers import Quiz17Serializers, Quiz18Serializers
from .serializers import Quiz19Serializers, Quiz20Serializers
from django.contrib import messages, auth


from django.contrib.auth.decorators import  login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    return render(request, 'quiz/home.html')


def main(request):
    return render(request,'quiz/main.html')



@login_required
def category(request):
    return render(request,'quiz/category.html')

@login_required
def quizroom(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }

    return render(request, 'quiz/html/quizroom.html',context)

@login_required
def html2(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }

    return render(request,'quiz/html/html2.html',context)

@login_required
def quiz3(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/html/html3.html', context)


@login_required
def quiz4(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/html/html4.html', context)

@login_required
def quiz5(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/html/html5.html',context)

@login_required
def quiz6(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/css/quiz1.html',context)


@login_required
def quiz7(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/css/quiz2.html', context)

@login_required
def quiz8(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/css/quiz3.html', context)

@login_required
def quiz9(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/javascript/quiz1.html',context)

@login_required
def quiz10(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/javascript/quiz2.html', context)

def quiz11(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/javascript/quiz3.html', context)

def quiz12(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/javascript/quiz4.html', context)

def quiz13(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/django/quiz1.html', context)

def quiz14(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/django/quiz2.html', context)

def quiz15(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/django/quiz3.html', context)

def quiz16(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/django/quiz4.html', context)

def quiz17(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/jquery/quiz1.html', context)


def quiz18(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/jquery/quiz2.html', context)

def quiz19(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/jquery/quiz3.html', context)

def quiz20(request):
    name = request.GET.get('name')
    scores = request.GET.get('scores')
    status = request.GET.get('status')
    quizname = request.GET.get('quizname')
    save_data = Results.objects.create(username=name, quizname=quizname, score=scores, status=status)
    context = {
        'data': save_data
    }
    return render(request,'quiz/jquery/quiz4.html', context)



def signupuser(request):

    if request.method == 'POST':

        #get form values

        first_name = request.POST['first_name']

        last_name = request.POST['last_name']

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']


        user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)

        user.save()

        messages.success(request, 'You are now registered and can log in')

        return redirect('loginuser')

    else:

        return render(request, 'quiz/accounts/signupuser.html')



def loginuser(request):

    if request.method == 'POST':

       username = request.POST['username']

       password = request.POST['password']



       user = auth.authenticate(username = username, password = password)



       if user is not None:

           auth.login(request, user)

           messages.success(request, 'you are now logged in')

           return redirect('main')

       else:

           messages.error(request,' Invalid credentials')

           return redirect('loginuser')

            

    else:

       return render(request, 'quiz/accounts/loginuser.html')





def logoutuser(request):

    if request.method == "POST":

        auth.logout(request)

        messages.success(request,'You are now logged out')

        return redirect('home')





# def signupuser(request):
#     if request.method == 'GET':
#         return render(request, 'quiz/accounts/signupuser.html', {'form': UserCreationForm()})
#     else:
#         #create a new user
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('main')
#             except IntegrityError:
#                 return render(request, 'quiz/accounts/signupuser.html',{'forms':UserCreationForm(),'error':"That user name has been taken. Please try someother username"})
#         else:
#             return render(request, 'quiz/accounts/signupuser.html',{'forms':UserCreationForm(), 'error':'password did not match'})

# def loginuser(request):
#     if request.method == 'GET':
#         return render(request, 'quiz/accounts/loginuser.html', {'form':AuthenticationForm()})
#     else:
#         user = authenticate(request,username = request.POST['username'],password = request.POST['password'])
#         if user is None:
#             return render(request, 'quiz/accounts/loginuser.html', {'form':AuthenticationForm,'error':'Username and password did not match'})
#         else:
#             login(request,user)
#             return redirect('main')

# @login_required
# def logoutuser(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect('home')


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
      queryset = Quiz3.objects.all()
      serializer_class = Html3Serializers

class HtmlAPIDetailthree(generics.ListCreateAPIView):
     queryset = Quiz3.objects.all()
     serializer_class = Html3Serializers

# #api(html4)

class HtmlAPIfour(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz4.objects.all()
      serializer_class = Html4Serializers

class HtmlAPIDetailfour(generics.ListCreateAPIView):
     queryset = Quiz4.objects.all()
     serializer_class = Html4Serializers


# #api(html5)

class HtmlAPIfive(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz5.objects.all()
      serializer_class = Html5Serializers

class HtmlAPIDetailfive(generics.ListCreateAPIView):
     queryset = Quiz5.objects.all()
     serializer_class = Html5Serializers


# #api(css1)

class CssAPIone(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz6.objects.all()
      serializer_class = Css1Serializers

class CssAPIDetailone(generics.ListCreateAPIView):
     queryset = Quiz6.objects.all()
     serializer_class = Css1Serializers

# #api(css2)

class CssAPItwo(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz7.objects.all()
      serializer_class = Css2Serializers

class CssAPIDetailtwo(generics.ListCreateAPIView):
     queryset = Quiz7.objects.all()
     serializer_class = Css2Serializers

# #api(css3)

class CssAPIthree(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz8.objects.all()
      serializer_class = Css3Serializers

class CssAPIDetailthree(generics.ListCreateAPIView):
     queryset = Quiz8.objects.all()
     serializer_class = Css3Serializers

#api(quiz9)
class Quiz9API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz9.objects.all()
      serializer_class = Quiz9Serializers

class Quiz9Detail(generics.ListCreateAPIView):
     queryset = Quiz9.objects.all()
     serializer_class = Quiz9Serializers

#api(quiz10)
class Quiz10API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz10.objects.all()
      serializer_class = Quiz10Serializers

class Quiz10Detail(generics.ListCreateAPIView):
     queryset = Quiz10.objects.all()
     serializer_class = Quiz10Serializers

#api(quiz11)
class Quiz11API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz11.objects.all()
      serializer_class = Quiz11Serializers

class Quiz11Detail(generics.ListCreateAPIView):
     queryset = Quiz11.objects.all()
     serializer_class = Quiz11Serializers

#api(quiz12)
class Quiz12API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz12.objects.all()
      serializer_class = Quiz12Serializers

class Quiz12Detail(generics.ListCreateAPIView):
     queryset = Quiz12.objects.all()
     serializer_class = Quiz12Serializers


#api(quiz13)
class Quiz13API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz13.objects.all()
      serializer_class = Quiz13Serializers

class Quiz13Detail(generics.ListCreateAPIView):
     queryset = Quiz13.objects.all()
     serializer_class = Quiz13Serializers

#api(quiz14)
class Quiz14API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz14.objects.all()
      serializer_class = Quiz14Serializers

class Quiz14Detail(generics.ListCreateAPIView):
     queryset = Quiz14.objects.all()
     serializer_class = Quiz14Serializers

#api(quiz15)
class Quiz15API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz15.objects.all()
      serializer_class = Quiz15Serializers

class Quiz15Detail(generics.ListCreateAPIView):
     queryset = Quiz15.objects.all()
     serializer_class = Quiz15Serializers

#api(quiz16)
class Quiz16API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz16.objects.all()
      serializer_class = Quiz16Serializers

class Quiz16Detail(generics.ListCreateAPIView):
     queryset = Quiz16.objects.all()
     serializer_class = Quiz16Serializers

#api(quiz17)
class Quiz17API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz17.objects.all()
      serializer_class = Quiz17Serializers

class Quiz17Detail(generics.ListCreateAPIView):
     queryset = Quiz17.objects.all()
     serializer_class = Quiz17Serializers

#api(quiz18)
class Quiz18API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz18.objects.all()
      serializer_class = Quiz18Serializers

class Quiz18Detail(generics.ListCreateAPIView):
     queryset = Quiz18.objects.all()
     serializer_class = Quiz18Serializers

#api(quiz19)
class Quiz19API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz19.objects.all()
      serializer_class = Quiz19Serializers

class Quiz19Detail(generics.ListCreateAPIView):
     queryset = Quiz19.objects.all()
     serializer_class = Quiz19Serializers


#api(quiz20)
class Quiz20API(generics.RetrieveUpdateDestroyAPIView):
      queryset = Quiz20.objects.all()
      serializer_class = Quiz20Serializers

class Quiz20Detail(generics.ListCreateAPIView):
     queryset = Quiz20.objects.all()
     serializer_class = Quiz20Serializers

