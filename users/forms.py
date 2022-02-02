from dataclasses import fields
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser as Student


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = (
            'username', 'email',
            'password1', 'password2',
            'first_name', 'last_name',
            'father_name', 'roll_no',
            'seat_no', 'cgpa', 'batch',
            'admission_category', 'dept'
        )

class CustomChangeForm(UserChangeForm):
    class Meta:
        model = Student
        fields = (
            'username', 'password',
            'roll_no', 'seat_no', 'cgpa',
            'email'
        )