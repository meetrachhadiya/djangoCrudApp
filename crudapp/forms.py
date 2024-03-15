from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "standard"]
        widgets = {
            "name" : forms.TextInput(attrs={"class" : "form-control"}),
            "email" : forms.EmailInput(attrs={"class" : "form-control"}),
            "standard" : forms.TextInput(attrs={"class" : "form-control"}),
        }

