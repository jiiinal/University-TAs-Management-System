from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
# Create your models here.


class course(models.Model):
    name = models.CharField(max_length=50,null=False)
    courseid =models.CharField(max_length=20,primary_key=True)
    number_of_TA = models.IntegerField(null=False)

class student(models.Model):
    name = models.CharField(max_length=30,null=False)
    pwd = models.CharField(max_length=8,null=False)
    cid = models.ForeignKey(course,on_delete=models.CASCADE)
    mail = models.EmailField(max_length=30,null=False) #login
    batch = models.IntegerField(null=False)
    sid = models.IntegerField(null=False)


class faculty(models.Model):
    name = models.CharField(max_length=30,null=False)
    pwd = models.CharField(max_length=8,null=False)
    cid = models.OneToOneField(course,on_delete=models.CASCADE)
    mail = models.EmailField(max_length=30,null=False,unique=True)#login
    an= models.BooleanField(default=False)


class ta(models.Model):
    name = models.CharField(max_length=30,null=False)
    pwd = models.CharField(max_length=8,null=False)
    cid = models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    mail = models.EmailField(max_length=30,null=False,unique=True)
    year = models.IntegerField(null=False)
    star = models.IntegerField(default=0,null=False)
    status = models.CharField(default='Not Assigned',max_length=12)
    an= models.BooleanField(default=False)

class coordinator(models.Model):
    mail = models.EmailField(max_length=30,null=False,unique=True,default=None)
    pwd = models.CharField(max_length=8,null=False)

class stipendRequest(models.Model):
    Month = models.CharField(blank=False, max_length=20)
    TAObj = models.ForeignKey(ta,on_delete=models.CASCADE, null="False")
    CourseObj = models.ForeignKey(course,on_delete=models.CASCADE)
    FacultyObj = models.ForeignKey(faculty,on_delete=models.CASCADE, null="False")
    choice = (("Approved", 'Approved'), ("Not approved yet", 'Not approved yet'), ("Disapproaaved", 'Disapproved'),)
    status = models.CharField(choices=choice, max_length=20, default="Not approved yet")
    message = models.CharField(blank=True, max_length=100)

class rating(models.Model):
    studentObj = models.ForeignKey(student, on_delete=models.CASCADE)
    TAObj = models.ForeignKey(ta, on_delete=models.CASCADE)
    CourseObj = models.ForeignKey(course, on_delete=models.CASCADE)
    rates= ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rate = models.IntegerField(choices=rates, max_length=1, default=0)