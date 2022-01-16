from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from .models import Employee

admin="001"

# Create your views here.
def home(request):
    return render (request,'Hrms/index.html')


def h(request):
    return render (request,'Hrms/h.html')
 
def register(request):
    if request.method=="POST":
        username="004"
        password="004"
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        age=request.POST['age']
        sex=request.POST['sex']
        #firstname=request.POST['username']
        
        
        '''
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.sex=sex
        myuser.age=age
        myuser.save()
        '''
        em=Employee()
        em.fname="mk"
        em.lname="mk"
        em.email="mk"
        em.password='jediandualem@gmail.com'
        em.age=12
        em.salary=12.5
        em.sex="m"
        
        em.save()
        messages.success(request,"successfuly created")
        print("successful")
        
        return redirect('home')
    return render (request,'Hrms/register.html')
 
def adminpage(request):
    return render (request,'Hrms/adminpage.html')
def userspage(request):
    return render (request,'Hrms/userspage.html')

def viewemployees(request):
    data = Employees.objects.all
    stu = {
        "dat": data
    }
    return render(request,"Hrms/viewemployees.html", stu)
def attendance(request):
    return render(request,"Hrms/attendance.html", stu)
    
    #return render (request,'Hrms/attendance.html')
def editacc(request):
    return render (request,'Hrms/editacc.html')
def logged(request):
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            if username==admin:
                return redirect('adminpage')
            else:
                print('sertual eko############################33')
                return redirect('userspage')
            
        
        else:
            messages.error(request,"bad credentials ")
            return redirect('home')
        
        
    return render (request,'Hrms/logged.html')