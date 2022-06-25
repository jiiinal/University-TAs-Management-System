from django.contrib import admin
from django.urls import path
from .views import home
from .views import TAhome
from .views import viewCourse
from .views import StiReq
from .views import studentHome
from .views import facultyHome
from .views import rateTA
from .views import seeReq
from .views import assignedCourse
from .views import submitPref
from .views import seeList
from django.conf.urls.static import static
from django.conf import settings
from Main import views

urlpatterns = [
    path('home/',home),
    path('TA/', TAhome, name='TAhome'),
    path('TA/viewCourse/<str:id>', viewCourse,  name='viewcourse'),
    path('TA/StipendReq/',StiReq),
    path('student/', studentHome),
    path('faculty/', facultyHome),
    path('student/rateTA', rateTA),
    path('faculty/seeRequests', seeReq),
    path('faculty/assignedCourse',assignedCourse),
    path('faculty/submitPreference',submitPref),
    path('faculty/seeTheList',seeList)
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


  
   

    