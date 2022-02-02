from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    father_name = models.CharField(max_length=20, null=True, blank=True)
    roll_no = models.IntegerField(null=True, blank=True)
    seat_no = models.CharField(max_length=8, null=True, blank=True)
    cgpa = models.FloatField(null=True, blank=True)
    admission_category = models.CharField(max_length=8, null=True, blank=True)
    batch = models.IntegerField(null=True, blank=True)
    dept = models.ForeignKey(to='courses.Department', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return f'{self.username} ({self.email})'