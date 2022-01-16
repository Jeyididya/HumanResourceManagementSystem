from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logged',views.logged,name='logged'),
    path('h',views.h,name='h'),
    path('register',views.register,name='register'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('userspage',views.userspage,name='userspage'),
    path('attendance',views.attendance,name='attendance'),
    path('attendance',views.attendance,name='attendance'),
    path('editacc',views.editacc,name='editacc'),
    path('viewemployees',views.viewemployees,name='viewemployees'),
    path('confirmattendance',views.confirmattendance,name='confirmattendance'),
    path('salary',views.salary,name='salary'),
    
    
]
