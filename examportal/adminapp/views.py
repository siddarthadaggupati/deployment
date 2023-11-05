from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Admin,Faculty,Student,Course
from .forms import AddStudentForms,AddCourseForms,AddFacultyForms, AddFacultyCourseMapping
from django.http import HttpResponse
import random
from django.core.mail import send_mail
from django.conf import settings
#adminhome
def adminhome(request):
    return render(request,'adminhome.html')

#checking admin login
def checkadminlogin(request):
    adminuname = request.POST['username']
    adminpwd = request.POST['password']

    flag = Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    if flag:
        request.session['auname'] = adminuname
        ts = Student.objects.all().count()
        tc = Course.objects.all().count()
        tf = Faculty.objects.all().count()
        return render(request, 'admin_dashboard.html', {'total_student': ts, 'total_course': tc, 'total_faculty': tf,'name':adminuname})
    else:
        msg = "Login Failed"
        return render(request,'adminlogin.html',{"message":msg})

#faculty views
def addfaculty(request):
    forms = AddFacultyForms()
    if request.method == "POST":
        form1 = AddFacultyForms(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Faculty Added Sucessfully."
            return render(request, 'addfaculty.html', {'msg' : message,'forms':forms})
        else:
            message = "Failed to add Faculty"
            return render(request, 'addfaculty.html', {'msg' : message, 'forms' : forms})
    return render(request, 'addfaculty.html', {'forms' : forms})


def deletefaculty(request):
    faculty = Faculty.objects.all()
    #return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request,'deletefaculty.html',{'facultydata': faculty})

def facultydeletion(request,fid):

    Faculty.objects.filter(id=fid).delete()
    #return HttpResponse("Course Deleted Sucessfuly")
    return redirect("deletefaculty")

def updatefaculty(request):
    student = Faculty.objects.all()
    # return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request, 'updatefaculty.html', {'facultydata' : student})

def facultyupdation(request,sid):

    student = get_object_or_404(Faculty,pk=sid)
    if request.method == 'POST':
        form = AddFacultyForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
            message = "Faculty Updation Successful."
            return render(request, 'facultyupdated.html', {'msg' : message, 'form': form})
            #return HttpResponse("Student Updated Successfully")
        else :
            message = "Faculty Updation Failed."
            form = AddFacultyForms(instance=student)
        return render(request, 'facultyupdated.html', {'form': form ,'msg' : message})
    else:
        form = AddFacultyForms(instance=student)
    return render(request,'facultyupdated.html',{'form':form})

#Student views
def addstudent(request):
    forms = AddStudentForms()
    if request.method == "POST":
        form1 = AddStudentForms(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Student Added Successfully."
            return render(request, 'addstudent.html', {'msg' : message,'forms':forms})
        else:
            message = "Failed to add Student"
            return render(request, 'addstudent.html', {'msg' : message, 'forms' : forms})
    return render(request, 'addstudent.html', {'forms' : forms})

def deletesudent(request):
    student = Student.objects.all()
    #return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request,'deletestudent.html',{'studentdata': student})

def studentdeletion(request,sid):

    Student.objects.filter(id=sid).delete()
    #return HttpResponse("Course Deleted Sucessfuly")
    return redirect("deletestudent")

def updatestudent(request):
    student = Student.objects.all()
    # return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request, 'updatestudent.html', {'studentdata' : student})

def studentupdation(request,sid):

    student = get_object_or_404(Student,pk=sid)
    if request.method == 'POST':
        form = AddStudentForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
            message = "Student Updation Successful."
            return render(request, 'studentupdated.html', {'msg' : message, 'form': form})
            #return HttpResponse("Student Updated Successfully")
        else :
            message = "Student Updation Failed."
            form = AddStudentForms(instance=student)
        return render(request, 'studentupdated.html', {'form': form ,'msg' : message})
    else:
        form = AddStudentForms(instance=student)
    return render(request,'studentupdated.html',{'form':form})

#Course views
def addcourse(request):
    forms = AddCourseForms()
    if request.method == "POST":
        form1 = AddCourseForms(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Course Added Successfully."
            return render(request, 'addcourse.html', {'msg' : message,'forms':forms})
        else:
            message = "Failed to add Student"
            return render(request, 'addcourse.html', {'msg' : message, 'forms' : forms})
    return render(request, 'addcourse.html', {'forms' : forms})

def deletecourse(request):
    courses = Course.objects.all()
    #return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request,'deletecourse.html',{'coursedata': courses})

def coursedeletion(request,cid):

    Course.objects.filter(id=cid).delete()
    #return HttpResponse("Course Deleted Sucessfuly")
    return redirect("deletecourse")


def admin_dashboard(request):
    name = request.session['auname']
    ts = Student.objects.all().count()
    tc = Course.objects.all().count()
    tf = Faculty.objects.all().count()
    return render(request,'admin_dashboard.html',{'total_student':ts,'total_course':tc,'total_faculty':tf,'name':name})

def generate_otp():
    return str(random.randint(1000, 9999))

otp_storage = {}
def send_otp_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = generate_otp()
        otp_storage[email] = otp
        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        if Admin.objects.filter(email=email).exists():
            send_mail(subject, message, from_email, recipient_list)
            return render(request, 'validate_otp.html')
        else:
            msg = 'Enter a Valid Mail'
            return render(request, 'send_otp.html',{'msg':msg})
    return render(request, 'send_otp.html')

def validate_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')  # Use get() method to avoid KeyError
        user_otp = request.POST.get('otp', '')  # Use get() method to avoid KeyError

        stored_otp = otp_storage.get(email)

        if user_otp == stored_otp:
            return render(request,'changepassword.html')  # Correct the syntax for passing 'msg'
        else:
            msg = 'Otp Verified Failed'
            return render(request,'validate_otp.html',{'msg':msg})  # Correct the syntax for passing 'msg'

    return render(request, 'validate_otp.html')

def updatebeforelogin(request):
    auname = request.POST['username']
    opwd = request.POST['opwd']
    npwd = request.POST['npwd']
    flag = Admin.objects.filter(email=auname)
    if flag:
        msg = "Password Updated Sucessfully"
        Admin.objects.filter(email=auname).update(password=npwd)
    else:
        msg = "Password Updation Failed"
    return render(request, 'changepassword.html', {"message": msg})


def changepassword(request):
    return render(request,'changepassword.html')

def changepasswordadmin(request):
    return render(request,'changepasswordadmin.html')


def adminupdatepwd(request):
    name = request.session['auname']
    opwd = request.POST['opwd']
    npwd = request.POST['npwd']
    flag = Admin.objects.filter(Q(username=name) & Q(password=opwd))
    if flag:
        msg = "Password Updated Sucessfully"
        Admin.objects.filter(username=name).update(password=npwd)

    else:
        msg = "Old Password is Incorrect"
    return render(request,'changepasswordadmin.html',{'adminuname':name,"message":msg})

def adminprofile(request):
    user = request.session['auname']
    profile = Admin.objects.get(username=user)
    print(profile)
    return render(request,'adminprofile.html',{'profile':profile,'name':user})


def updatecourse(request):
    student = Course.objects.all()
    return render(request, 'updatecourse.html', {'coursedata' : student})

def courseupdation(request,sid):

    student = get_object_or_404(Course,pk=sid)
    if request.method == 'POST':
        form = AddCourseForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
            message = "Course Updation Successful."
            return render(request, 'courseupdated.html', {'msg' : message, 'form': form})
            #return HttpResponse("Student Updated Successfully")
        else :
            message = "Course Updation Failed."
            form = AddCourseForms(instance=student)
        return render(request, 'courseupdated.html', {'form': form ,'msg' : message})
    else:
        form = AddCourseForms(instance=student)
    return render(request,'courseupdated.html',{'form':form})

def facultycoursemapping(request):
    forms = AddFacultyCourseMapping
    if request.method == "POST":
        form1 = AddFacultyCourseMapping(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Faculty Course Mapping Sucessfully."
            return render(request, 'facultycoursemapping.html', {'msg' : message,'forms':forms})
        else:
            message = "Faculty Course Mapping Failed"
            return render(request, 'facultycoursemapping.html', {'msg' : message, 'forms' : forms})
    return render(request, 'facultycoursemapping.html', {'forms' : forms})