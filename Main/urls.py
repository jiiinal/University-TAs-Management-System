from django.contrib import admin
from django.urls import path
from .views import *
from .coviews import *
from django.conf.urls.static import static
from django.conf import settings
from Main.views import *
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
    path('TA/<str:id>', TAhome, name='TAhome'),
    path('TA/viewCourse/<str:id>', viewCourse,  name='viewcourse'),
    path('TA/StipendReq/<str:id>',StiReq, name='StiReq'),
    path('TA/SeePrevReq/<str:id>', PrevReq, name='PrevReq'),
    path('student/', studentHome, name='studentHome'),
    path('student/rateTA', rateTA, name='rateTA'),
    path('faculty/<str:id>', facultyHome, name='facultyHome'),
    path('faculty/seeRequests/<str:id>', seeReq, name='seeRequests'),
    path('faculty/assignedCourse/<str:id>',assignedCourse, name='assignedCourse'),
    path('faculty/submitPreference/<str:id>',submitPref, name='submitPref'),
    path('faculty/seeTheList/<str:id>',seeList, name='seeList'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





  
   

    
