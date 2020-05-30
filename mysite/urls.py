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

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path('reset/<uid64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



    
]
