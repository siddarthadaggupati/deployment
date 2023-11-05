from django import forms
from .models import Course,Faculty, Student, FacultyCoursrMapping

class AddFacultyForms(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude = {"password"}
        labels = {"facultyid":"Enter Faculty ID","gender":"Select Gender"}


class AddStudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"password"}

class AddCourseForms(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        exclude = {"password"}

class AddFacultyCourseMapping(forms.ModelForm):
    class Meta:
        model = FacultyCoursrMapping
        fields = "__all__"
