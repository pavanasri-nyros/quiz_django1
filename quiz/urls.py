from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.models import User
from .views import QuizAPIView, QuizAPIDetailView
from .views import  HtmlAPIDetailtwo, HtmlAPItwo
from .views import  HtmlAPIDetailthree, HtmlAPIthree
from .views import  HtmlAPIDetailfour, HtmlAPIfour
from .views import  HtmlAPIDetailfive, HtmlAPIfive
from .views import  CssAPIDetailone, CssAPIone
from .views import  CssAPIDetailtwo, CssAPItwo
from .views import  CssAPIDetailthree, CssAPIthree
from .views import  Quiz9Detail, Quiz9API
from .views import  Quiz10Detail, Quiz10API
from .views import  Quiz11Detail, Quiz11API
from .views import  Quiz12Detail, Quiz12API
from .views import  Quiz13Detail, Quiz13API
from .views import  Quiz14Detail, Quiz14API
from .views import  Quiz15Detail, Quiz15API
from .views import  Quiz16Detail, Quiz16API
from .views import  Quiz17Detail, Quiz17API
from .views import  Quiz18Detail, Quiz18API
from .views import  Quiz19Detail, Quiz19API
from .views import  Quiz20Detail, Quiz20API








urlpatterns = [

    path('home', views.home,name = "home"),
    path('main',views.main, name='main'),
    #path('', views.score, name = "score"),
    path('profile/',views.profile, name = "profile"),
    path('category/',views.category, name = "category"),


    #html1
    path('quizroom/', views.quizroom , name = "quizroom" ),
    path('api/',QuizAPIDetailView.as_view(),name = "apidetail" ),
    path('api/<int:pk>/',QuizAPIView.as_view(), name = "list"),       
    
    #html2
    path('quiz2',views.html2, name = "html2"),
    path('api2/', HtmlAPIDetailtwo.as_view(),name = "quizapidetail" ),
    path('api2/<int:pk>/',HtmlAPItwo.as_view(), name = "list"), 

    #html3
    path('quiz3',views.quiz3, name = "quiz3"),
     path('api3/', HtmlAPIDetailthree.as_view(),name = "quizapidetail" ),
    path('api3/<int:pk>/',HtmlAPIthree.as_view(), name = "list"), 


    #html4
    path('quiz4', views.quiz4, name = "quiz4"),
    path('api4/', HtmlAPIDetailfour.as_view(),name = "quizapidetail" ),
    path('api4/<int:pk>/',HtmlAPIfour.as_view(), name = "list"), 

    #html5
    path('quiz5', views.quiz5, name = 'quiz5'),
    path('api5/', HtmlAPIDetailfive.as_view(),name = "quizapidetail" ),
    path('api5/<int:pk>/',HtmlAPIfive.as_view(), name = "list"), 


    #css1
    path('quiz6',views.quiz6, name='quiz6'),
    path('api6/', CssAPIDetailone.as_view(),name = "quizapidetail" ),
    path('api6/<int:pk>/',CssAPIone.as_view(), name = "list"), 

    #css2
    path('quiz7',views.quiz7, name='quiz7'),
    path('api7/', CssAPIDetailtwo.as_view(),name = "quizapidetail" ),
    path('api7/<int:pk>/',CssAPItwo.as_view(), name = "list"), 
     
    #css3
    path('quiz8',views.quiz8, name='quiz8'),
    path('api8/', CssAPIDetailthree.as_view(),name = "quizapidetail" ),
    path('api8/<int:pk>/',CssAPIthree.as_view(), name = "list"),

    #javascript1
    path('quiz9',views.quiz9, name='quiz9'),
    path('quizapi9/', Quiz9Detail.as_view(),name = "quizapidetail" ),
    path('quizapi9/<int:pk>/',Quiz9API.as_view(), name = "list"),
 
   #javascript12
    path('quiz10',views.quiz10, name='quiz10'),
    path('quizapi10/', Quiz10Detail.as_view(),name = "quizapidetail" ),
    path('quizapi10/<int:pk>/',Quiz10API.as_view(), name = "list"),

      #javascript1
    path('quiz11',views.quiz11, name='quiz11'),
    path('quizapi11/', Quiz11Detail.as_view(),name = "quizapidetail" ),
    path('quizapi11/<int:pk>/',Quiz11API.as_view(), name = "list"),
 
   #javascript12
    path('quiz12' ,views.quiz12, name='quiz12'),
    path('quizapi12/', Quiz12Detail.as_view(),name = "quizapidetail" ),
    path('quizapi12/<int:pk>/',Quiz12API.as_view(), name = "list"),

    #django1
    path('quiz13' ,views.quiz13, name='quiz13'),
    path('quizapi13/', Quiz13Detail.as_view(),name = "quizapidetail" ),
    path('quizapi13/<int:pk>/',Quiz13API.as_view(), name = "list"),

    #django2
    path('quiz14' ,views.quiz14, name='quiz14'),
    path('quizapi14/', Quiz14Detail.as_view(),name = "quizapidetail" ),
    path('quizapi14/<int:pk>/',Quiz14API.as_view(), name = "list"),

    #django3
    path('quiz15' ,views.quiz15, name='quiz15'),
    path('quizapi15/', Quiz15Detail.as_view(),name = "quizapidetail" ),
    path('quizapi15/<int:pk>/',Quiz15API.as_view(), name = "list"),

    #django4
    path('quiz16' ,views.quiz16, name='quiz16'),
    path('quizapi16/', Quiz16Detail.as_view(),name = "quizapidetail" ),
    path('quizapi16/<int:pk>/',Quiz16API.as_view(), name = "list"),

#vuejs1
    path('quiz17' ,views.quiz17, name='quiz17'),
    path('quizapi17/', Quiz17Detail.as_view(),name = "quizapidetail" ),
    path('quizapi17/<int:pk>/',Quiz17API.as_view(), name = "list"),

#vuejs1
    path('quiz18' ,views.quiz18, name='quiz18'),
    path('quizapi18/', Quiz18Detail.as_view(),name = "quizapidetail" ),
    path('quizapi18/<int:pk>/',Quiz18API.as_view(), name = "list"),


#vuejs3
    path('quiz19' ,views.quiz19, name='quiz19'),
    path('quizapi19/', Quiz19Detail.as_view(),name = "quizapidetail" ),
    path('quizapi19/<int:pk>/',Quiz19API.as_view(), name = "list"),


#vuejs4
    path('quiz20' ,views.quiz20, name='quiz20'),
    path('quizapi20/', Quiz20Detail.as_view(),name = "quizapidetail" ),
    path('quizapi20/<int:pk>/',Quiz20API.as_view(), name = "list"),



]