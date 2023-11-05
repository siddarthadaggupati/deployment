from django.urls import path
from . import views
urlpatterns = [
    path('facultyhome/',views.facultyhome,name='facultyhome'),
    path('changepasswordfaculty/',views.facultychangepassword,name='changepasswordfaculty'),
    path('viewcourses/', views.viewcourse, name='viewcourses'),
    path('checkfacultylogin/',views.checkfacultylogin,name='checkfacultylogin'),
    path('viewstudent/', views.viewstudent, name='viewstudent'),
    path('facultyprofile/',views.facultyprofile,name='facultyprofile'),
]