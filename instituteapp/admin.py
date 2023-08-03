from django.contrib import admin

from .models import Courses



class AdminCourse(admin.ModelAdmin):
    list_display=['course_name','duration','timings','fee','start_date','trainer_name','trainer_exp']





admin.site.register(Courses,AdminCourse)
