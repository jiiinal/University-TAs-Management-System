
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from Main import models
from Main import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from .models import ta
from .models import faculty
from .models import student
from audioop import reverse

# Create your views here.

def base(request):
    return render(request,'home.html')

def home(request):
    return render(request,'basic.html')


def facultylogin(request):
    return render(request,'basic.html')    
   
def adminlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'hello.html')
        else:
          return render(request,'adminlogin.html')

    return render(request,'adminlogin.html')    

def tas(request):
    if request.method=="POST":
        signupname = request.POST.get('signupname')
        signuppwd = request.POST.get('signuppwd')
        signupmail = request.POST.get('signupmail')
        signupyear = request.POST.get('signupyear')
        tas = ta(name=signupname,pwd=signuppwd, mail=signupmail, year=signupyear)
        tas.save()
        messages.success(request, 'Profile details updated.')
        return redirect('base')
    return render(request, 'tas.html')
     
def facultysignup(request):
    if request.method=="POST":
        facultyname = request.POST.get('facultyname')
        facultypwd = request.POST.get('facultypwd')
        facultymail = request.POST.get('facultymail')
        facultysignup = faculty(name=facultyname,pwd=facultypwd, mail=facultymail)
        facultysignup.save()
        messages.success(request, 'Profile details updated.')
        return redirect('base')
    return render(request, 'facultysignup.html')

def talogin(request):
    if request.method=="POST":
        loginemail = request.POST['loginemail']
        loginpwd = request.POST['loginpwd']
         
        try:
            user = ta.objects.get(mail=loginemail,pwd=loginpwd)
            context={'taid':user.id}
            messages.success(request,"success")
            return render(request, 'TAhome.html', context)
        except :
            user=None
            messages.info(request,"Invalid details")
            return redirect('tas')

    return render(request, 'talogin.html')

def facultylogin(request):
    if request.method=="POST":
        facultymail = request.POST.get('facultymail')
        facultypwd = request.POST.get('facultypwd')
         
        try:
            user = faculty.objects.get(mail=facultymail,pwd=facultypwd)
            messages.success(request,"success")
            return render(request, 'hello.html')
            
        except :
            user=None
            messages.info(request,"Invalid details")
            return redirect('facultysignup')

    return render(request, 'facultylogin.html')    

def studentlogin(request):
    if request.method=="POST":
        studentemail = request.POST['studentemail']
        studentpwd = request.POST['studentpwd']

        try:
            user = student.objects.get(mail=studentemail,pwd=studentpwd)
            messages.success(request,"success")
            return render(request, 'hello.html')

        except:
            user=None
            messages.info(request,"Invalid details")
            return redirect('talogin')

    return render(request, 'studentlogin.html')            


def talogout(request):    
    return HttpResponse('logout')


def TAhome(request):
    return render(request,'TAhome.html')

def StiReq(request):
    return render(request,'stipendReq.html')

def viewCourse(request,id):
    obj = ta.objects.get(id=id)
    #viewFac= faculty.objects.get(cid = obj.cid)
    return render(request, 'viewAssignedCourse.html', { 'viewCourse': obj})

def facultyHome(request):
    return render(request, 'FacultyHome.html')

def studentHome(request):
    return render(request, 'StudentHome.html')

def rateTA(request):
    TA_list= ta.objects.all()
    return render(request, 'rateTA.html', {'TAlist' : TA_list})

def seeReq(request):
    return render(request, 'seeReq.html')

def assignedCourse(request):
    return render( request, 'assignedCourse.html')

def submitPref(request):
    return render(request, 'submitPref.html')


    
def facultyHome(request):
    return render(request, 'FacultyHome.html')

def studentHome(request):
    return render(request, 'StudentHome.html')

def rateTA(request):
    return render(request, 'rateTA.html')

def seeReq(request):
    return render(request, 'seeReq.html')

def assignedCourse(request):
    return render( request, 'assignedCourse.html')

def submitPref(request):
    return render(request, 'submitPref.html')

def seeList(request):
    seeList= ta.objects.all()
    return render(request, 'seeList.html', {'seeList' : seeList})


