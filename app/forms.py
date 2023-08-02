from django import forms
from app.models import *
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'