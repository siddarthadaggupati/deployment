from django.urls import path
from . import views
urlpatterns = [
    path('adminhome/',views.adminhome,name='adminhome'),
    path('checkadminlogin',views.checkadminlogin,name='checkadminlogin'),
    path('changepasswordadmin/',views.changepasswordadmin,name='changepasswordadmin'),

    #faculty paths
    path('addfaculty/',views.addfaculty,name='addfaculty'),
    path('deletefaculty/',views.deletefaculty,name='deletefaculty'),
    path('facultydeletion/<int:fid>',views.facultydeletion,name='facultydeletion'),
    path('updatefaculty/', views.updatefaculty, name='updatefaculty'),
    path('facultyupdation/<int:sid>', views.facultyupdation, name='facultyupdation'),
    path('admindashboard/',views.admin_dashboard,name = 'admindashboard'),

    #student paths
    path('addstudent/',views.addstudent,name='addstudent'),
    path('deletestudent/',views.deletesudent,name='deletestudent'),
    path('studentdeletion/<int:sid>',views.studentdeletion,name='studentdeletion'),
    path('updatestudent/',views.updatestudent,name='updatestudent'),
    path('studentupdation/<int:sid>',views.studentupdation,name='studentupdation'),

    #courses paths
    path('addcourse/',views.addcourse,name='addcourse'),
    path('deletecourse/', views.deletecourse, name='deletecourse'),
    path('coursedeletion/<int:cid>',views.coursedeletion,name='coursedeletion'),
    path('updatecourse/',views.updatecourse,name='updatecourse'),
    path('courseupdation/<int:sid>',views.courseupdation,name='courseupdation'),


    #changepassword
    path('sendotp/',views.send_otp_email,name='sendotp'),
    path('validate/',views.validate_otp,name='validate_otp'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('adminupdatepwd/',views.adminupdatepwd,name='adminupdatepwd'),

    path('facultycoursemapping/',views.facultycoursemapping,name='facultycoursemapping'),

    path('adminprofile/',views.adminprofile,name='adminprofile'),
    path('updatebeforelogin/',views.updatebeforelogin,name='updatebeforelogin'),
]
