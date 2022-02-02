from unicodedata import name
from django.urls import path
from .views import PortalView, CourseDetails, BacklogCourses, Form, MeritList


urlpatterns = [
    path('', PortalView, name='portal'),
    path('courseDetails/', CourseDetails, name='coursedetails'),
    path('backlogCourses/', BacklogCourses, name='backlogcourses'),
    path('form/', Form, name='form'),
    path('meritList/', MeritList, name='meritlist'),
]