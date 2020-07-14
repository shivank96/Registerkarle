from django.db import models

class CourseModel(models.Model):
    idno = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=50,unique=True)
    facultyname = models.CharField(max_length=50)
    fees = models.FloatField()
    stardate = models.CharField(max_length=50)
    duration = models.IntegerField()
    classtime = models.TimeField()

class StudentModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contactnumber = models.IntegerField(unique=True)
    emailid = models.CharField(unique=True,max_length=100)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default="pending")

