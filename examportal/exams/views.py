from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, ExamForm
from . import models

def liveexams(request):
    courses= models.Exam.objects.all()
    return render(request,'exam/live_exams.html',{'courses':courses})


def addquestion(request):
    forms = QuestionForm()
    if request.method == "POST":
        form1 = QuestionForm(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Question Added Successfully."
            return render(request, 'exam/conductexam.html', {'msg' : message,'forms':forms})
        else:
            message = "Failed to add Question"
            return render(request, 'exam/conductexam.html', {'msg' : message, 'forms' : forms})
    return render(request, 'exam/conductexam.html', {'forms' : forms})

def conductexam(request):
    forms = ExamForm()
    if request.method == "POST":
        form1 = ExamForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/addquestion')
        else:
            message = "Failed to add Exam"
            return render(request, 'exam/addexam.html', {'msg' : message, 'forms' : forms})
    return render(request, 'exam/addexam.html', {'forms' : forms})


def viewquestions(request,pk):
    exam = models.Exam.objects.get(id=pk)
    questions = models.Question.objects.all().filter(exam_name=exam)
    print(questions)
    print(exam)
    return render(request, 'exam/viewquestions.html',{'questions':questions, 'exam':exam})

