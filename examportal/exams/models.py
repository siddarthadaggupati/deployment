from django.db import models
from adminapp.models import Course, Student

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=200)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return str(self.exam_name)

class Question(models.Model):
    exam_name = models.ForeignKey(Exam,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

    def __str__(self):
        return str(self.course)


