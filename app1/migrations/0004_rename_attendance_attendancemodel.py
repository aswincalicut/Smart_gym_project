# Generated by Django 4.1.7 on 2023-08-04 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_complaints_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendance',
            new_name='attendancemodel',
        ),
    ]
