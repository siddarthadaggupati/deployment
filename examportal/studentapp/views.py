from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from adminapp.models import Admin,Faculty,Student,Course
import exams.models as models
from . models import Order1
import razorpay
from django.conf import settings
from .constants import PaymentStatus
from django.views.decorators.csrf import csrf_exempt
import json

def checkstudentlogin(request):
    adminuname = request.POST['username']
    adminpwd = request.POST['password']

    flag = Student.objects.filter(Q(studentid=adminuname)&Q(password=adminpwd))
    if flag:
        request.session['adminuname'] = adminuname
        return render(request, 'student/studenthome.html', {'name':adminuname})
    else:
        msg = "Login Failed"
        return render(request,'student/student_login.html',{"message":msg})

def studenthome(request):
    return render(request, 'student/studenthome.html')

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

def paymentindex(request):
    return render(request, "student/paymentindex.html")


def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Order1.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order["id"]
        )
        order.save()
        return render(
            request,
            "student/payment.html",{"callback_url": "http://" + "127.0.0.1:8000" + "/callback/","razorpay_key": 'rzp_test_06GeKary0jkcOO',"order": order})
    return render(request, "student/payment.html")


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order1.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if not verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            return render(request, "student/callback.html", context={"status": order.status})
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "student/callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get("order_id")
        order = Order1.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "callback.html", context={"status": order.status})