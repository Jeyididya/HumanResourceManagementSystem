from django.db import models
from django.utils import timezone

# Create your models here.

class Employee(models.Model):
    username=models.CharField(max_length=100,unique=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.FloatField()
    sex=models.CharField(max_length=10)
    
    def __str__(self):
        return self.firstname+" "+self.lastname


class Attendance(models.Model):
    username=models.CharField(max_length=100)
    dat=models.CharField(max_length=100)
    pday = models.DateTimeField(default=timezone.now)

  
class Salary(models.Model):
    username=models.CharField(max_length=100)
    paidmonth=models.CharField(max_length=100)