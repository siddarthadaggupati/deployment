from django.shortcuts import render

def adminlogin(request):
    return render(request,'adminlogin.html')

def index(request):
    return render(request,'index.html')

def studentlogin(request):
    return render(request,'studentlogin.html')

def facultylogin(request):
    return render(request,'faculty/facultylogin.html')