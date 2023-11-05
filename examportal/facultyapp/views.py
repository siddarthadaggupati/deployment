from django.shortcuts import render
from adminapp.models import Faculty,Course,FacultyCoursrMapping, Student
from django.db.models import Q

def checkfacultylogin(request):
    fid = request.POST['username']
    facultypwd = request.POST['password']

    flag = Faculty.objects.filter(Q(facultyid=fid)&Q(password=facultypwd))
    if flag:
        request.session['fid'] = fid
        return render(request, 'faculty/facultyhome.html')
    else:
        msg = "Login Failed"
        return render(request,'faculty/facultylogin.html',{"message":msg})
def facultyhome(request):
    return render(request,'faculty/facultyhome.html')

def facultychangepassword(request):
    if request.method == 'POST':
        name = request.session['fid']
        old = request.POST['opwd']
        new = request.POST['npwd']
        flag = Faculty.objects.filter(Q(facultyid=name) & Q(password=old))
        if flag:
            msg = "Password Updated Sucessfully"
            Faculty.objects.filter(facultyid=name).update(password=new)

        else:
            msg = "Old Password is Incorrect"
        return render(request,'faculty/changepasswordfaculty.html',{'adminuname':name,"message":msg})
    return render(request, 'faculty/changepasswordfaculty.html')

def viewcourse(request):
    fid = request.session['fid']
    mappingcourses = FacultyCoursrMapping.objects.all()
    fcourses=[]
    for course in mappingcourses:
        if(course.faculty.facultyid==int(fid)):
            fcourses.append(course)
    return render(request,'faculty/viewcourses.html',{'fid':fid,'fcourses':fcourses})
def viewstudent(request):
    student = Student.objects.all()
    return render(request,'faculty/viewstudent.html',{'studentdata': student})

def facultyprofile(request):
    user = request.session['fid']
    profile = Faculty.objects.get(facultyid=user)
    return render(request,'faculty/facultyprofile.html',{'profile':profile,'name':user})