from django.contrib import admin
from django.urls import path, include
from quiz import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    #quiz
    path('',include('quiz.urls')),

    path('admin/', admin.site.urls),

    #Auth
    path('signup/',views.signupuser, name = "signupuser"),
    path('login/', views.loginuser, name = "loginuser"),
    path('logout/',views.logoutuser,name = "logoutuser"),

    

    
]
