from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 




# Create your views here.
def home(request):
    return render (request,'Hrms/index.html')


def h(request):
    return HttpResponse("hollo")
def logged(request):
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        myuser=User.objects.create_user(username,password)
        myuser.save()
        messages.success(request,"successfuly created")
        
        return redirect('h')
        
    return render (request,'Hrms/logged.html')