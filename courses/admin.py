from django.contrib import admin
from .models import Course, Department, BacklogCourse, DeptCourseImage, CODStudent
# Register your models here.

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(CODStudent)
admin.site.register(BacklogCourse)
admin.site.register(DeptCourseImage)