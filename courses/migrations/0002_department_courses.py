# Generated by Django 3.2.5 on 2022-01-31 11:19

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department_Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_list', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='Courses/'), upload_to='static/Courses/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_dept_name', to='courses.department')),
            ],
        ),
    ]