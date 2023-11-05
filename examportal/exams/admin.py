from django.contrib import admin
from .models import Question,Result,Exam
# Register your models here.
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Exam)