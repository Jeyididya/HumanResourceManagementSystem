from django.db import models

# Create your models here.

class Employee(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.FloatField(max_length=200)
    sex=models.CharField(max_length=3)
    
    def __str__(self):
        return self.fname+" "+self.lname
    