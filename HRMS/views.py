from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render (request,'Hrms/index.html')

def loged(request):
    return render (request,'Hrms/index.html')