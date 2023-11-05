from django import forms
from . import models

class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = "__all__"

class ExamForm(forms.ModelForm):
    class Meta:
        model = models.Exam
        fields = "__all__"