import json
import requests
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.templatetags.static import static
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *


def add_student(request):
    student_form = addstudent(request.POST or None)
    context = {'form': student_form, 'page_title': 'Add Student'}
    if request.method == 'POST':
        if student_form.is_valid():
            student_form.save()
            messages.success(request,'Student Added Sucessfully')
            return redirect(reverse('gostudent'))
        else:
            messages.error(request, "Cannot Add: ")
    return render(request, 'addstudent.html', context)

def update_student(request,pk):
    key=get_object_or_404(student,id=pk)
    form = addstudent(request.POST or None,instance=key)
    context ={'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Student Updated Sucessfully')
            return redirect(reverse('gostudent'))
        else:
            messages.error(request, "Cannot Update: ")
    return render(request,'updatestudent.html',context)

def delete_student(request,pk):
    key=get_object_or_404(student,id=pk)
    if request.method == 'POST':
        key.delete()
        return redirect(reverse('gostudent'))
    return render(request,'deletestudent.html')


def add_course(request):
    c_form = addcourse()
    context = {'form': c_form, 'page_title': 'Add Course'}
    if request.method == 'POST':
        c_form = addcourse(request.POST)
        if c_form.is_valid():
            c_form.save(commit=False)
            c_form.save()
            messages.success(request,'Course Added Sucessfully')
            return redirect(reverse('gocourse'))
        else:
            messages.error(request, "Cannot Add: ")
    return render(request, 'addcourse.html', context)

def update_course(request,pk):
    key=get_object_or_404(course,pk=pk)
    form = addcourse(request.POST or None,instance=key)
    context ={'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Course Updated Sucessfully')
            return redirect(reverse('gocourse'))
        else:
            messages.error(request, "Cannot Update: ")
    return render(request,'updatecourse.html',context)

def delete_course(request,pk):
    key=get_object_or_404(course,pk=pk)
    if request.method == 'POST':
        key.delete()
        return redirect(reverse('gocourse'))
    return render(request,'deletecourse.html')

def add_faculty(request):
    faculty_form = addfaculty(request.POST or None)
    context = {'form': faculty_form, 'page_title': 'Add Faculty'}
    if request.method == 'POST':
        if faculty_form.is_valid():
            faculty_form.save()
            messages.success(request,'Faculty Added Sucessfully')
            return redirect(reverse('gofaculty'))
        else:
            messages.error(request, "Cannot Add: ")
    return render(request, 'addfaculty.html', context)

def update_faculty(request,pk):
    key=get_object_or_404(faculty,id=pk)
    form = addfaculty(request.POST or None,instance=key)
    context ={'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Faculty Updated Sucessfully')
            return redirect(reverse('gofaculty'))
        else:
            messages.error(request, "Cannot Update: ")
    return render(request,'updatefaculty.html',context)

def delete_faculty(request,pk):
    key=get_object_or_404(faculty,id=pk)
    if request.method == 'POST':
        key.delete()
        return redirect(reverse('gofaculty'))
    return render(request,'deletefaculty.html')

def add_ta(request):
    ta_form = addta(request.POST or None)
    context = {'form': ta_form, 'page_title': 'Add TA'}
    if request.method == 'POST':
        if ta_form.is_valid():
            ta_form.save()
            messages.success(request,'TA Added Sucessfully')
            return redirect(reverse('gota'))
        else:
            messages.error(request, "Cannot Add: ")
    return render(request, 'addta.html', context)

def update_ta(request,pk):
    key=get_object_or_404(ta,id=pk)
    form = addta(request.POST or None,instance=key)
    context ={'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'TA Updated Sucessfully')
            return redirect(reverse('gota'))
        else:
            messages.error(request, "Cannot Update: ")
    return render(request,'updateta.html',context)

def delete_ta(request,pk):
    key=get_object_or_404(ta,id=pk)
    if request.method == 'POST':
        key.delete()
        return redirect(reverse('gota'))
    return render(request,'deleteta.html')

def assignta(request,id):
    key=get_object_or_404(ta,id=id)
    form = allocateta(request.POST or None,instance=key)
    context={'form':form}

    if request.method=='POST':
        if form.is_valid():
                #request.POST['status']='Assigned'
                key=get_object_or_404(ta,id=id)
                ob=form.cleaned_data.get('cid')
                list=ta.objects.filter(cid=ob,status='Assigned').count()
                k=course.objects.get(courseid=ob.courseid)
                if list< k.number_of_TA:
                    form.save()
                    key.cid=ob
                    key.status='Assigned'
                    key.save()
                    messages.success(request,'TA assigned sucessfully.')
                    return redirect(reverse('gota'))
                else :
                    messages.error(request,'Cannot Assigned more than threshold')
                    return redirect(reverse('talist'))
    return render(request,'assignta.html',context)

def reassigntas(request,id):
    key=get_object_or_404(ta,id=id)
    form = allocateta(request.POST or None,instance=key)
    context={'form':form}

    if request.method=='POST':
        if form.is_valid():
                context={'form':form}
                #request.POST['status']='Assigned'
                key=get_object_or_404(ta,id=id)
                ob=form.cleaned_data.get('cid')
                list=ta.objects.filter(cid=ob,status='Assigned').count()
                k=course.objects.get(courseid=ob.courseid)
                if list< k.number_of_TA:
                    form.save()
                    key.cid=ob
                    key.save()
                    messages.success(request,'TA re-assigned sucessfully.')
                    return redirect(reverse('gota'))
                else :
                    messages.error(request,'Cannot Assigned more than threshold')
                    return redirect(reverse('talist2'))
    return render(request,'reassignta.html',context)

def cohome(request):
    context = {
        'page_title': "Co-ordinator Dashboard",
    }
    return render(request, 'cohome.html', context)

def vstudent(request):
    context={}
    context['dataset']=student.objects.all()
    return render(request, 'student.html', context)

def vcourse(request):
    context={}
    context['dataset']=course.objects.all()
    return render(request, 'course.html', context)

def vta(request):
    context={}
    context['dataset']=ta.objects.all()
    return render(request, 'ta.html', context)

def vfaculty(request):
    context={}
    context['dataset']=faculty.objects.all()
    return render(request, 'faculty.html', context)

def talist(request):
    context={}
    context['dataset']=ta.objects.filter(status='Not Assigned')
    return render(request, 'talist.html', context)

def talist2(request):
    context={}
    context['dataset']=ta.objects.filter(status='Assigned')
    return render(request, 'talist2.html', context)


def declare(request):
    return render(request,'announce.html')

def makeannounce(request):
    ob1=ta.objects.all()
    ob2=faculty.objects.all()
    for ob in ob1:
        ob.an=True
        ob.save()
    for ob in ob2:
        ob.an=True
        ob.save()
    return render(request,'cohome.html')

def copref(request):
    return render(request,'copref.html')
