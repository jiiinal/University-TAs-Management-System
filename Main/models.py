from django.db import models


# Create your models here.

class course(models.Model):
    name = models.CharField(max_length=50,null=False)  
    courseid =models.CharField(max_length=20,primary_key=True)
    number_of_TA= models.IntegerField(null=False)


class student(models.Model):
    name = models.CharField(max_length=30,null=False)
    pwd = models.CharField(max_length=8,null=False)
    cid = models.ForeignKey(course,on_delete=models.CASCADE)
    mail = models.EmailField(max_length=30,null=False,unique=True) 
    batch = models.IntegerField(null=False)
    sid = models.IntegerField(null=False)


class faculty(models.Model):
    name = models.CharField(max_length=30,null=False)
    pwd = models.CharField(max_length=8,null=False)
    cid = models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    mail = models.EmailField(max_length=30,null=False,unique=True)


class ta(models.Model):
    name = models.CharField(max_length=30,null=False)
    pwd = models.CharField(max_length=8,null=False)
    cid = models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    mail = models.EmailField(max_length=30,null=False,unique=True)
    year = models.IntegerField(null=False)
    star = models.IntegerField(default=0,null=False)
    status = models.CharField(default='Not Assigned',max_length=20)

class coordinator(models.Model):
    coid = models.CharField(max_length=10,null=False,unique=True)
    pwd = models.CharField(max_length=8,null=False)
