from django.db import models
from users.models import CustomUser as Student
from django.core.files.storage import FileSystemStorage

# Create your models here.
fileStorage = FileSystemStorage(location='Courses/')

class Course(models.Model):
    semester_choices = [('S', 'Spring'), ('F', 'Fall')]
    course_code = models.CharField(max_length=8, primary_key=True)
    course_name = models.CharField(max_length=70)
    credit_hours = models.IntegerField()
    theory_hours = models.IntegerField()
    practical_hours = models.IntegerField()
    semester = models.CharField(max_length=10, choices=semester_choices, default="F")

    def __str__(self):
        return f'{self.course_name} ({self.course_code})'

class Department(models.Model):
    dept_name = models.CharField(max_length=30)
    open_seats = models.IntegerField()
    total_seats = models.IntegerField()
    
    def __str__(self):
        return f'{self.dept_name}'

class DeptCourseImage(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='+')
    course_list = models.ImageField(storage=fileStorage, upload_to='static/Courses/')

    def __str__(self):
        return f'{self.department.dept_name}'

class BacklogCourse(models.Model):
    from_dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='+')
    to_dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='+')
    course1 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course2 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course3 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course4 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course5 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course6 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course7 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course8 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course9 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course10 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course11 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)
    course12 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+', null=True, blank=True, default=-1)

    def __str__(self):
        return f'From {self.from_dept.dept_name} to {self.to_dept.dept_name}'

class CODStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.first_name}'