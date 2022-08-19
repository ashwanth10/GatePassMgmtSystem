from django import forms
from django.forms import ModelForm
from App.models import Student

# form for adding new students
class NewStudentForm(forms.ModelForm):    
    class Meta:
        model = Student
        fields = ['FirstName', 'SecondName', 'Registration', 'Hostel','LaptopSerialNumber']

class StudentUpdateForm(forms.ModelForm):    
    class Meta:
        model = Student
        fields = ['FirstName', 'SecondName', 'Registration', 'Hostel','LaptopSerialNumber']