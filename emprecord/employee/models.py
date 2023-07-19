from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empNumber = models.CharField(max_length=60)
    empDept = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=10,null=True)
    joiningDate = models.DateField(null=True)
    def __str__(self):
         return self.user.username



class EmployeeEducation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    courseug = models.CharField(max_length=100,null=True)
    schoolclgug = models.CharField(max_length=100,null=True)
    yearofpassingug = models.CharField(max_length=20,null=True)
    percentageug = models.CharField(max_length=20,null=True)

    coursepg = models.CharField(max_length=100,null=True)
    schoolclgpg = models.CharField(max_length=100,null=True)
    yearofpassingpg = models.CharField(max_length=20,null=True)
    percentagepg = models.CharField(max_length=20,null=True)

    coursessc = models.CharField(max_length=100,null=True)
    schoolclgssc = models.CharField(max_length=100,null=True)
    yearofpassingssc = models.CharField(max_length=20,null=True)
    percentagessc = models.CharField(max_length=20,null=True)

    coursehsc = models.CharField(max_length=100,null=True)
    schoolclghsc = models.CharField(max_length=100,null=True)
    yearofpassinghsc = models.CharField(max_length=20,null=True)
    percentagehsc = models.CharField(max_length=20,null=True)
    
    
    
    def __str__(self):
         return self.user.username


class EmployeeExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company1name = models.CharField(max_length=100,null=True)
    company1desig = models.CharField(max_length=100,null=True)
    company1salary = models.CharField(max_length=20,null=True)
    company1duration = models.CharField(max_length=20,null=True)

    company2name = models.CharField(max_length=100,null=True)
    company2desig = models.CharField(max_length=100,null=True)
    company2salary = models.CharField(max_length=100,null=True)
    company2duration = models.CharField(max_length=100,null=True)

    company3name = models.CharField(max_length=100,null=True)
    company3desig = models.CharField(max_length=100,null=True)
    company3salary = models.CharField(max_length=100,null=True)
    company3duration = models.CharField(max_length=100,null=True)
    
           
    def __str__(self):
         return self.user.username




