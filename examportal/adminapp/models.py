from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100, blank=False)

    class Meta:
        db_table = 'admin_table'

    def __str__(self):
        return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)

    department_choices = (("CSE(Regular)","CSE(R)"),("CSE(HONORS)","CSE(H)"),("CS&IT","CSIT") )
    department = models.CharField(max_length=100, blank=False,choices=department_choices)

    prg_choices = (("BTECH", "BTECH"), ("MTECH", "MTECH"))
    program = models.CharField(max_length=100, blank=False, choices=prg_choices)

    acadamic_choices = (("2023-24","2023-2024"), ("2022-23", "2022-2023"))
    acadamicyear = models.CharField(max_length=20,blank=False,choices=acadamic_choices)

    semester_choice = (("ODD","ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=20, blank=False,choices=semester_choice)

    year = models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20, blank=False, unique="true")
    coursetitle = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'course_table'


    def __str__(self):
        return str(self.coursetitle)



class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.BigIntegerField(blank=False,unique=True)
    fullname = models.CharField(max_length=100, blank=False)

    gen_choices = (("MALE","MALE"),("FEMLAE","FEMALE"),("OTHERS","OTHERS"))
    gender = models.CharField(max_length=20, blank=False,choices=gen_choices)

    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(HONORS)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)

    prg_choices = (("BTECH","BTECH"),("MTECH","MTECH"))
    program = models.CharField(max_length=100, blank=False,choices=prg_choices)

    semester_choice = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=20, blank=False,choices=semester_choice)

    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100,blank=False,default='klu123')
    email = models.EmailField(max_length=100,blank=False,unique=True)
    contact = models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table = 'student_table'

    def __str__(self):
        return str(self.studentid)


class Faculty(models.Model) :
    id = models.AutoField(primary_key=True)
    facultyid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)

    gen_choices = (("MALE", "MALE"), ("FEMLAE", "FEMALE"), ("OTHERS", "OTHERS"))
    gender = models.CharField(max_length=10, blank=False,choices=gen_choices)

    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(HONORS)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)


    qual_choices = (("PHD","PHD"),("BTECH", "BTECH"), ("MTECH", "MTECH"))
    qualification = models.CharField(max_length=100, blank=False,choices=qual_choices)

    deg_choices = (("Prof.","professor"), ("Assoc. prof.","Associate professor"), ("Asst.prof.","Assistant professor"))
    designation = models.CharField(max_length=100,blank=False,choices=deg_choices)
    password = models.CharField(max_length=100, blank=False, default='klu123')
    email = models.EmailField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta :
        db_table = 'faculty_table'

    def __str__(self):
        return str(self.facultyid)

class FacultyCoursrMapping(models.Model):
    mappingid = models.AutoField(primary_key = True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    component_choices = (('l','Lecture'),('T','Tutorial'),('P', 'Practial'),('S','Skill'))
    component =  models.CharField(max_length=10,blank=False,choices= component_choices)

    type = models.BooleanField(blank=False)
    section = models.CharField(blank=False)#Integerfield


    class Meta:
        db_table = "facultycoursemapping_table"

    def __str__(self):
        return f"{self.course.coursetitle}-{self.faculty.fullname}"