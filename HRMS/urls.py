from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logged',views.logged,name='logged'),
    path('h',views.h,name='h'),
    
]
