# Generated by Django 4.1.7 on 2023-08-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_attendance_attendancemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='firstaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='instructor')),
            ],
        ),
    ]