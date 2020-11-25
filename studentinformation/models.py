from django.db import models

# Create your models here.

class Home(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    major = models.CharField(max_length=500)
    year = models.CharField(max_length=500)
    gpa = models.DecimalField(max_digits=3, decimal_places=1)
    courseid = models.IntegerField()
    coursetitle = models.CharField(max_length=500)
    coursename = models.CharField(max_length=500)
    coursesectioncode = models.IntegerField()
    coursedepartment = models.CharField(max_length=500)
class Students(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    major = models.CharField(max_length=500)
    year = models.CharField(max_length=500)
    gpa = models.DecimalField(max_digits=3, decimal_places=1)
    
class Courses(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursetitle = models.CharField(max_length=500)
    coursename = models.CharField(max_length=500)
    coursesectioncode = models.IntegerField()
    coursedepartment = models.CharField(max_length=500)
    instructorname = models.CharField(max_length=500)
    
class Enrollment(models.Model):
    studentid = models.IntegerField()
    coursetitle = models.CharField(max_length=500)
    
