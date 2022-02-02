from django.shortcuts import redirect, render
from users.models import CustomUser
from .models import BacklogCourse, CODStudent, Department, DeptCourseImage

def PortalView(request):
    template_name = 'courses/portal.html'
    if request.user.is_authenticated:
        return render(request, template_name)
    else:
        return redirect('login')

def CourseDetails(request):
    template_name = 'courses/coursedetails.html'
    if request.user.is_authenticated:
        department_images = DeptCourseImage.objects.all()
        return render(request, template_name, {'depts': department_images})
    else:
        return redirect('login')

def BacklogCourses(request):
    template_name = 'courses/backlogcourses.html'
    if request.user.is_authenticated:
        departments = Department.objects.all()
        if request.method == "GET":
            courses = ""
            return render(request, template_name, {'courses':courses,'depts': departments})
        elif request.method == 'POST':
            from_dept = request.POST.get('from-dept')
            to_dept = request.POST.get('to-dept')
            if from_dept == to_dept:
                return redirect("backlogcourses`")
            courses = BacklogCourse.objects.get(from_dept=from_dept, to_dept=to_dept)
            return render(request, template_name, {'courses': courses, 'depts': departments})
    else:
        return redirect('login')

def Form(request):
    template_name = 'courses/form.html'
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, template_name)
        elif request.method == "POST":
            CODStudent.objects.create(student=CustomUser.objects.get(username=request.user.username))
            return redirect("portal")
    else:
        return redirect("login")

def MeritList(request):
    template_name = 'courses/meritlist.html'
    if request.user.is_authenticated:
        students = CODStudent.objects.all()
        students_array = []
        for std in students:
            students_array.append(std)
        array_length = len(students)
        for i in range(array_length):
            for j in range(i+1, array_length):
                if students_array[i].student.cgpa < students_array[j].student.cgpa:
                    temp = students_array[i]
                    students_array[i] = students_array[j]
                    students_array[j] = temp
        return render(request, template_name, {'students': students_array})
    else:
        return redirect("login")