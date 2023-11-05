from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from adminapp.models import Admin,Faculty,Student,Course
import exams.models as models
def checkstudentlogin(request):
    adminuname = request.POST['username']
    adminpwd = request.POST['password']

    flag = Student.objects.filter(Q(studentid=adminuname)&Q(password=adminpwd))
    if flag:
        request.session['adminuname'] = adminuname
        return render(request, 'student/studenthome.html', {'name':adminuname})
    else:
        msg = "Login Failed"
        return render(request,'student/studentlogin.html',{"message":msg})

def studenthome(request, start_date, end_date):
    calendar_events = models.CalendarEvent.objects.filter(date__range=(start_date, end_date))
    return render(request, 'student/studenthome.html', {'calendar_events': calendar_events})

def passwordfunction(request):
    if request.method == 'POST':
        name = request.session['adminuname']
        old = request.POST['opwd']
        new = request.POST['npwd']
        flag = Student.objects.filter(Q(studentid=name) & Q(password=old))
        if flag:
            msg = "Password Updated Sucessfully"
            Student.objects.filter(studentid=name).update(password=new)

        else:
            msg = "Old Password is Incorrect"
        return render(request,'student/changepassword_student.html',{'adminuname':name,"message":msg})
    return render(request, 'student/changepassword_student.html')

def resultfunction(request):
    return render(request,"student/student_result.html")

def profilefunction(request):
    user = request.session['adminuname']
    profile = Student.objects.get(studentid=user)
    return render(request,'student/student_profile.html',{'profile':profile,'name':user})

def examfunction(request):
    courses= models.Exam.objects.all()
    return render(request,'student/student_viewexams.html',{'courses':courses})

def startexam(request,pk):
    exam = models.Exam.objects.get(id=pk)
    questions = models.Question.objects.all().filter(exam_name=exam)
    return render(request, 'student/startexam.html',{'questions':questions, 'exam':exam})
