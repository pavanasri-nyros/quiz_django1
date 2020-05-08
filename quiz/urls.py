"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import QuizAPIView, QuizAPIDetailView

urlpatterns = [
    path('', views.home,name = "home"),
    path('quizroom/', views.quizroom , name = "quizroom" ),
    path('<int:qid>/',views.questiondetails,name = "question"),
    path('api/',QuizAPIDetailView.as_view(),name = "apidetail" ),
    path('api/<int:pk>/',QuizAPIView.as_view(), name = "list"),
    path('score/',views.score, name="score"),
    path('query',views.query,name='query'),
    path('quizroom/reverse', views.reverse , name = "reverse" ),


    
]
