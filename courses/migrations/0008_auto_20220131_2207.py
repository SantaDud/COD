# Generated by Django 3.2.5 on 2022-01-31 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codstudent',
            name='from_dept',
        ),
        migrations.RemoveField(
            model_name='codstudent',
            name='to_dept',
        ),
    ]