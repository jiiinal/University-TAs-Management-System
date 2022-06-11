from django.db import models

# Create your models here.
class course(models.Model):
    name = models.CharField(max_length=50,null=False)
    courseid =models.CharField(max_length=20,primary_key=True)
    count = models.IntegerField(null=False)


class student(models.Model):
    name = models.CharField(max_length=30,null=False)
    pwd = models.CharField(max_length=8,null=False)
    cid = models.ForeignKey(course,on_delete=models.CASCADE)
    mail = models.CharField(max_length=30,null=False)
    batch = models.IntegerField(null=False)
    sid = models.IntegerField(null=False)


class faculty(models.Model):
    name = models.CharField(max_length=30,null=False)
    pwd = models.CharField(max_length=8,null=False)
    cid = models.ForeignKey(course,on_delete=models.CASCADE)
    mail = models.CharField(max_length=30,null=False)


class ta(models.Model):
    name = models.CharField(max_length=30,null=False)
    pwd = models.CharField(max_length=8,null=False)
    cid = models.ForeignKey(course,on_delete=models.CASCADE)
    mail = models.CharField(max_length=30,null=False)
    year = models.IntegerField(null=False)
    star = models.IntegerField(null=False)
    status = models.CharField(max_length=20)

class coordinator(models.Model):
    coid = models.CharField(max_length=10,null=False)
    pwd = models.CharField(max_length=8,null=False)
