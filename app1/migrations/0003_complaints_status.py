# Generated by Django 4.1.7 on 2023-08-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_attendancemodel_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
