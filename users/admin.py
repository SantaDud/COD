from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomChangeForm as ChangeForm, CustomCreationForm as CreateForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):

    form = ChangeForm
    add_form = CreateForm
    model = CustomUser
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'first_name', 'last_name', 'father_name', 'email', 'password1',
                'password2', 'roll_no', 'seat_no', 'cgpa', 'batch', 'admission_category', 'dept'
            ),
        }),
    )
    fieldsets = (
        ('User Information', {'fields': ('username', 'first_name', 'last_name', 'father_name', 'email', 'password')}),
        ('Student Info', {'fields': ('roll_no', 'seat_no', 'cgpa', 'dept', 'batch', 'admission_category')}),
        ('Permissions', {'fields': ('is_staff','is_superuser')}),
    )
    list_display = ('first_name', 'last_name', 'email', 'username',)

admin.site.register(CustomUser, CustomUserAdmin)