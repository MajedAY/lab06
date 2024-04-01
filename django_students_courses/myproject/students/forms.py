from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']  

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class StudentCourseForm(forms.Form):
    student = forms.ModelChoiceField(queryset=None, empty_label=None, widget=forms.HiddenInput())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
