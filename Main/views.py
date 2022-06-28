from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from Main import models
from Main import forms
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

def base(request):
    return render(request,'home.html');

def home(request):
    return render(request,'basic.html');
