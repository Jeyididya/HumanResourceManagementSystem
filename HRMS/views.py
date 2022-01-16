from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from .models import Employee, Attendance
from .forms import EmployeeForm, AttendanceForm
from datetime import date


atte=[]


#######################################

import socket
import sys

HOST = '10.240.212.95'	# Symbolic name, meaning all available interfaces
PORT = 7800	# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print ('Socket bind complete')

#Start listening on socket
s.listen(10)


#############3333


def retnam():
    n=""
    while 1:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        data=conn.recv(1024)
        print(str(data)[2:-1])
        return str(data)[2:-1]
    s.close()
    
    







admin="001"

# Create your views here.
def home(request):
    return render (request,'Hrms/index.html')


def h(request):
    return render (request,'Hrms/h.html')
 
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        
        
        
        form=EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            myuser=User.objects.create_user(username,email,password)
            myuser.first_name=firstname
            myuser.last_name=lastname
            print("successful")
            messages.success(request,"successfully created an Employee")
            return redirect('register')
        else:
            sex=request.POST['sex']
            age=request.POST['age']
            salary=request.POST['salary']
            messages.success(request,"there was an error try again")
            return render (request,'Hrms/register.html',{'username':username,'firstname':firstname,
                                                    'lastname':lastname,'email':email,'password':password,'sex':sex,'age':age,
                                                    'salary':salary})
    else:
        return render (request,'Hrms/register.html')
 
def adminpage(request):
    return render (request,'Hrms/adminpage.html')
def userspage(request):
    return render (request,'Hrms/userspage.html')
def salary(request):
    return render (request,'Hrms/salary.html')
def viewemployees(request):
    data = Employees.objects.all
    stu = {
        "dat": data
    }
    return render(request,"Hrms/viewemployees.html", stu)
def attendance(request):
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    if request.method=="POST":
        print("started============================")
        name=retnam()
        
        da={"name":name+"+"+str(d1),"name1":name}
        return render(request,"HRMS/confirmattendance.html",da)

        request.POST['username']  
    else:    
        return render(request,"Hrms/attendance.html")
    
    #return render (request,'Hrms/attendance.html')

def confirmattendance(request):
    if request.method=="POST":
        form1=AttendanceForm(request.POST or None)
        if form1.is_valid():
            print("valid form")
            if request.POST['username'].split('+')[0] in atte:
                messages.success(request,"attendance already taken!!")
                return redirect("userspage")
            else:
                atte.append(request.POST['username'].split('+')[0])
                form1.save()
                messages.success(request,"attendance taken!!")
                return redirect("userspage")
        else:
            print(str(form1.errors),)
            if("Attendance" in str(form1.errors)):
                messages.success(request,"attendance already taken!!")
            return redirect("userspage")
    else:  
        return render (request,'Hrms/confirmattendance.html')


def editacc(request):
    return render (request,'Hrms/editacc.html')
def logged(request):
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            n={'name':username}
            if username==admin:
                return redirect('adminpage')
            else:
                print('sertual eko############################33')
                return redirect('userspage')
            
        
        else:
            messages.error(request,"bad credentials ")
            return redirect('home')
        
        
    return render (request,'Hrms/logged.html')