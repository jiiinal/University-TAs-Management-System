from django.contrib import admin
from django.urls import path
from .views import home
from .coviews import *
from django.conf.urls.static import static
from django.conf import settings
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
    path('home/',home,name='home'),
    path('cohome/',cohome,name='cohome'),
    path('cohome/student/',vstudent,name='gostudent'),
    path('cohome/course/',vcourse,name='gocourse'),
    path('cohome/ta/',vta,name='gota'),
    path('cohome/faculty/',vfaculty,name='gofaculty'),
    path('cohome/ta/addta',add_ta,name='addta'),
    path('cohome/ta/assignta/<str:id>/',assignta,name='assigntas'),
    path('cohome/ta/reassignta/<str:id>/',reassigntas,name='reassigntas'),
    path('cohome/student/addstudent/',add_student,name='addstudent'),
    path('cohome/course/addcourse/',add_course,name='addcourse'),
    path('cohome/faculty/addfaculty/',add_faculty,name='addfaculty'),
    path('updatestudent/<str:pk>/',update_student,name='updatestudent'),
    path('updatefaculty/<str:pk>/',update_faculty,name='updatefaculty'),
    path('updatecourse/<str:pk>/',update_course,name='updatecourse'),
    path('deletestudent/<str:pk>/',delete_student,name='deletestudent'),
    path('deletecourse/<str:pk>/',delete_course,name='deletecourse'),
    path('deletefaculty/<str:pk>/',delete_faculty,name='deletefaculty'),
    path('updateta/<str:pk>/',update_ta,name='updateta'),
    path('deleteta/<str:pk>/',delete_ta,name='deleteta'),
    path('cohome/ta/talist/',talist,name='talist'),
    path('cohome/ta/talist2/',talist2,name='talist2'),
    path('cohome/makeannounce/',makeannounce,name='makeannounce'),
    path('cohome/declare/',declare,name='declare'),
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





  
   

    
