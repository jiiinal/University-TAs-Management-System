from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from .models import ta
from .models import faculty
from audioop import reverse

# Create your views here.

def base(request):
    return render(request,'home.html')

def home(request):
    return render(request,'basic.html')

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

def seeList(request):
    see_List = ta.objects.all()
    return render(request, 'seeList.html', {'seeList' : see_List})
    
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
    TA_list= ta.objects.all()
    return render(request, 'seeList.html', {'seeList' : TA_list})

