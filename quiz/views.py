from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import Quiz
from rest_framework import generics
from .serializers import QuizSerializers
# Create your views here.

def home(request):
    return render(request, 'quiz/home.html')

def reverse(request):
    return render(request,'quiz/home.html')

def quizroom(request):
    results = Quiz.objects.all()
    return render(request, 'quiz/quizroom.html',{'result':results[0]})

def questiondetails(request, qid):
    if qid < 8:
        questiondetails = Quiz.objects.all()[qid]
        return render(request, 'quiz/quizroom.html', {'result':questiondetails})
    else:
        return render(request, 'quiz/score.html')

def score(request):
    return render(request,'quiz/score.html')

def query(request):
    return render(request,'quiz/java.html')

#api

class QuizAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers

class QuizAPIDetailView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers





        


        