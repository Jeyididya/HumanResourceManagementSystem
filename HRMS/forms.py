from django import forms
from .models import Employee,Attendance


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['username','firstname','lastname','email','password','age','salary','sex']
        
        
class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=['username']