from django.urls import path
from . import views
urlpatterns = [
    path('checkstudentlogin/',views.checkstudentlogin,name='checkstudentlogin'),
    path('studenthome/',views.studenthome,name='studenthome'),
    path("studentprofile/", views.profilefunction, name='studentprofile'),
    path("changepasswordstudent/", views.passwordfunction, name='changepasswordstudent'),
    path("live_exam/", views.examfunction, name='live_exam'),
    path("startexam/<int:pk>",views.startexam,name='startexam'),
    path('paymentindex/', views.paymentindex, name='paymentindex'),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
]


'''urlpatterns = [
    path("",views.index,name='index'),
    path("login",views.login,name = 'login'),
    path("home/",views.homefunction,name='home'),
    path("dashboard/",views.dashboardfunction,name='dashboard'),
   
   
   
    path("result/",views.resultfunction,name='result'),

]'''