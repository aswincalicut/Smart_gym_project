from django.contrib import admin

from app1 import models

# Register your models here.
admin.site.register(models.customuser)
admin.site.register(models.complaints)
admin.site.register(models.attendancemodel)
admin.site.register(models.schedule)
