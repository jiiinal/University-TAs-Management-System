from django.contrib import admin
from .models import course,faculty,student,coordinator,ta

# Register your models here.
admin.site.register(course)
admin.site.register(student)
admin.site.register(faculty)
admin.site.register(ta)
admin.site.register(coordinator)
