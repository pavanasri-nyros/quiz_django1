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
from .views import  CssAPIDetailfour, CssAPIfour
from .views import  CssAPIDetailtfive, CssAPIfive
from .views import  JsAPIDetailone, JsAPIone
from .views import  JsAPIDetailtwo, JsAPItwo
from .views import  JsAPIDetailthree, JsAPIthree
from .views import  JsAPIDetailfour, JsAPIfour
from .views import  JsAPIDetailtfive,  JsAPIfive
from .views import  DjangoAPIDetailone, DjangoAPIone
from .views import  DjangoAPIDetailtwo, DjangoAPItwo
from .views import  DjangoAPIDetailthree, DjangoAPIthree
from .views import  DjangoAPIDetailfour, DjangoAPIfour
from .views import  DjangoAPIDetailtfive,  DjangoAPIfive
from .views import  VueAPIDetailone, VueAPIone
from .views import  VueAPIDetailtwo, VueAPItwo
from .views import  VueAPIDetailthree, VueAPIthree
from .views import  VueAPIDetailfour, VueAPIfour
from .views import  VueAPIDetailtfive,  VueAPIfive


urlpatterns = [

    path('home', views.home,name = "home"),
    path('', views.main, name = "main"),
    path('profile/',views.profile, name = "profile"),
    path('category/',views.category, name = "category"),


    #html1
    path('quizroom/', views.quizroom , name = "quizroom" ),
    path('api/',QuizAPIDetailView.as_view(),name = "apidetail" ),
    path('api/<int:pk>/',QuizAPIView.as_view(), name = "list"),       
    
    #html2
    path('html2/',views.html2, name = "html2"),
    path('api2/', HtmlAPIDetailtwo.as_view(),name = "quizapidetail" ),
    path('api2/<int:pk>/',HtmlAPItwo.as_view(), name = "list"), 

    #html3
    path('html3/',views.html3, name = "html3"),
     path('api3/', HtmlAPIDetailthree.as_view(),name = "quizapidetail" ),
    path('api3/<int:pk>/',HtmlAPIthree.as_view(), name = "list"), 


    #html4
    path('html4/', views.html4, name = "html4"),
    path('api4/', HtmlAPIDetailfour.as_view(),name = "quizapidetail" ),
    path('api4/<int:pk>/',HtmlAPIfour.as_view(), name = "list"), 

    #html5
    path('html5/', views.html5, name = 'html5'),
    path('api5/', HtmlAPIDetailfive.as_view(),name = "quizapidetail" ),
    path('api5/<int:pk>/',HtmlAPIfive.as_view(), name = "list"), 


    #css1
    path('css1/',views.css1, name='css1'),
    path('api6/', CssAPIDetailone.as_view(),name = "quizapidetail" ),
    path('api6/<int:pk>/',CssAPIone.as_view(), name = "list"), 

    #css2
    path('css2/',views.css2, name='css2'),
    path('api7/', CssAPIDetailtwo.as_view(),name = "quizapidetail" ),
    path('api7/<int:pk>/',CssAPItwo.as_view(), name = "list"), 
     
    #css3
    path('css3/',views.css3, name='css3'),
    path('api8/', CssAPIDetailthree.as_view(),name = "quizapidetail" ),
    path('api8/<int:pk>/',CssAPIthree.as_view(), name = "list"), 

    #css4
    path('css4/',views.css4, name='css4'),
    path('api9/', CssAPIDetailfour.as_view(),name = "quizapidetail" ),
    path('api9/<int:pk>/',CssAPIfour.as_view(), name = "list"), 

    #css5
    path('css5/',views.css5, name='css5'),
    path('api10/', CssAPIDetailtfive.as_view(),name = "quizapidetail" ),
    path('api10/<int:pk>/',CssAPIfive.as_view(), name = "list"), 
   

    #js1
    path('js1/',views.js1, name='js1'),
    path('api11/', JsAPIDetailone.as_view(),name = "quizapidetail" ),
    path('api11/<int:pk>/',JsAPIone.as_view(), name = "list"), 

    #Js2
    path('js2/',views.js2, name='js2'),
    path('api12/', JsAPIDetailtwo.as_view(),name = "quizapidetail" ),
    path('api12/<int:pk>/',JsAPItwo.as_view(), name = "list"), 
     
    #Js3
    path('js3/',views.js3, name='js3'),
    path('api13/', JsAPIDetailthree.as_view(),name = "quizapidetail" ),
    path('api13/<int:pk>/',JsAPIthree.as_view(), name = "list"), 

    #Js4
    path('js4/',views.js4, name='js4'),
    path('api14/', JsAPIDetailfour.as_view(),name = "quizapidetail" ),
    path('api14/<int:pk>/',JsAPIfour.as_view(), name = "list"), 

    #Js5
    path('js5/',views.js5, name='js5'),
    path('api15/', JsAPIDetailtfive.as_view(),name = "quizapidetail" ),
    path('api15/<int:pk>/',JsAPIfive.as_view(), name = "list"), 

     #Django1
    path('django1/',views.django1, name='django1'),
    path('api16/', DjangoAPIDetailone.as_view(),name = "quizapidetail" ),
    path('api116/<int:pk>/',DjangoAPIone.as_view(), name = "list"), 

    #django2
    path('django2/',views.django2, name='django2'),
    path('api17/', DjangoAPIDetailtwo.as_view(),name = "quizapidetail" ),
    path('api17/<int:pk>/',DjangoAPItwo.as_view(), name = "list"), 
     
    #Django3
    path('django3/',views.django3, name='django3'),
    path('api18/', DjangoAPIDetailthree.as_view(),name = "quizapidetail" ),
    path('api18/<int:pk>/',DjangoAPIthree.as_view(), name = "list"), 

    #Django4
    path('django4/',views.django4, name='django4'),
    path('api19/', DjangoAPIDetailfour.as_view(),name = "quizapidetail" ),
    path('api19/<int:pk>/',DjangoAPIfour.as_view(), name = "list"), 

    #dJango5
    path('django5/',views.django5, name='django5'),
    path('api20/', DjangoAPIDetailtfive.as_view(),name = "quizapidetail" ),
    path('api20/<int:pk>/',DjangoAPIfive.as_view(), name = "list"), 
   

    #vuejs1
    path('vuejs1/',views.vuejs1, name='vuejs1'),
    path('api21/', VueAPIDetailone.as_view(),name = "quizapidetail" ),
    path('api21/<int:pk>/',VueAPIone.as_view(), name = "list"), 

    #vueJs2
    path('vuejs2/',views.vuejs2, name='vuejs2'),
    path('api22/', VueAPIDetailtwo.as_view(),name = "quizapidetail" ),
    path('api22/<int:pk>/',VueAPItwo.as_view(), name = "list"), 
     
    #vueJs3
    path('vuejs3/',views.vuejs3, name='vuejs3'),
    path('api23/', VueAPIDetailthree.as_view(),name = "quizapidetail" ),
    path('api23/<int:pk>/',VueAPIthree.as_view(), name = "list"), 

    #vueJs4
    path('vuejs4/',views.vuejs4, name='vuejs4'),
    path('api24/', VueAPIDetailfour.as_view(),name = "quizapidetail" ),
    path('api24/<int:pk>/',VueAPIfour.as_view(), name = "list"), 

    #vueJs5
    path('vuejs5/',views.vuejs5, name='vuejs5'),
    path('api25/', VueAPIDetailtfive.as_view(),name = "quizapidetail" ),
    path('api25/<int:pk>/',VueAPIfive.as_view(), name = "list"), 


   ]
