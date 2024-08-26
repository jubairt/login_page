from django.urls import path,include
from login_app import views

urlpatterns = [
    path('', views.logIn, name='logIn'),
    path('home/', views.tohome, name='home'),
    path('logout/', views.tologout, name='logout'),
    path('pract/',views.practice,name='ractice')
    
]

