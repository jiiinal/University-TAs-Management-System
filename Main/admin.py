from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(course)
admin.site.register(student)
admin.site.register(faculty)
admin.site.register(ta)
admin.site.register(coordinator)
admin.site.register(stipendRequest)